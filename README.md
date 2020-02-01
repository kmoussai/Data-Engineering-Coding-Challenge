# Data Engineering Coding Challenge

The goal of this coding challenge is to create a solution that crawls for articles from a news website, cleanses the response, stores it in a mongo database, then makes it available to search via an API.

## Crawling
#### Setup

setup settings in `/ArticlesParser/ArticlesParser/settings.py`

```
# mongoDB data
    MONGO_USER = "<User>"
    MONGO_PASSWORD = "<Password>"
    MONGO_SERVER = "<Server>"

    MONGO_DB_NAME = "Challenge"
    MONGO_DB_COLLECTION = "Articles"
# Number of article to crawl
    ARTICLE_COUNT = 300
```
#### Run

```
cd ArticlesParser && scrapy crawl Articles && cd -
```
## API
#### Setup

Set Env variable in `ArticleSearchApi/nodemon.js`

```
{
    "env": {
        "PORT": 5000,
        "MONGO_PASSWORD": "<Password>",
        "MONGO_USER": "<User>",
        "MONGO_SERVER": "<Server>",

        "MONGO_DB_NAME": "Challenge",
        "MONGO_DB_COLLECTION": "Articles"
    }
}
```

#### Run

```
cd ArticleSearchApi && npm install && npm start
```

### Search in articles

```
    GET /search
        params :
                query : String (Required).
                _limit : Number (Optional, default 20) // Result size.
                _offset : Number (Optional, default 0) // Number of article to skip, for pagination.

```


## Module required for scraping
* [dnspython](http://www.dnspython.org/)
* [Scrapy](https://scrapy.org/)
