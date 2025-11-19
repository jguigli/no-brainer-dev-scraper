import scrapy
from github_trending_scraper.items import GithubRepoItem
from scrapy_playwright.page import PageCoroutine

class GithubTrendingSpider(scrapy.Spider):
    name = "github_trending"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/trending"]

    custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_page_coroutines=[
                        PageCoroutine("wait_for_selector", "article.Box-row")
                    ]
                )
            )

    def parse(self, response):
        for repo in response.css("article.Box-row"):
            item = GithubRepoItem()
            full_name = repo.css("h2 a::attr(href)").get().strip("/")
            author, name = full_name.split("/")
            item['author'] = author.strip()
            item['name'] = name.strip()
            item['url'] = response.urljoin(repo.css("h2 a::attr(href)").get())
            item['description'] = repo.css("p::text").get(default="").strip()
            item['language'] = repo.css("[itemprop=programmingLanguage]::text").get(default="").strip()
            
            stars_text = repo.css("a.Link--muted[href$='/stargazers']::text").get()
            item['stars'] = int(stars_text.strip().replace(',', '')) if stars_text else 0

            forks_text = repo.css("a.Link--muted[href$='/network/members']::text").get()
            item['forks'] = int(forks_text.strip().replace(',', '')) if forks_text else 0

            yield item
