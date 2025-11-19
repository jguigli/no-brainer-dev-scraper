FROM python:3.12

RUN apt-get update && apt-get install -y \
    cron \
    curl \
    gnupg \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install

COPY scraper/ ./scraper
COPY start.sh .

RUN chmod +x start.sh

CMD ["./start.sh"]