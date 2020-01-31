import scrapy

from ArticlesParser.items import articleItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.utils.project import get_project_settings


class ArticleSpider(scrapy.Spider):
    name = "Articles"
    start_urls = [
        # During my search i found this page where there is all articles for a specific day.
        "https://www.theguardian.com/world/2020/jan/01/all"
    ]

    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': get_project_settings().get("ARTICLE_COUNT")
    }

    def parse(self, response):

        for article in response.xpath("//div[@class='fc-item__container']"):
            # get all link of articles in page and parse them one by one
            url = article.xpath(".//a//@href").extract_first()
            # i make the parse just for articles so i ingored the video pages
            checkVideoGallery = "/video" not in url and "/gallery" not in url
            if url is not None and checkVideoGallery:
                yield Request(url, callback=self.parseArticle)
        # Next page or older article
        # there is a link in the bottom of the start page that lead to older articles
        next_page = response.xpath("//a[@rel='prev']/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield Request(next_page_link, callback=self.parse, )

    # this functin for parse article page and extract relevant information of the article
    def parseArticle(self, response):
        l = ItemLoader(item=articleItem(), response=response)
        l.add_xpath("title", "//h1[@itemprop='headline']//text()")
        l.add_xpath("author", "//span[@itemprop='name']//text()")
        l.add_xpath("body", "//div[@itemprop='articleBody']/p//text()")
        l.add_value("url", response.url)
        yield l.load_item()
