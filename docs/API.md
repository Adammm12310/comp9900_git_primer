# API Documentation

Complete API reference for the Fake News Detection System.

## Base URL

```
http://localhost:8000
```

## Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Table of Contents

- [Authentication](#authentication)
- [Detection Endpoints](#detection-endpoints)
- [Generation Endpoints](#generation-endpoints)
- [History Endpoints](#history-endpoints)
- [User Endpoints](#user-endpoints)
- [Utility Endpoints](#utility-endpoints)
- [Error Responses](#error-responses)

---

## Authentication

Most endpoints require authentication via JWT tokens.

### Register User

**POST** `/api/auth/register`

Create a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "username": "username"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "username": "username"
  }
}
```

### Login

**POST** `/api/auth/login`

Login with email and password.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "username": "username"
  }
}
```

### Firebase OAuth Sync

**POST** `/api/auth/firebase_sync`

Sync user data from Firebase OAuth.

**Request Body:**
```json
{
  "firebase_uid": "firebase_user_id",
  "email": "user@example.com",
  "display_name": "User Name"
}
```

---

## Detection Endpoints

### Improved Detection

**POST** `/api/detect/improved`

Advanced multi-model fake news detection with fact verification.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "News article text to analyze...",
  "image_url": "https://example.com/image.jpg" // optional
}
```

**Response:**
```json
{
  "is_fake": true,
  "confidence": 0.85,
  "verdict": "likely fake",
  "key_factors": [
    "Multiple factual inconsistencies detected",
    "Emotional language used extensively",
    "Sources could not be verified"
  ],
  "detailed_analysis": {
    "gpt_analysis": {
      "score": 0.9,
      "reasoning": "Analysis details..."
    },
    "fact_check": {
      "verified_claims": 2,
      "unverified_claims": 5
    },
    "rhetorical_analysis": {
      "emotional_score": 0.8,
      "loaded_terms": ["shocking", "unbelievable"]
    }
  },
  "highlighted_text": "<span class='suspicious'>Text...</span>",
  "timestamp": "2025-12-03T12:00:00Z"
}
```

### Baseline Detection

**POST** `/api/detect/baseline`

Simple detection using individual models.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "News article text to analyze..."
}
```

**Response:**
```json
{
  "is_fake": false,
  "confidence": 0.65,
  "model_scores": {
    "gpt4": 0.6,
    "roberta": 0.7
  },
  "timestamp": "2025-12-03T12:00:00Z"
}
```

---

## Generation Endpoints

### Generate Fake News

**POST** `/api/generate/single`

Generate fake news article using specified strategy.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "topic": "Climate change breakthrough",
  "strategy": "loaded_language", // optional
  "style": "sensational", // optional
  "topic_domain": "technology", // optional
  "real_news_url": "https://news.com/article", // optional
  "image_data": "base64_encoded_image" // optional
}
```

**Available Strategies:**
- `loaded_language`
- `conspiracy_theory`
- `fabricated_evidence`
- `timeline_shift`
- `misleading_headline`
- `false_urgency`
- `emotional_manipulation`

**Available Styles:**
- `formal`
- `sensational`
- `fun`
- `normal`

**Available Domains:**
- `politics`
- `business`
- `sports`
- `technology`

**Response:**
```json
{
  "fake_news": "Generated fake news article text...",
  "strategy_used": "loaded_language",
  "style_used": "sensational",
  "topic_domain": "technology",
  "metadata": {
    "original_topic": "Climate change breakthrough",
    "manipulation_techniques": ["emotional language", "unverified claims"]
  },
  "timestamp": "2025-12-03T12:00:00Z"
}
```

### Get Available Strategies

**GET** `/api/generate/strategies`

Get list of available generation strategies.

**Response:**
```json
{
  "strategies": [
    {
      "name": "loaded_language",
      "description": "Uses emotionally charged words"
    },
    {
      "name": "conspiracy_theory",
      "description": "Incorporates conspiracy elements"
    }
  ]
}
```

---

## History Endpoints

### Get Detection History

**GET** `/api/history/detection`

Get user's detection history.

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `limit` (optional): Number of records (default: 50)
- `offset` (optional): Skip records (default: 0)

**Response:**
```json
{
  "history": [
    {
      "id": "record_id",
      "text": "Analyzed text...",
      "result": {
        "is_fake": true,
        "confidence": 0.85
      },
      "timestamp": "2025-12-03T12:00:00Z"
    }
  ],
  "total": 10
}
```

### Get Generation History

**GET** `/api/history/generation`

Get user's generation history.

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `limit` (optional): Number of records (default: 50)
- `offset` (optional): Skip records (default: 0)

**Response:**
```json
{
  "history": [
    {
      "id": "record_id",
      "topic": "Original topic",
      "fake_news": "Generated text...",
      "strategy": "loaded_language",
      "timestamp": "2025-12-03T12:00:00Z"
    }
  ],
  "total": 5
}
```

### Get Statistics

**GET** `/api/history/stats`

Get user's usage statistics.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "total_detections": 25,
  "total_generations": 10,
  "detections_by_verdict": {
    "fake": 15,
    "real": 10
  },
  "generations_by_strategy": {
    "loaded_language": 5,
    "conspiracy_theory": 3,
    "emotional_manipulation": 2
  }
}
```

---

## User Endpoints

### Get User Profile

**GET** `/api/user/profile`

Get current user's profile.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "user_id",
  "email": "user@example.com",
  "username": "username",
  "created_at": "2025-12-01T00:00:00Z",
  "stats": {
    "total_detections": 25,
    "total_generations": 10
  }
}
```

### Update User Profile

**PUT** `/api/user/profile`

Update user profile information.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "username": "new_username",
  "email": "new_email@example.com"
}
```

---

## PDF Export Endpoints

### Download PDF Report

**GET** `/api/pdf/{record_id}`

Download PDF report for a detection or generation record.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
- Content-Type: `application/pdf`
- Binary PDF file

---

## Utility Endpoints

### Health Check

**GET** `/health`

Check system health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-03T12:00:00Z",
  "services": {
    "database": "connected",
    "ai_models": "loaded"
  }
}
```

### System Info

**GET** `/api/system/info`

Get system information.

**Response:**
```json
{
  "version": "1.0.0",
  "models_loaded": ["gpt-4", "roberta", "clip"],
  "api_provider": "openai"
}
```

---

## Error Responses

### Common Error Codes

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Missing or invalid token |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 422 | Validation Error - Invalid data format |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

### Error Response Format

```json
{
  "detail": "Error message description",
  "error_code": "ERROR_CODE",
  "timestamp": "2025-12-03T12:00:00Z"
}
```

### Example Error Responses

**401 Unauthorized:**
```json
{
  "detail": "Could not validate credentials",
  "error_code": "INVALID_TOKEN"
}
```

**422 Validation Error:**
```json
{
  "detail": [
    {
      "loc": ["body", "text"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**429 Rate Limit:**
```json
{
  "detail": "Rate limit exceeded. Please try again later.",
  "error_code": "RATE_LIMIT_EXCEEDED",
  "retry_after": 60
}
```

---

## Rate Limits

- **Detection**: 100 requests per hour per user
- **Generation**: 50 requests per hour per user
- **Authentication**: 10 requests per minute per IP

---

## Authentication Header Format

Include the JWT token in all authenticated requests:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

---

## Example Usage

### Python Example

```python
import requests

BASE_URL = "http://localhost:8000"

# Login
response = requests.post(f"{BASE_URL}/api/auth/login", json={
    "email": "user@example.com",
    "password": "password"
})
token = response.json()["access_token"]

# Detect fake news
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    f"{BASE_URL}/api/detect/improved",
    headers=headers,
    json={"text": "News article to analyze..."}
)
result = response.json()
print(f"Is fake: {result['is_fake']}")
print(f"Confidence: {result['confidence']}")
```

### JavaScript Example

```javascript
const BASE_URL = "http://localhost:8000";

// Login
const loginResponse = await fetch(`${BASE_URL}/api/auth/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    email: "user@example.com",
    password: "password"
  })
});
const { access_token } = await loginResponse.json();

// Detect fake news
const detectResponse = await fetch(`${BASE_URL}/api/detect/improved`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${access_token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    text: "News article to analyze..."
  })
});
const result = await detectResponse.json();
console.log(`Is fake: ${result.is_fake}`);
console.log(`Confidence: ${result.confidence}`);
```

---

## WebSocket Support (Future)

WebSocket endpoints for real-time updates are planned for future releases.

---

## API Versioning

Current API version: `v1`

All endpoints are prefixed with `/api/` for version 1.

---

## Additional Resources

- **Swagger UI**: http://localhost:8000/docs - Interactive API testing
- **ReDoc**: http://localhost:8000/redoc - Alternative documentation
- **Postman Collection**: Available in `/docs/postman/` directory
