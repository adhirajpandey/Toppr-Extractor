#!/bin/bash

cd /app

mkdir DATA

# Update and install basic dependencies
apt-get update && apt-get install -y \
    bash \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxi6 \
    libxtst6 \
    libfreetype6 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxss1 \
    lsb-release \
    xdg-utils \
    wget \
    python3 \
    python3-pip \
    xvfb \
    --no-install-recommends



# Install Python packages
pip3 install -r requirements.txt

echo "Requirements Installed"

nohup gunicorn --bind 0.0.0.0:5000 --log-level=debug wsgi:app >> flasknohup.out 2>&1 &

echo "Flask Application Initialized"

xvfb-run -a -s "-screen 0 1280x1024x24" celery -A tasks worker -l info

echo "Celery Worker Initialized"

echo $PWD