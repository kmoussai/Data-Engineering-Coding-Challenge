
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

# To remove white spaces from the title


def whiteSpaceClear(value):
    return value.strip()


# To Add new Line to paragraph if we found "."
def addBackLine(value):
    if value[-1] == '.':
        value = value + '\n'
    return value


class articleItem(scrapy.Item):
    # Field for article title
    title = scrapy.Field(
        output_processor=TakeFirst(),
        input_processor=MapCompose(whiteSpaceClear))
    # Field for article author
    author = scrapy.Field(
        input_processor=MapCompose(whiteSpaceClear))
    # Field for article body
    # stored like an array of paragraph
    body = scrapy.Field(
        input_processor=MapCompose(addBackLine)
    )
    # Field for article original url
    url = scrapy.Field(
        output_processor=TakeFirst())
