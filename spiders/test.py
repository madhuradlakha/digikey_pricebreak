import scrapy

from digikey_pricebreak.items import DigiKeyPriceBreakItem
from scrapy.selector import HtmlXPathSelector

class PriceBreakSpider(scrapy.Spider):
	name = "pricebreak"
	allowed_domains = ["digikey.com"]
	start_urls = ["http://www.digikey.com/product-search/en/integrated-circuits-ics/embedded-microcontrollers/2556109"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//td[@class='digikey-partnumber']/a")
		for href in titles:
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		hxs = HtmlXPathSelector(response)
        titles = hxs.select("//td[@class='catalog-pricing']")
		items = []
		for titles in titles:
			item = DigiKeyPriceBreakItem()
			item["Price_Break"] = titles.select("")


