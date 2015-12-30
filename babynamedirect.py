from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector


class MySpider(CrawlSpider):
    name = "babynamedirect"
    allowed_domains = ["babynamesdirect.com"]
    start_urls = [
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/A",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/B",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/C",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/D",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/E",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/F",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/G",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/H",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/I",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/J",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/K",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/L",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/M",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/N",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/O",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/P",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/Q",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/R",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/S",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/T",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/U",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/V",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/W",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/X",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/Y",
	"http://www.babynamesdirect.com/hindu-baby-names/Boy/Z",
	
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/A",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/B",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/C",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/D",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/E",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/F",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/G",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/H",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/I",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/J",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/K",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/L",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/M",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/N",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/O",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/P",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/Q",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/R",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/S",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/T",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/U",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/V",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/W",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/X",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/Y",
	"http://www.babynamesdirect.com/sanskrit-baby-names/Boy/Z"
	]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[@class="nb"]')), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
	for n in hxs.xpath('//td/b/text()').extract():
                item = {}
                item['title'] = n
		items.append(item)
	return(items)
