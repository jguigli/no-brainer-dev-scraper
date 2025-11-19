import scrapy

class GithubRepoItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    stars = scrapy.Field()
    forks = scrapy.Field()
    score = scrapy.Field()

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    published_at = scrapy.Field()
    summary = scrapy.Field()
    tags = scrapy.Field()
