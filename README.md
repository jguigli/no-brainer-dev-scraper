# no-brainer-dev-scraper

Scraper using scrapy and playwright to collect informations about Tech.

Scraped site :

- Github Trending repos
- TechCrunch
- OpenAI Blog

The data is stored in a MongoDB database with separated collections for each spider.

## Requirements

docker  
docker-compose  
make  

## Usage

```
git clone https://github.com/jguigli/no-brainer-dev-scraper.git
cd no-brainer-dev-scraper
make
```