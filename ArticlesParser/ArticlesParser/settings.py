
BOT_NAME = 'ArticlesParser'

SPIDER_MODULES = ['ArticlesParser.spiders']
NEWSPIDER_MODULE = 'ArticlesParser.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'ArticlesParser.pipelines.ArticlesparserPipeline': 300,
}

# mongoDB data
MONGO_USER = "kmoussai"
MONGO_PASSWORD = "H3pthJCVOMPSgD5I"
MONGO_SERVER = "cluster0-io2fq.mongodb.net"
MONGO_DB_NAME = "Challenge"
MONGO_DB_COLLECTION = "Articles"

# this value is to make sure that the script stop
# properly cause there is a lot of historiq there.
ARTICLE_COUNT = 300
