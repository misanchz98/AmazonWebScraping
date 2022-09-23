cd amazon_scraper
DEL items.csv
scrapy crawl amazon -o items.csv -t csv
cd ..