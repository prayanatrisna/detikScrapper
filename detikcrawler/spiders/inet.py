import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from detikcrawler import items
import timegenerator

class inet(CrawlSpider):
    name = 'inet'
    urls = timegenerator.generate_datetime(1,12,2015)
    start_urls = []
    for url in urls:
        start_urls.append('https://inet.detik.com/indeks?date='+url)

    rules = (
    	Rule(LinkExtractor(allow=r'cyberlife/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'consumer/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'tips-dan-trik/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'games-news/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'fotostop-news/'),callback="parse_item"),
    	)
    def parse_item(self, response):
    	item = items.DetikcrawlerItem()
    	item['title'] = response.xpath('//div[@class="jdl"]/h1/text()').extract()
    	str_cont = response.xpath('//*[@id="detikdetailtext"]/text()').extract()
    	str_cont = " ".join(str_cont).strip()
    	item['content'] = str_cont[2:]

    	return item