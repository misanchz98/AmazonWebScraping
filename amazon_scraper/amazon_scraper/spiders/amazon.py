import scrapy
from ..items import AmazonScraperItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from time import sleep

MAX_ITEMS = 10

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = ['https://www.amazon.es/']

    def __init__(self):
        serv = Service(r'driver\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv)
    
    def get_selenium_response(self, url):
        self.driver.get(url)
        sleep(5)

        #Step 1: Look for "tarjeta gráfica" in amazon's search box
        search_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys('tarjeta gráfica')
        btn_search = self.driver.find_element(By.ID, 'nav-search-submit-button')
        btn_search.click()
        sleep(2)

        # Accept cookies
        accept_cookies = self.driver.find_element(By.ID, 'sp-cc-accept')
        accept_cookies.click()
        sleep(2)

        #Step 2: Apply "50-100 EUR" filter
        price_option = self.driver.find_element(By.XPATH, '//li[@aria-label="50 - 100 EUR"]//a[@class="a-link-normal s-navigation-item"]')
        price_option.click()
        sleep(2)

        #Step 3: Apply "Valoración media de los clientes" filter
        assessment_options = self.driver.find_element(By.ID, 'a-autoid-0-announce')
        assessment_options.click()
        sleep(1)

        mean_assessment = self.driver.find_element(By.ID, 's-result-sort-select_3')
        mean_assessment.click()
        sleep(2)

        #url = self.driver.current_url
        return self.driver.page_source.encode('utf-8')
        #driver.quit()

    def parse(self, response):
        count = 0
        selenium_response = scrapy.Selector(text=self.get_selenium_response(response.url))
        all_div_items = selenium_response.xpath('//div[@data-component-type="s-search-result"]')
        
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


 