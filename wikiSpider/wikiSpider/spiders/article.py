import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        urls = [
            "https://en.wikipedia.org/wiki/Programming_paradigm",
            "https://en.wikipedia.org/wiki/Functional_programming",
            "https://en.wikipedia.org/wiki/Monty_Python",
        ]
        
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print(f'URL is: {url}')
        print(f'Title is: {title}')
