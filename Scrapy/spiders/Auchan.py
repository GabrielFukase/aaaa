import scrapy
from ..items import ScrapyItem
import string

class AuchanSpider(scrapy.Spider):
    name = 'Auchan'
    start_urls = ['https://www.auchan.pt/Frontoffice/produtos_frescos/fruta']

    def parse(self, response):
        items = ScrapyItem()
        product_name = response.css('#divDataList h3::text').extract()
        product_price = response.css('.product-item-price-column').css('::text').extract()
        product_imglink = response.css('#divDataList .hidden-print').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imglink'] = product_imglink

        yield items
