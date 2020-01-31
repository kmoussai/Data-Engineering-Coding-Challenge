# -*- coding: utf-8 -*-
import pymongo
import functools
from scrapy.utils.project import get_project_settings
import operator


class ArticlesparserPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        # Connect to mongo db Server and create DB and an Collection
        Host = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(
            settings.get("MONGO_USER"),
            settings.get("MONGO_PASSWORD"),
            settings.get("MONGO_SERVER")
        )
        self.client = pymongo.MongoClient(Host)
        db = self.client[settings.get("MONGO_DB_NAME")]
        self.collection = db[settings.get("MONGO_DB_COLLECTION")]
        # Create some indexes field to make the search fast
        self.collection.create_index([
            ("title", pymongo.TEXT),
            ("body", pymongo.TEXT),
            ("author", pymongo.TEXT)
        ])

    def process_item(self, item, spider):
        # some we found article with name of associated press
        # so i decide to ignore them
        # and make the author array empty
        try:
            author = item["author"]
        except:
            author = []
        # insert item to the collection
        self.collection.insert_one({
            "title": item["title"],
            "author": author,
            "body": functools.reduce(operator.add, item["body"]),
            "url": item["url"]
        })
        return item

    def __del__(self):
        self.client.close()
