# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonScraperPipeline:
    def process_item(self, item, spider):
        print("Title: ", item['title'])
        print("Assessment: ", item['assessment'])
        print("Price: ", item['price'])
        print("RAM Size: ", item['RAM_size'])
        print("RAM Type: ", item['RAM_type'])
        print("Graphic Card: ", item['graphic_card'])
        print("Memory Speed: ", item['memory_speed'])
        return item
