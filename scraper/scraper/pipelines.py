import pymongo

class MongoPipeline:
    def __init__(self):
        self.client = None
        self.db = None

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(spider.settings.get('MONGO_URI'))
        self.db = self.client[spider.settings.get('MONGO_DB')]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == "github_trending":
            stars = item.get('stars', 0)
            forks = item.get('forks', 0)
            item['score'] = stars + forks * 0.5

        collection = self.db[spider.name]
        collection.update_one(
            {'url': item['url']},
            {'$set': dict(item)},
            upsert=True
        )
        return item
