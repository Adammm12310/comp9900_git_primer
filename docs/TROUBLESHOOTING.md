# Troubleshooting Guide

This guide helps you resolve common issues with the Fake News Detection System.

## Table of Contents

- [Backend Issues](#backend-issues)
- [Frontend Issues](#frontend-issues)
- [Database Issues](#database-issues)
- [Performance Issues](#performance-issues)
- [API Issues](#api-issues)

---

## Backend Issues

### Problem: "ModuleNotFoundError" or Import Errors

**Solution:**
```bash
cd backend
pip3 install -r requirements.txt --force-reinstall
```

### Problem: "spaCy model not found"

**Solution:**
```bash
python3 -m spacy download en_core_web_sm
```

### Problem: "NLTK data not found"

**Solution:**
```bash
python3 <<EOF
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
EOF
```

### Problem: Models Fail to Load (RoBERTa, CLIP, etc.)

**Explanation**: This is normal - the system gracefully degrades. GPT-4 detection will still work.

**What happens**: The system will continue to function with available models and skip models that fail to load.

### Problem: "MongoDB connection failed"

**Solution:**

1. Check if MongoDB is running:
   ```bash
   docker ps | grep mongo
   # or for local installation
   mongosh --eval "db.adminCommand('ping')"
   ```

2. Verify MongoDB URL in `.env` file matches your setup

3. If using Docker, restart MongoDB:
   ```bash
   docker compose -f docker-compose.mongo.yml restart
   ```

### Problem: "OPENAI_API_KEY not found"

**Solution**: Ensure `.env` file exists in `backend/` directory and contains a valid `OPENAI_API_KEY`.

```bash
# Check if .env exists
ls -la backend/.env

# If not, create it from template
cp backend/.env.example backend/.env
# Then edit and add your API keys
```

### Problem: Port 8000 Already in Use

**Solution:**

```bash
# Find process using port 8000
lsof -ti:8000

# Kill the process
kill -9 $(lsof -ti:8000)

# Or change port in main.py (line with uvicorn.run)
```

### Problem: Python Version Incompatibility

**Symptoms**: Import errors, package installation failures

**Solution:**

Check your Python version:
```bash
python3 --version
```

Required: Python 3.8+, Recommended: Python 3.9 or 3.10

If using Python 3.12+, some packages may have compatibility issues. Consider using Python 3.10.

---

## Frontend Issues

### Problem: "Cannot connect to backend"

**Solution:**

1. Verify backend is running on http://localhost:8000
   ```bash
   curl http://localhost:8000/health
   ```

2. Check browser console for CORS errors

3. Verify `VITE_API_BASE_URL` in frontend `.env` (if set)

4. Ensure backend started successfully (check terminal output)

### Problem: "npm install fails"

**Solution:**

```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Problem: Port 5173 Already in Use

**Solution**: Vite will automatically use the next available port (5174, 5175, etc.)

You can also specify a different port:
```bash
npm run dev -- --port 3000
```

### Problem: Node.js Version Warning

**Symptoms**: Warning about unsupported Node.js version

**Solution:**

Current project works with Node.js 20.17.0 despite warnings. If you want to upgrade:

```bash
# Using nvm (recommended)
nvm install 22
nvm use 22

# Or download from nodejs.org
```

### Problem: Build Errors

**Solution:**

```bash
# Clear cache and rebuild
rm -rf dist
npm run build
```

---

## Database Issues

### Problem: "MongoDB authentication failed"

**Solution**:

Verify credentials in `.env` match MongoDB setup:
- Default Docker credentials: `admin` / `admin123`
- Update `MONGODB_URL` if using different credentials

```env
MONGODB_URL=mongodb://admin:admin123@localhost:27017/fakenews_db?authSource=admin
```

### Problem: "Database not found"

**Solution**: MongoDB will create the database automatically on first use. Ensure:
1. MongoDB is running
2. MongoDB is accessible
3. Credentials are correct

### Problem: Docker Container Won't Start

**Solution:**

```bash
# Check Docker status
docker ps -a

# View container logs
docker compose -f docker-compose.mongo.yml logs

# Remove and recreate containers
docker compose -f docker-compose.mongo.yml down -v
docker compose -f docker-compose.mongo.yml up -d
```

### Problem: "Cannot Connect to MongoDB"

**Solution:**

Check if port 27017 is available:
```bash
lsof -i :27017
```

If another process is using it:
```bash
# Kill the process
kill -9 $(lsof -ti:27017)

# Or change MongoDB port in docker-compose.mongo.yml
```

---

## Performance Issues

### Problem: Slow Model Loading on First Run

**Explanation**: This is normal. Models are downloaded and cached on first use.

**Solution**:
- Be patient during first run (can take 5-10 minutes)
- Subsequent runs will be faster
- Ensure stable internet connection

### Problem: Generation Takes Too Long (>60 seconds)

**Possible Causes:**
1. Slow internet connection
2. OpenAI API rate limits
3. Invalid API key

**Solution:**

1. Check internet connection
2. Verify OpenAI API key is valid:
   ```bash
   curl https://api.openai.com/v1/models \
     -H "Authorization: Bearer YOUR_API_KEY"
   ```
3. Check backend logs for errors:
   ```bash
   tail -f backend/logs/fakenews.log
   ```

### Problem: High Memory Usage

**Solution:**

1. Increase system RAM (recommended: 8GB+)
2. Close other applications
3. Restart the backend service

### Problem: Detection Takes Too Long

**Explanation**: Multi-model detection is computationally intensive

**Solutions:**
- Use baseline detection instead of improved detection
- Ensure models are cached (after first run)
- Check system resources (CPU, RAM)

---

## API Issues

### Problem: "Invalid API Key" Error

**Solution:**

1. Verify API key in `.env` file
2. Check for extra spaces or newlines
3. Ensure API key hasn't expired
4. Test API key directly:
   ```bash
   curl https://api.openai.com/v1/models \
     -H "Authorization: Bearer YOUR_OPENAI_API_KEY"
   ```

### Problem: "Rate Limit Exceeded"

**Explanation**: You've exceeded your API quota

**Solution:**
1. Check your OpenAI usage at https://platform.openai.com/usage
2. Upgrade your API plan if needed
3. Wait for rate limit to reset
4. Consider using DeepSeek API as alternative

### Problem: Tavily API Not Working

**Solution:**

1. Verify `TAVILY_API_KEY` in `.env`
2. Check if Tavily service is down
3. Set `USE_TAVILY=false` to disable (optional feature)

---

## Common Error Messages

### "Connection refused"

**Cause**: Service not running

**Solution**: Start the required service (backend, MongoDB, etc.)

### "EADDRINUSE"

**Cause**: Port already in use

**Solution**: Kill process using the port or use different port

### "Command not found"

**Cause**: Required tool not installed

**Solution**: Install missing tool (docker, python3, npm, etc.)

### "Permission denied"

**Cause**: Insufficient permissions

**Solution**:
```bash
# Make script executable
chmod +x script.sh

# Or use sudo (be careful)
sudo command
```

---

## Getting Help

If you're still experiencing issues:

1. **Check logs**:
   - Backend: `backend/logs/fakenews.log`
   - Frontend: Browser console (F12)
   - Docker: `docker compose logs`

2. **Verify all services are running**:
   ```bash
   # Check backend
   curl http://localhost:8000/health

   # Check frontend
   curl http://localhost:5173

   # Check MongoDB
   docker ps | grep mongo
   ```

3. **Review system requirements**: Ensure your system meets minimum requirements

4. **Check GitHub Issues**: Search for similar problems

5. **Create a new issue**: Include:
   - Error message
   - Steps to reproduce
   - System information (OS, Python version, Node version)
   - Relevant logs

---

## Debugging Tips

### Enable Debug Logging

Edit `backend/.env`:
```env
LOG_LEVEL=DEBUG
```

### Check Service Status

```bash
# Backend
curl http://localhost:8000/health

# Frontend
curl http://localhost:5173

# MongoDB
docker ps | grep mongo
```

### View Real-time Logs

```bash
# Backend logs
tail -f backend/logs/fakenews.log

# Docker logs
docker compose -f docker-compose.mongo.yml logs -f
```

### Test API Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Test detection endpoint
curl -X POST http://localhost:8000/api/detect/baseline \
  -H "Content-Type: application/json" \
  -d '{"text": "Test news article"}'
```

---

## Quick Fixes Checklist

- [ ] All services running (backend, frontend, MongoDB)
- [ ] API keys configured in `.env`
- [ ] No port conflicts
- [ ] All dependencies installed
- [ ] Correct Python and Node versions
- [ ] Internet connection stable
- [ ] Sufficient disk space and RAM
- [ ] Firewall not blocking ports
- [ ] `.env` file exists in correct location
- [ ] No typos in configuration

---

## Still Need Help?

Contact the development team or check the project repository for more information.
