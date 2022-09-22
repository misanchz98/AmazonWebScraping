import scrapy
from ..items import AmazonScraperItem

MAX_ITEMS = 10

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/']
    
    def start_response(self):

    
    def parse(self, response):
        count = 0
        all_div_items = response.xpath('//div[@data-component-type="s-search-result"]')
        
        for i in all_div_items:
            
            if count == MAX_ITEMS:
                break
            else:
                count += 1
                item = AmazonScraperItem(
                    title = i.css('.a-size-medium').css('::text').extract(),
                    assessment = i.css('.aok-align-bottom').css('::text').extract(),
                    price = i.css('.a-price-whole').css('::text').extract(),
                    RAM_size = i.css('.puis-padding-right-small:nth-child(1) .a-text-bold').css('::text').extract(),
                    RAM_type = i.css('.puis-padding-right-small:nth-child(2) .a-text-bold').css('::text').extract(),
                    graphic_card = i.css('.puis-padding-right-small:nth-child(3) .a-text-bold').css('::text').extract(),
                    memory_speed = i.css('.puis-padding-right-small:nth-child(4) .a-text-bold').css('::text').extract()
                )
                yield item


 