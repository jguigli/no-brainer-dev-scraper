#!/bin/bash

echo "0 0 * * * cd /scrapers/scrapers && scrapy crawl github_trending >> /var/log/scrapy.log 2>&1" > /etc/cron.d/scrapy-cron
echo "0 0 * * * cd /scrapers/scrapers && scrapy crawl techcrunch >> /var/log/scrapy.log 2>&1" >> /etc/cron.d/scrapy-cron
echo "0 0 * * * cd /scrapers/scrapers && scrapy crawl openai_blog >> /var/log/scrapy.log 2>&1" >> /etc/cron.d/scrapy-cron

chmod 0644 /etc/cron.d/scrapy-cron

crontab /etc/cron.d/scrapy-cron

cron -f
