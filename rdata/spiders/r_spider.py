import scrapy

class Rspider(scrapy.Spider):
	name = "realestate"
	allowed_domains = ["realtor.com"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		for sel in response.xpath('//ul/li'):
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract
			desc = sel.xpath('text()').extract
			print title, link, desc
