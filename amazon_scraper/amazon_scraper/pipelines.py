# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class AmazonScraperPipeline:
    def process_item(self, item, spider):
        data_list = ['title', 'assessment', 'price', 'RAM_size', 'RAM_type', 'graphic_card', 'memory_speed']
        
        # Process empty values
        for data in data_list:
            if not item[data]:
                item[data] = ['-']

        return item
