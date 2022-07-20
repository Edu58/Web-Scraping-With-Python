import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        """_summary_
            use of start_requests()
        Returns:
            response(list): _description_

            start_requests is a Scrapy-defined entry point to the program used to generate Request objects that Scrapy uses to crawl the website.
        """
        urls = [
            "https://en.wikipedia.org/wiki/Programming_paradigm",
            "https://en.wikipedia.org/wiki/Functional_programming",
            "https://en.wikipedia.org/wiki/Monty_Python",
        ]
        
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        """_summary_
            use of parse()
        Args:
            response (None): _description_
            parse is a callback function defined by the user, and is passed to the Request object with callback=self.parse.
        """
        url = response.url
        title = response.css('h1::text').extract_first()
        print(f'URL is: {url}')
        print(f'Title is: {title}')
