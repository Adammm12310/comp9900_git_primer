# Detailed Setup Guide

This guide provides step-by-step instructions for setting up the Fake News Detection System.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Configuration](#configuration)
- [Running the System](#running-the-system)
- [Verification](#verification)

---

## Prerequisites

Before installing, ensure you have the following installed:

- **Python 3.8+** (Python 3.9 or 3.10 recommended)
- **Node.js 16+** (Node.js 18+ recommended)
- **npm** or **yarn**
- **Docker** and **Docker Compose** (for MongoDB)
- **Git**

### Verify Prerequisites

```bash
# Check Python version
python3 --version

# Check Node.js version
node --version

# Check npm version
npm --version

# Check Docker
docker --version
docker compose --version
```

---

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/Adammm12310/comp9900_git_primer.git
cd comp9900_git_primer
```

### Step 2: Set Up MongoDB Database

#### Option A: Using Docker Compose (Recommended)

```bash
cd backend
docker compose -f docker-compose.mongo.yml up -d
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

**macOS** (using Homebrew):
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Linux** (Ubuntu/Debian):
```bash
sudo apt-get install -y mongodb
sudo systemctl start mongodb
```

**Windows**: Download from [MongoDB website](https://www.mongodb.com/try/download/community)

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

# Download spaCy English model
python3 -m spacy download en_core_web_sm

# Download NLTK data
python3 <<EOF
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
EOF
```

### Step 4: Frontend Setup

```bash
# From project root directory
npm install
```

---

## Configuration

### Backend Configuration

Create a `.env` file in the `backend/` directory:

```bash
cd backend
nano .env  # or use your preferred text editor
```

Add the following configuration:

```env
# ===== API Provider =====
API_PROVIDER=openai

# ===== DeepSeek API =====
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# ===== OpenAI API (Required) =====
OPENAI_API_KEY=your_openai_api_key_here

# ===== Tavily API (Optional) =====
TAVILY_API_KEY=your_tavily_api_key_here
USE_TAVILY=true

# ===== MongoDB Configuration =====
MONGODB_URL=mongodb://admin:admin123@localhost:27017/fakenews_db?authSource=admin
MONGODB_HOST=127.0.0.1
MONGODB_PORT=27017
MONGODB_DATABASE=fakenews_db
MONGODB_USER=admin
MONGODB_PASSWORD=admin123

# ===== Logging =====
LOG_LEVEL=INFO
LOG_FILE=logs/fakenews.log

# ===== Security =====
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

# ===== PDF Configuration =====
PDF_STORAGE_BASE_PATH=storage
PDF_AUTO_GENERATE=true
```

### Getting API Keys

1. **OpenAI API Key** (Required):
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Copy and paste into `.env` file

2. **DeepSeek API Key** (Alternative):
   - Visit https://platform.deepseek.com/
   - Sign up and get your API key

3. **Tavily API Key** (Optional but recommended):
   - Visit https://tavily.com/
   - Sign up and get your API key

### Frontend Configuration

The frontend automatically connects to `http://localhost:8000`. If your backend runs on a different port, create a `.env` file in the project root:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## Running the System

### Step 1: Start MongoDB (if using Docker)

```bash
cd backend
docker compose -f docker-compose.mongo.yml up -d
```

To stop MongoDB:
```bash
docker compose -f docker-compose.mongo.yml down
```

### Step 2: Start Backend Server

```bash
cd backend
python3 main.py
```

The backend will start on **http://localhost:8000**

You should see output like:
```
INFO:     Started server process
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Start Frontend Server

Open a **new terminal window** and run:

```bash
# From project root
npm run dev
```

The frontend will start on **http://localhost:5173**

You should see output like:
```
VITE v7.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

---

## Verification

### 1. Check Backend Health

```bash
curl http://localhost:8000/health
```

Should return: `{"status":"healthy",...}`

### 2. Check Frontend

Open http://localhost:5173 in your browser

### 3. Check MongoDB (if using Docker)

```bash
docker ps | grep mongo
```

Should show running MongoDB container

---

## Access Points

Once running, you can access:

- **Frontend Application**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Mongo Express** (Docker): http://localhost:8081

---

## System Requirements

### Minimum Requirements

- **CPU**: 2 cores
- **RAM**: 4GB
- **Storage**: 5GB free space
- **Internet**: Required for API calls

### Recommended Requirements

- **CPU**: 4+ cores
- **RAM**: 8GB+
- **Storage**: 10GB+ free space
- **Internet**: Stable connection

---

## Docker Usage

### Start MongoDB

```bash
cd backend
docker compose -f docker-compose.mongo.yml up -d
```

### Stop MongoDB

```bash
docker compose -f docker-compose.mongo.yml down
```

### View Logs

```bash
docker compose -f docker-compose.mongo.yml logs -f
```

### Reset MongoDB Data

```bash
docker compose -f docker-compose.mongo.yml down -v
docker compose -f docker-compose.mongo.yml up -d
```

---

## Environment Variables Reference

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 | `sk-proj-...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | DeepSeek API key | None |
| `TAVILY_API_KEY` | Tavily API key | None |
| `MONGODB_URL` | MongoDB connection string | `mongodb://admin:admin123@localhost:27017/fakenews_db` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `PDF_AUTO_GENERATE` | Auto-generate PDFs | `true` |

---

## Next Steps

After setup is complete:

1. Visit http://localhost:5173
2. Create an account or sign in
3. Try the detection and generation features
4. Check out the [API Documentation](API.md) for integration
5. See [Troubleshooting](TROUBLESHOOTING.md) if you encounter issues
