Inspiration:
https://www.upwork.com/jobs/_~0148b2283c68400cc0/

# Start crawling form command line
scrapy crawl email_spider -a start_url='http://codingboar.com' -o scraped.json

# Start spider from script
See crawl.py

# Website for checking own IP (useful for checking whether socket works)
http://icanhazip.com

# Storage
This scraper save scraped data to a local mongodb. The database connection can be configured in settings.py:
MONGO_URI = 'localhost:27017'
MONGO_DATABASE = 'scraping'

# Proxy
A Tor socket is used for annoymity. It can be configured in middlewares.py
TOR_SOCK_URI = 'localhost:9150'