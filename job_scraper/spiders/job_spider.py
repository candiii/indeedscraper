import scrapy
from scrapy_splash import SplashRequest
import json

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    start_urls = ['https://www.indeed.com/jobs?q=software']

    def start_requests(self):
        api_key = 'YOUR  API KEY HERE'
        target_url = 'https://www.indeed.com/jobs?q=software'
        scraper_api_url = f'http://api.scraperapi.com/?api_key={api_key}&url={target_url}'

        # Adjust range to scrape more pages, e.g., range(0, 100, 10) for 10 pages
        for start in range(0, 50, 10):
            page_url = f'{scraper_api_url}&start={start}'
            yield SplashRequest(url=page_url, callback=self.parse, args={'wait': 2})

    def parse(self, response):
        job_data_list = []

        for job_anchor in response.css('.jcs-JobTitle'):
            job_title = job_anchor.css('span::text').get()
            job_link_absolute = job_anchor.css('a::attr(href)').get()

            if job_title and job_link_absolute:
                if not job_link_absolute.startswith('https://www.indeed.com'):
                    job_link_absolute = f'https://www.indeed.com{job_link_absolute}'

                company = job_anchor.css('.company::text').get()
                salary = job_anchor.css('.salaryText::text').get()

                job_data = {
                    'job_title': job_title.strip() if job_title else None,
                    'company': company.strip() if company else None,
                    'salary': salary.strip() if salary else None,
                    'job_link': job_link_absolute,
                    'url': job_link_absolute  # Adding a 'url' field with the same link as 'job_link'
                }

                job_data_list.append(job_data)

        with open('job_data.json', 'a', encoding='utf-8') as json_file:
            json_file.write(json.dumps(job_data_list, indent=2))

        self.log(f'Job data have been stored in job_data.json')
