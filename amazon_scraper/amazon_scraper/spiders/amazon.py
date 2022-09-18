import scrapy
from ..items import AmazonScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/s?k=tarjeta+gráfica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&ds=v1%3AWaGq4VgCol11wI5HIWNRm%2Fi%2BSqyf0tUcxLYF57b%2F%2FkA&qid=1663515144&rnid=1323854031&ref=sr_st_review-rank']

    def parse(self, response):
        items = AmazonScraperItem()
        pass
