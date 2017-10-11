import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from detikcrawler import items
import timegenerator

class finance(CrawlSpider):
    name = 'finance'
    urls = timegenerator.generate_datetime(1,12,2016)
    start_urls = []
    for url in urls:
        start_urls.append('https://finance.detik.com/indeks?date='+url)

    rules = (
    	Rule(LinkExtractor(allow=r'energi/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'berita-ekonomi-bisnis/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'bursa-dan-valas/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'properti/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'industri/'),callback="parse_item"),
    	)
    def parse_item(self, response):
    	item = items.DetikcrawlerItem()
    	item['title'] = response.xpath('//div[@class="jdl"]/h1/text()').extract()
    	str_cont = response.xpath('//*[@id="detikdetailtext"]/text()').extract()
    	str_cont = " ".join(str_cont).strip()
    	item['content'] = str_cont[2:]

    	return item