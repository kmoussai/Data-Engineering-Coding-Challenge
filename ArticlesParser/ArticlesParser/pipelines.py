# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import functools


class ArticlesparserPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://kmoussai:H3pthJCVOMPSgD5I@cluster0-io2fq.mongodb.net/Challenge?retryWrites=true&w=majority")
        self.db = self.client.Challenge

    def process_item(self, item, spider):
        # client = pymongo.MongoClient(
        #     "mongodb+srv://kmoussai:H3pthJCVOMPSgD5I@cluster0-io2fq.mongodb.net/Challenge?retryWrites=true&w=majority")
        # db = client.Challenge
        self.db.Articles.insert_one({
            "title": item["title"],
            "author": item["author"],
            "body": functools.reduce(lambda a, b: a + b, item["body"]),
            "url": item["url"]
        })
        return item

    def __del__(self):
        self.client.close()
