import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 

serv = Service(r'C:\\Users\\INTEL I5\\Desktop\\AmazonWebScraping\\amazon_scraper\\driver\\chromedriver.exe')
driver = webdriver.Chrome(service=serv)

driver.get('https://www.amazon.es/')

#Step 1: Look for "tarjeta gráfica" in amazon's search box
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('tarjeta gráfica')
btn_search = driver.find_element(By.ID, 'nav-search-submit-button')
btn_search.click()
sleep(2)

# Accept cookies
accept_cookies = driver.find_element(By.ID, 'sp-cc-accept')
accept_cookies.click()
sleep(2)

#Step 2: Apply "50-100 EUR" filter
price_option = driver.find_element(By.XPATH, '//li[@aria-label="50 - 100 EUR"]//a[@class="a-link-normal s-navigation-item"]')
price_option.click()
sleep(2)

#Step 3: Apply "Valoración media de los clientes" filter
assessment_options = driver.find_element(By.ID, 'a-autoid-0-announce')
assessment_options.click()
sleep(1)

mean_assessment = driver.find_element(By.ID, 's-result-sort-select_3')
mean_assessment.click()
sleep(2)

url = driver.current_url
print(url)

driver.quit()