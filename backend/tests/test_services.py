import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

BACKEND_DIR = Path(__file__).resolve().parents[1]
if str(BACKEND_DIR) not in sys.path:
    sys.path.append(str(BACKEND_DIR))

_original_stdout = sys.stdout
_original_stderr = sys.stderr
_silenced_stream = io.StringIO()
sys.stdout = _silenced_stream
sys.stderr = _silenced_stream
try:
    from services.mongo_service import MongoService  # noqa: E402
    from services.pdf_service import PDFService  # noqa: E402
    from services.vision_service import VisionService  # noqa: E402
    from services.generation_service import GenerationService  # noqa: E402
finally:
    sys.stdout = _original_stdout
    sys.stderr = _original_stderr


class VisionServiceTests(unittest.TestCase):
    def setUp(self):
        # Use a dummy key to avoid relying on real secrets
        self.service = VisionService(api_key="test-key")

    def test_prepare_image_data_base64_without_prefix(self):
        raw_b64 = "YWJjMTIz"
        result = self.service._prepare_image_data(raw_b64)
        self.assertTrue(result.startswith("data:image/jpeg;base64,"))
        self.assertTrue(result.endswith(raw_b64))

    def test_to_concise_paragraph_removes_formatting(self):
        messy_text = (
            "**Title**\n"
            "- Bullet item\n"
            "2) Numbered item\n"
            "主要场景描述：Some details appear here."
        )
        cleaned = self.service._to_concise_paragraph(messy_text, max_chars=200)
        self.assertNotIn("*", cleaned)
        self.assertNotIn("- ", cleaned)
        self.assertNotIn("2)", cleaned)
        self.assertNotIn("主要场景描述", cleaned)
        self.assertTrue("Some details" in cleaned)


class PDFServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.service = PDFService(storage_base_path=self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_format_text_escapes_and_truncates(self):
        text = "<tag>&value " + "x" * 50
        formatted = self.service._format_text(text, max_length=40)
        self.assertTrue(formatted.startswith("&lt;tag&gt;&amp;value "))
        self.assertTrue(formatted.endswith("... (truncated)"))


class MongoServiceTests(unittest.TestCase):
    @patch.object(MongoService, "_connect", autospec=True)
    def test_insert_one_handles_exception(self, mock_connect):
        mock_connect.return_value = None
        service = MongoService(url="mongodb://user:pass@localhost:27017/testdb", database="testdb")
        failing_collection = MagicMock()
        failing_collection.insert_one.side_effect = Exception("boom")
        service.db = {"demo": failing_collection}

        result = service.insert_one("demo", {"foo": "bar"})
        self.assertIsNone(result)


class GenerationServiceTests(unittest.TestCase):
    def _make_service(self):
        service = GenerationService.__new__(GenerationService)
        service.fake_news_generator = MagicMock()
        service.fake_news_generator.styles = {"normal": "Style: Normal"}
        service.fake_news_generator.domains = {}
        service.fake_news_generator._format_article = lambda text: text.strip()
        return service

    def test_generate_fake_news_requires_topic(self):
        service = self._make_service()
        result = service.generate_fake_news({})
        self.assertFalse(result["success"])
        self.assertIn("Topic is required", result["error"])

    def test_generate_fake_news_calls_generator(self):
        service = self._make_service()
        service.fake_news_generator.generate_with_strategy.return_value = {"success": True}
        payload = {"topic": "AI news", "strategy": "loaded_language", "style": "formal"}
        result = service.generate_fake_news(payload)
        service.fake_news_generator.generate_with_strategy.assert_called_once()
        self.assertTrue(result["success"])

    def test_generate_from_real_requires_source_text(self):
        service = self._make_service()
        request = {"source_url": "https://example.com"}
        result = service.generate_from_real(request)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "source_text is required")

    def test_generate_from_real_returns_formatted_article(self):
        service = self._make_service()
        mock_response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=" sample article "))],
            usage=SimpleNamespace(prompt_tokens=10, completion_tokens=20, total_tokens=30),
        )
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_response
        service.fake_news_generator.client = mock_client

        request = {
            "source_text": "Original article text",
            "source_url": "https://source.com",
            "topic": "Economy",
        }
        result = service.generate_from_real(request)
        self.assertTrue(result["success"])
        self.assertEqual(result["article"], "sample article")
        self.assertEqual(result["source_url"], "https://source.com")
        self.assertEqual(result["metadata"]["usage"]["total_tokens"], 30)


if __name__ == "__main__":
    unittest.main()

