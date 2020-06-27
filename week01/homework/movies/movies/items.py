# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()
    actor = scrapy.Field()
    release_time = scrapy.Field()
    content = scrapy.Field()
