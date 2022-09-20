import scrapy
from ..items import AmazonScraperItem

MAX_ITEMS = 10

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/s?k=tarjeta+gráfica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&ds=v1%3AkYmNY2E2LnzJBtBJnAnx69lXM8c52NL64KoWbgBCeUY&qid=1663691117&rnid=1323854031&ref=sr_st_review-rank']
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


 