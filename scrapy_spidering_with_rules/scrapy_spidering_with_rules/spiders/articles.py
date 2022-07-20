from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'
    ]
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]


    def parse_items(self, response):
        """_summary_

        Args:
            response (None): _description_
            THis crawler extracts the title and URL on each page. The text content of each page is extracted using an XPath selector. XPath
            is often used when retrieving text content including text in child tags (for example, an
            <a> tag inside a block of text). If you use the CSS selector to do this, all text within
            child tags will be ignored.
        """
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath("//div[@id='mw-content-text']//text()").extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on','')

        print(f'URL: {url}')
        print(f'Title: {title}')
        print(f'Text is: {text}')
        print(f'Last updated: {lastUpdated}')