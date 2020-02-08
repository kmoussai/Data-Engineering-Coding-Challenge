
BOT_NAME = 'ArticlesParser'

SPIDER_MODULES = ['ArticlesParser.spiders']
NEWSPIDER_MODULE = 'ArticlesParser.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'ArticlesParser.pipelines.ArticlesparserPipeline': 300,
}

# mongoDB data
MONGO_USER = "<User>"
MONGO_PASSWORD = "<Password>"
MONGO_SERVER = "<Server>"
MONGO_DB_NAME = "Challenge"
MONGO_DB_COLLECTION = "Articles"

# Number of article to crawl
ARTICLE_COUNT = 300
