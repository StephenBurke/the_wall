# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class LyricSpider(scrapy.Spider):
    name = "lyric"

    def start_requests(self):
        urls = ['https://www.davemcnally.com/album-lyrics/the-wall/pink-floyd/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        yield {'lyrics': response.css('div/col-md::text').getall()}

        # A way to store what's crawled maybe

        page = response.url.split("/")[-1]
        filename = f'lyric-{page}.html'

        with open(filename, 'wb') as f:
            f.write(response.css('div/col-md::text').getall())
        self.log(f'Saved file {filename}')
