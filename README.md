# Fake News Detection System

> An AI-powered system that investigates whether AI can detect its own lies by providing both fake news generation and multi-model detection capabilities.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-16+-green.svg)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📑 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Documentation](#-documentation)
- [Architecture](#️-architecture)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [Configuration](#️-configuration)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [System Requirements](#-system-requirements)
- [Access Points](#-access-points)
- [Security Notes](#-security-notes)
- [License](#-license)
- [Team](#-team)
- [Support](#-support)

---

## 🌟 Features

### Detection Module
- 🤖 **Multi-Model Detection**: Combines GPT-4, RoBERTa, CLIP, and zero-shot classification
- ✅ **Fact Verification**: Real-time fact checking using Tavily API and Wikipedia
- 📊 **Rhetorical Analysis**: Detects emotional language and manipulation patterns
- 🔍 **Visual Highlighting**: Highlights problematic sentences with detailed explanations

### Generation Module
- 🎭 **7 Manipulation Strategies**: Loaded language, conspiracy theory, fabricated evidence, and more
- 🎨 **4 Writing Styles**: Formal, sensational, fun, and normal
- 🌐 **4 Topic Domains**: Politics, business, sports, and technology
- 🖼️ **Image Support**: Generate content from images or real news URLs

### User Experience
- 🎯 **Interactive 3D Guide**: Engaging onboarding experience
- 📈 **Analytics Dashboard**: View history and statistics
- 📄 **PDF Export**: Export detection and generation results
- 🔐 **Authentication**: Email/password and Google OAuth support

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Docker (for MongoDB)
- OpenAI API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/Adammm12310/comp9900_git_primer.git
cd comp9900_git_primer

# Start MongoDB
cd backend
docker compose -f docker-compose.mongo.yml up -d

# Install backend dependencies
./setup.sh
# Or manually: pip3 install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys

# Install frontend dependencies
cd ..
npm install
```

### Running the System

```bash
# Terminal 1: Start backend
cd backend
python3 main.py

# Terminal 2: Start frontend
npm run dev
```

**Access the application**: http://localhost:5173

---

## 📖 Documentation

- 📦 **[Setup Guide](docs/SETUP.md)** - Detailed installation instructions
- 🔧 **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- 🌐 **[API Documentation](docs/API.md)** - Complete API reference
- 📊 **[Swagger UI](http://localhost:8000/docs)** - Interactive API docs (when running)

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │  React + TypeScript + Vite
│   (Port 5173)   │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Backend API   │  FastAPI + Python
│   (Port 8000)   │
└────────┬────────┘
         │
    ┌────┴────┬────────────┬──────────┐
    ↓         ↓            ↓          ↓
┌────────┐ ┌──────┐ ┌───────────┐ ┌──────┐
│MongoDB │ │GPT-4 │ │  RoBERTa  │ │ CLIP │
│(27017) │ │ API  │ │   Model   │ │Model │
└────────┘ └──────┘ └───────────┘ └──────┘
```

### Tech Stack

**Frontend:**
- React 19 with TypeScript
- Vite for build tooling
- Tailwind CSS for styling
- Three.js for 3D visualizations

**Backend:**
- FastAPI (Python)
- OpenAI GPT-4 API
- Transformers (RoBERTa, CLIP)
- MongoDB for data persistence
- Tavily API for fact verification

---

## 🎯 Usage Examples

### Detection

```bash
curl -X POST http://localhost:8000/api/detect/improved \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news article here..."}'
```

### Generation

```bash
curl -X POST http://localhost:8000/api/generate/single \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Climate change breakthrough",
    "strategy": "loaded_language",
    "style": "sensational"
  }'
```

See [API Documentation](docs/API.md) for complete examples.

---

## 📁 Project Structure

```
.
├── backend/                 # Backend Python application
│   ├── main.py             # FastAPI entry point
│   ├── services/           # Core services (detection, generation)
│   ├── utils/              # Utilities (auth, verification)
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
│
├── src/                    # Frontend React application
│   ├── pages/             # Page components
│   ├── components/        # Reusable components
│   └── services/          # API client
│
├── docs/                   # Documentation
│   ├── SETUP.md           # Setup guide
│   ├── TROUBLESHOOTING.md # Troubleshooting
│   └── API.md             # API reference
│
├── public/                # Static assets
├── package.json           # Frontend dependencies
└── README.md             # This file
```

---

## ⚙️ Configuration

### Required Environment Variables

Create `backend/.env` with these required variables:

```env
# API Provider (openai or deepseek)
API_PROVIDER=openai

# OpenAI API Key (Required)
OPENAI_API_KEY=your_openai_api_key_here

# MongoDB (default Docker config)
MONGODB_URL=mongodb://admin:admin123@localhost:27017/fakenews_db?authSource=admin

# Optional: Tavily for fact verification
TAVILY_API_KEY=your_tavily_api_key_here
```

**Get API Keys:**
- OpenAI: https://platform.openai.com/api-keys
- Tavily: https://tavily.com/
- DeepSeek: https://platform.deepseek.com/

See [Setup Guide](docs/SETUP.md) for complete configuration options.

---

## 🧪 Testing

### Run Backend Tests

```bash
cd backend
python3 -m unittest tests.test_services -v
```

### Manual Testing

1. Open http://localhost:5173
2. Create an account or sign in
3. Try detection with sample text
4. Generate fake news with different strategies
5. View your history and statistics

---

## 🐛 Troubleshooting

Having issues? Check these first:

- ✅ All services running (backend, frontend, MongoDB)
- ✅ API keys configured in `backend/.env`
- ✅ No port conflicts (8000, 5173, 27017)
- ✅ Python 3.8+ and Node.js 16+ installed

See [Troubleshooting Guide](docs/TROUBLESHOOTING.md) for detailed solutions.

---

## 📊 System Requirements

**Minimum:**
- CPU: 2 cores
- RAM: 4GB
- Storage: 5GB free
- Internet connection

**Recommended:**
- CPU: 4+ cores
- RAM: 8GB+
- Storage: 10GB+ free
- Stable internet connection

---

## 🌐 Access Points

Once running, access these URLs:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **Mongo Express**: http://localhost:8081 (if using Docker)

---

## 🔒 Security Notes

- Never commit `.env` files to version control
- Use strong passwords for MongoDB in production
- Rotate API keys regularly
- Enable HTTPS in production environments

---

## 📝 License

This project is part of a capstone course at UNSW.

---

## 🤝 Contributing

This is an academic project. For contributions, please contact the project maintainers.

---

## 👥 Team

Developed by Team Almond as part of COMP9900 Capstone Project at UNSW.

---

## 📞 Support

- 📖 **Documentation**: Check the [docs](docs/) directory
- 🐛 **Issues**: Review the [Troubleshooting Guide](docs/TROUBLESHOOTING.md)
- 💬 **Questions**: Create an issue on GitHub

---

## 🗺️ Roadmap

- [ ] Add more AI models (BERT, XLNet)
- [ ] Implement WebSocket for real-time updates
- [ ] Add multi-language support
- [ ] Mobile app development
- [ ] Enhanced visualization tools

---

## ⭐ Acknowledgments

- OpenAI for GPT-4 API
- Hugging Face for transformer models
- Tavily for fact-checking API
- UNSW for project support

---

**Made with ❤️ by Team Almond**

*Last Updated: December 2025*
