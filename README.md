dependencies:

`pip install scrapy`
`pip install scrapy-splash`


This project scrapes indeed.com for jobs using Scrapy.


Usage :


open the job_spider.py file inside the spiders folder using any Editor .e.g Visual Studio Code.


Put in your API key you can get free ones from ScraperApi, ScrapingBee etc.


Change the url in the code if you want to scrape for other jobs the project scrapes software jobs.


Once you have updated the code run the following command in the same directory :


`scrapy runspider job_spider.py`


It will save the scraped jobs in inside the json file in the spiders directory.
