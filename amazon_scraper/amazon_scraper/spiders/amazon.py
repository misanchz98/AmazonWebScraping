import scrapy
from ..items import AmazonScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/s?k=tarjeta+grafica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&ds=v1%3AWaGq4VgCol11wI5HIWNRm%2Fi%2BSqyf0tUcxLYF57b%2F%2FkA&qid=1663515144&rnid=1323854031&ref=sr_st_review-rank']

    def parse(self, response):
        items = AmazonScraperItem()

        title = item.css('.a-size-medium').css('::text').extract(),
        assessment = item.css('.aok-align-bottom').css('::text').extract(),
        price = item.css('.a-price-whole').css('::text').extract(),
        RAM_size = item.css('.puis-padding-right-small:nth-child(1) .a-text-bold').css('::text').extract(),
        RAM_type = item.css('.puis-padding-right-small:nth-child(2) .a-text-bold').css('::text').extract(),
        graphic_card = item.css('.puis-padding-right-small:nth-child(3) .a-text-bold').css('::text').extract(),
        memory_speed = item.css('.puis-padding-right-small:nth-child(4) .a-text-bold').css('::text').extract()
        
        items['title'] = title
        items['assessment'] = assessment
        items['price'] = price
        items['RAM_size'] = RAM_size
        items['RAM_type'] = RAM_type
        items['graphic_card'] = graphic_card
        items['memory_speed'] = memory_speed

        yield items


 