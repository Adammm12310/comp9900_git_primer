#Fake News Detection System

A comprehensive AI-powered fake news detection and generation system built with React, TypeScript, FastAPI, and multiple ML models. This system investigates whether AI can detect its own lies by providing both fake news generation and multi-model detection capabilities.

##  Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the System](#running-the-system)
- [Access Points](#access-points)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

---

## ✨ Features

### Detection Module
- **Multi-Model Detection**: Combines GPT-4, RoBERTa, CLIP, and Zero-shot classification
- **Fact Verification**: Real-time fact checking using Tavily API and Wikipedia
- **Rhetorical Analysis**: Detects emotional language, loaded terms, and manipulation patterns
- **Cross-Modal Consistency**: Validates temporal, spatial, and logical consistency
- **Visual Highlighting**: Highlights problematic sentences in detection results
- **Detailed Reports**: Provides confidence scores, key factors, and explanations

### Generation Module
- **Multiple Strategies**: 7 different manipulation strategies (loaded language, conspiracy, fabricated evidence, timeline shift, misleading headlines, false urgency, emotional manipulation)
- **Style Options**: 4 writing styles (formal, sensational, fun, normal)
- **Domain Support**: 4 topic domains (politics, business, sports, technology)
- **Auto-Inference**: Automatically infers style and topic from user input
- **Real News Integration**: Can generate from real news articles via URL or text input
- **Image Support**: Can generate topics from image descriptions

### User Interface
- **Interactive 3D Guide**: Engaging onboarding experience
- **History Management**: View detection and generation history
- **Data Visualization**: Statistics and charts by style and topic
- **PDF Export**: Export detection and generation results as PDFs
- **Authentication**: Email/password and OAuth (Google) login support

---

## 🏗️ System Architecture

The system consists of four main components:

1. **Generation Module**: Creates synthetic fake news using GPT-4o with various strategies and styles
2. **Detection Module**: Multi-model fusion detection with external fact verification
3. **User Interface Module**: React-based frontend with interactive components
4. **Backend Infrastructure**: FastAPI backend with MongoDB for data persistence

---

## 📦 Prerequisites

Before installing, ensure you have the following installed on your system:

- **Python 3.8+** (Python 3.9 or 3.10 recommended)
- **Node.js 16+** (Node.js 18+ recommended)
- **npm** or **yarn** (comes with Node.js)
- **Docker** and **Docker Compose** (for MongoDB, optional)
- **Git**

### Verify Prerequisites

```bash
# Check Python version
python3 --version

# Check Node.js version
node --version

# Check npm version
npm --version

# Check Docker (optional, for MongoDB)
docker --version
docker-compose --version
```

---

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/unsw-cse-comp99-3900/capstone-project-25t3-9900-f12a-almond.git
cd capstone-project-25t3-9900-f12a-almond
```

### Step 2: Set Up MongoDB Database

#### Option A: Using Docker Compose (Recommended)

```bash
cd backend
docker-compose -f docker-compose.mongo.yml up -d
```

This will start:
- **MongoDB** on port `27017`
- **Mongo Express** (web UI) on port `8081`

**MongoDB Credentials:**
- Username: `admin`
- Password: `admin123`
- Database: `fakenews_db`

**Access Mongo Express**: http://localhost:8081

#### Option B: Install MongoDB Locally

If you prefer to install MongoDB locally:

1. **macOS** (using Homebrew):
   ```bash
   brew tap mongodb/brew
   brew install mongodb-community
   brew services start mongodb-community
   ```

2. **Linux** (Ubuntu/Debian):
   ```bash
   sudo apt-get install -y mongodb
   sudo systemctl start mongodb
   ```

3. **Windows**: Download and install from [MongoDB website](https://www.mongodb.com/try/download/community)

### Step 3: Backend Setup

```bash
cd backend

# Option 1: Use automatic setup script (Recommended)
chmod +x setup.sh
./setup.sh

# Option 2: Manual setup
# Create logs directory
mkdir -p logs

# Install Python dependencies
pip3 install -r requirements.txt

# Download spaCy English model (Required)
python3 -m spacy download en_core_web_sm

# Download NLTK data (Required)
python3 <<EOF
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
EOF
```

**Note**: The `setup.sh` script handles all of the above automatically!

### Step 4: Frontend Setup

```bash
# From project root directory
npm install
```

This will install all frontend dependencies including React, TypeScript, Vite, and UI libraries.

---

## ⚙️ Configuration

### Backend Configuration

Create a `.env` file in the `backend/` directory:

```bash
cd backend
nano .env  # or use your preferred text editor
```

Add the following configuration:

```env
# OpenAI API Key (Required for generation and detection)
OPENAI_API_KEY=your_openai_api_key_here

# Tavily API Key (Optional, for enhanced fact verification)
TAVILY_API_KEY=your_tavily_api_key_here

# News API Key (Optional, has default public key)
NEWS_API_KEY=your_news_api_key_here

# SerpAPI Key (Optional, for Google News search)
SERPAPI_KEY=your_serpapi_key_here

# MongoDB Configuration
MONGODB_URL=mongodb://admin:admin123@localhost:27017/fakenews_db?authSource=admin
MONGODB_HOST=127.0.0.1
MONGODB_PORT=27017
MONGODB_DATABASE=fakenews_db
MONGODB_USER=admin
MONGODB_PASSWORD=admin123

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=logs/fakenews.log

# Security Configuration (Optional)
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

# PDF Configuration
PDF_STORAGE_BASE_PATH=storage
PDF_AUTO_GENERATE=true
```

**Important**: Replace placeholder values with your actual API keys.

### Getting API Keys

1. **OpenAI API Key** (Required):
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Copy and paste into `.env` file

2. **Tavily API Key** (Optional but recommended):
   - Visit https://tavily.com/
   - Sign up and get your API key
   - Copy and paste into `.env` file

3. **News API Key** (Optional):
   - Visit https://newsapi.org/
   - Sign up for free tier
   - Copy and paste into `.env` file

### Frontend Configuration

The frontend automatically connects to the backend at `http://localhost:8000`. If your backend runs on a different port, create a `.env` file in the project root:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## 🚀 Running the System

### Start MongoDB (if using Docker)

```bash
cd backend
docker-compose -f docker-compose.mongo.yml up -d
```

To stop MongoDB:
```bash
docker-compose -f docker-compose.mongo.yml down
```

### Start Backend Server

```bash
cd backend
python3 main.py
```

The backend will start on **http://localhost:8000**

You should see output like:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Start Frontend Server

Open a **new terminal window** and run:

```bash
# From project root
npm run dev
```

The frontend will start on **http://localhost:5173** (or 5174 if 5173 is busy)

You should see output like:
```
  VITE v7.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### Verify Installation

1. **Check Backend Health**:
   ```bash
   curl http://localhost:8000/health
   ```
   Should return: `{"status":"healthy",...}`

2. **Check Frontend**:
   Open http://localhost:5173 in your browser

3. **Check MongoDB** (if using Docker):
   ```bash
   docker ps | grep mongo
   ```
   Should show running MongoDB container

---

## 🌐 Access Points

Once the system is running, you can access:

- **Frontend Application**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check Endpoint**: http://localhost:8000/health
- **Mongo Express** (if using Docker): http://localhost:8081

---

## 🧪 Testing

### Running Backend Tests

The project includes unit tests for core services:

```bash
cd backend
python3 -m unittest tests.test_services -v
```

### Manual Testing

For manual testing of the full system:

1. **Test Generation**:
   - Go to http://localhost:5173
   - Navigate to "Generate" page
   - Enter a topic or URL
   - Click "Generate"

2. **Test Detection**:
   - Go to http://localhost:5173
   - Navigate to "Detection" page
   - Paste some text or upload an image
   - Click "Detect"

3. **Test Authentication**:
   - Click "Sign In" or "Sign Up"
   - Create an account or use OAuth

---

## 🔍 Troubleshooting

### Backend Issues

#### Problem: "ModuleNotFoundError" or Import Errors

**Solution**:
```bash
cd backend
pip3 install -r requirements.txt --force-reinstall
```

#### Problem: "spaCy model not found"

**Solution**:
```bash
python3 -m spacy download en_core_web_sm
```

#### Problem: "NLTK data not found"

**Solution**:
```bash
python3 <<EOF
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
EOF
```

#### Problem: Models Fail to Load (RoBERTa, CLIP, etc.)

**Solution**: This is normal - the system gracefully degrades. GPT-4 detection will still work. The system continues to function with available models.

#### Problem: "MongoDB connection failed"

**Solution**:
1. Check if MongoDB is running:
   ```bash
   docker ps | grep mongo
   # or
   mongosh --eval "db.adminCommand('ping')"
   ```

2. Verify MongoDB URL in `.env` file matches your setup

3. If using Docker, restart MongoDB:
   ```bash
   docker-compose -f docker-compose.mongo.yml restart
   ```

#### Problem: "OPENAI_API_KEY not found"

**Solution**: Ensure `.env` file exists in `backend/` directory and contains a valid `OPENAI_API_KEY`.

#### Problem: Port 8000 Already in Use

**Solution**:
```bash
# Find process using port 8000
lsof -ti:8000

# Kill the process
kill -9 $(lsof -ti:8000)

# Or change port in main.py
```

### Frontend Issues

#### Problem: "Cannot connect to backend"

**Solution**:
1. Verify backend is running on http://localhost:8000
2. Check browser console for CORS errors
3. Verify `VITE_API_BASE_URL` in frontend `.env` (if set)

#### Problem: "npm install fails"

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### Problem: Port 5173 Already in Use

**Solution**: Vite will automatically use the next available port (5174, 5175, etc.)

### Database Issues

#### Problem: "MongoDB authentication failed"

**Solution**: Verify credentials in `.env` match MongoDB setup:
- Default Docker credentials: `admin` / `admin123`
- Update `MONGODB_URL` if using different credentials

#### Problem: "Database not found"

**Solution**: MongoDB will create the database automatically on first use. Ensure MongoDB is running and accessible.

### Performance Issues

#### Problem: Slow model loading on first run

**Solution**: This is normal. Models are downloaded and cached on first use. Subsequent runs will be faster.

#### Problem: Generation takes too long (>60 seconds)

**Solution**:
- Check internet connection (GPT-4 API calls)
- Verify OpenAI API key is valid
- Check backend logs for errors

---

## 📁 Project Structure

```
capstone-project-25t3-9900-f12a-almond/
├── backend/                    # Backend Python code
│   ├── main.py                # FastAPI application entry point
│   ├── config.py              # Configuration management
│   ├── requirements.txt       # Python dependencies
│   ├── setup.sh              # Automated setup script
│   ├── start.sh              # Start script
│   ├── .env                  # Environment variables (create this)
│   ├── docker-compose.mongo.yml  # MongoDB Docker configuration
│   ├── services/             # Service modules
│   │   ├── detection_service.py      # Baseline detection
│   │   ├── improved_detection.py     # Advanced detection
│   │   ├── generation_service.py     # Fake news generation
│   │   ├── vision_service.py         # Image analysis
│   │   ├── news_service.py           # News API integration
│   │   ├── find_news.py              # News search and ranking
│   │   ├── pdf_service.py            # PDF generation
│   │   └── mongo_service.py          # Database operations
│   ├── utils/                # Utility modules
│   │   ├── security.py       # Authentication and JWT
│   │   ├── tavily_verifier.py    # Tavily fact verification
│   │   └── wikipedia_verifier.py # Wikipedia verification
│   ├── tests/                # Test files
│   │   └── test_services.py  # Unit tests
│   ├── storage/              # Generated PDFs and files
│   └── logs/                 # Application logs
│
├── src/                      # Frontend React code
│   ├── pages/               # Page components
│   │   ├── Home.tsx         # Landing page
│   │   ├── Detection.tsx    # Detection page
│   │   ├── Generate.tsx     # Generation page
│   │   ├── Result.tsx       # Results display
│   │   ├── Profile.tsx      # User profile and history
│   │   └── Sign-in.tsx      # Authentication pages
│   ├── components/          # Reusable components
│   │   ├── Book/           # 3D interactive guide
│   │   ├── Profile/        # Profile and statistics
│   │   └── ui/             # UI components
│   ├── services/           # API service layer
│   │   └── api.ts          # API client
│   └── main.tsx            # React entry point
│
├── public/                  # Static assets
├── package.json            # Frontend dependencies
├── vite.config.ts          # Vite configuration
└── README.md              # This file
```

---

## 🔑 API Endpoints

### Detection Endpoints

- `POST /api/detect/improved` - Advanced detection with multi-model fusion
- `POST /api/detect/baseline` - Baseline detection using individual models

### Generation Endpoints

- `POST /api/generate/single` - Generate fake news article
- `GET /api/generate/strategies` - Get available generation strategies

### Authentication Endpoints

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/firebase_sync` - Firebase OAuth sync

### History and Export

- `GET /api/history/detection` - Get detection history
- `GET /api/history/generation` - Get generation history
- `GET /api/pdf/{record_id}` - Download PDF report

### Utility Endpoints

- `GET /health` - Health check
- `GET /docs` - API documentation (Swagger UI)

---

## 🛠️ Development

### Backend Development

```bash
cd backend
python3 main.py
```

The backend uses:
- **FastAPI** for the web framework
- **Uvicorn** as the ASGI server
- **Pydantic** for data validation
- **MongoDB** for data persistence

### Frontend Development

```bash
npm run dev
```

The frontend uses:
- **React 19** with TypeScript
- **Vite** for build tooling
- **Tailwind CSS** for styling
- **React Router** for navigation

### Building for Production

**Frontend**:
```bash
npm run build
```

**Backend**:
```bash
# Backend runs directly with Python
# For production, use a process manager like PM2 or systemd
```

---

## 📝 Environment Variables Reference

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 | `sk-proj-...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TAVILY_API_KEY` | Tavily API key for fact verification | None |
| `NEWS_API_KEY` | News API key | Public key provided |
| `SERPAPI_KEY` | SerpAPI key for Google News | None |
| `MONGODB_URL` | MongoDB connection string | `mongodb://admin:admin123@localhost:27017/fakenews_db` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `PDF_AUTO_GENERATE` | Auto-generate PDFs | `true` |

---

## 🐳 Docker Usage

### Start MongoDB with Docker

```bash
cd backend
docker-compose -f docker-compose.mongo.yml up -d
```

### Stop MongoDB

```bash
docker-compose -f docker-compose.mongo.yml down
```

### View MongoDB Logs

```bash
docker-compose -f docker-compose.mongo.yml logs -f
```

### Reset MongoDB Data

```bash
docker-compose -f docker-compose.mongo.yml down -v
docker-compose -f docker-compose.mongo.yml up -d
```

---

## 📊 System Requirements

### Minimum Requirements

- **CPU**: 2 cores
- **RAM**: 4GB
- **Storage**: 5GB free space (for models and dependencies)
- **Internet**: Required for API calls and model downloads

### Recommended Requirements

- **CPU**: 4+ cores
- **RAM**: 8GB+
- **Storage**: 10GB+ free space
- **Internet**: Stable connection for real-time API calls

---

## 🔒 Security Notes

1. **Never commit `.env` files** to version control
2. **Use strong passwords** for MongoDB in production
3. **Rotate API keys** regularly
4. **Enable HTTPS** in production
5. **Validate all user inputs** (handled by Pydantic)

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

## 🤝 Contributing

This is a capstone project. For contributions, please contact the project maintainers.

---

## 📄 License

This project is part of a capstone course at UNSW.

---

## 🆘 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review backend logs: `backend/logs/fakenews.log`
3. Check browser console for frontend errors
4. Verify all services are running and accessible

---

## ✅ Quick Start Checklist

- [ ] Clone repository
- [ ] Install prerequisites (Python 3.8+, Node.js 16+)
- [ ] Start MongoDB (Docker or local)
- [ ] Run `backend/setup.sh` or manual setup
- [ ] Create `backend/.env` with API keys
- [ ] Install frontend dependencies: `npm install`
- [ ] Start backend: `cd backend && python3 main.py`
- [ ] Start frontend: `npm run dev`
- [ ] Access http://localhost:5173

---

**Last Updated**: November 2025
