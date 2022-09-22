import scrapy
from ..items import AmazonScraperItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 

MAX_ITEMS = 10

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    #allowed_domains = ['amazon.es']
    #start_urls = ['https://www.amazon.es/']

    def start_request(self):
        serv = Service(r'C:\\Users\\INTEL I5\\Desktop\\AmazonWebScraping\\amazon_scraper\\driver\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv)

        driver.get('https://www.amazon.es/')

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys('tarjeta gráfica')
        btn_search = driver.find_element(By.ID, 'nav-search-submit-button')
        btn_search.click()

        url = driver.current_url
        print(url)

        yield scrapy.Request(url,callback=self.parse)

        driver.quit()

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


 