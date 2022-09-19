import scrapy
from ..items import AmazonScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/s?k=tarjeta+grafica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&ds=v1%3AWaGq4VgCol11wI5HIWNRm%2Fi%2BSqyf0tUcxLYF57b%2F%2FkA&qid=1663515144&rnid=1323854031&ref=sr_st_review-rank']

    def parse(self, response):

        all_div_products = response.xpath('//div[@class="s-main-slot s-result-list s-search-results sg-row"]')
        
        for i in all_div_products:

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


 