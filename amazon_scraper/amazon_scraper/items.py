# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() 
    assessment = scrapy.Field()
    price = scrapy.Field()
    RAM_size = scrapy.Field()
    RAM_type = scrapy.Field()
    memory_speed = scrapy.Field()
    pass
