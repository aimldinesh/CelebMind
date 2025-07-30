# 🐍 Base image
FROM python:3.10-slim

# 🔧 Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 📁 Working directory
WORKDIR /app

# 🧰 Install system dependencies (for OpenCV and general needs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Run setup.py (for editable install if using setup.py)
RUN pip install --no-cache-dir -e .

# 📁 Copy entire project into container
COPY . .

# 🌐 Expose Flask default port
EXPOSE 5000

# 🚀 Run the Flask application
CMD ["python", "app.py"]
