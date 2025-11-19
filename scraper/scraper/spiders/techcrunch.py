import scrapy
from scrapers.items import NewsItem


class TechCrunchSpider(scrapy.Spider):
    name = "tech_news"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]

    def parse(self, response):
        articles = response.css("div.post-block")

        for article in articles:
            item = NewsItem()

            item["title"] = article.css("h2.post-block__title a::text").get(default="").strip()
            item["url"] = article.css("h2.post-block__title a::attr(href)").get()

            item["source"] = "techcrunch"

            item["summary"] = (
                article.css("div.post-block__content::text").get(default="").strip()
            )

            # date format brut
            item["published_at"] = article.css("time::attr(datetime)").get()

            item["tags"] = article.css("a.post-block__primary-tag::text").getall() or None

            yield item

        next_page = response.css("a.load-more::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
