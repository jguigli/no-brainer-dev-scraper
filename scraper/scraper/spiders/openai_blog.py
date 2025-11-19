import scrapy
from scrapers.items import NewsItem


class OpenAIBlogSpider(scrapy.Spider):
    name = "ai_news"
    allowed_domains = ["openai.com"]
    start_urls = ["https://openai.com/blog"]

    def parse(self, response):
        articles = response.css("li.PostItem, div.PostItem")

        for article in articles:
            item = NewsItem()

            item["title"] = article.css("h2.PostItem-title a::text, h3.PostItem-title a::text").get(default="").strip()
            item["url"] = response.urljoin(article.css("h2.PostItem-title a::attr(href), h3.PostItem-title a::attr(href)").get())
            item["source"] = "openai-blog"
            item["summary"] = article.css("p.PostItem-lead::text, p.PostItem-excerpt::text").get(default="").strip()
            item["published_at"] = article.css("time::attr(datetime)").get()
            item["tags"] = article.css("a.PostItem-tag::text").getall() or None

            yield item

        next_page = response.css("a.load-more::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
