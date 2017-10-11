import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from detikcrawler import items
import timegenerator

class travel(CrawlSpider):
    name = 'travel'
    urls = timegenerator.generate_datetime(1,12,2015) #<-- ganti ini untuk ganti tanggal
    start_urls = []
    for url in urls:
        start_urls.append('https://travel.detik.com/indeks?date='+url)

    rules = (
    	Rule(LinkExtractor(allow=r'domestic-destination/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'international-destination/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'travel-tips/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'travel-news/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'advertorial-news-block-travel/'),callback="parse_item"),
        Rule(LinkExtractor(allow=r'dtravelers_stories/'),callback="parse_item2")
    	)
    def parse_item(self, response):
    	item = items.DetikcrawlerItem()
    	item['title'] = response.xpath('//*[@class="mt5"]/text()').extract()
    	str_cont = response.xpath('//*[@id="detikdetailtext"]/text()').extract()
    	str_cont = " ".join(str_cont).strip()
    	item['content'] = str_cont[2:]

    	return item

    def parse_item2(self, response):
        item = items.DetikcrawlerItem()
        item['title'] = response.xpath('//h2[@class="mt5"]/text()').extract()
        str_cont = response.xpath('//*[@class="read__content full mt20"]/text()').extract()
        str_cont = " ".join(str_cont).strip()
        item['content'] = str_cont[2:]
        
        return item