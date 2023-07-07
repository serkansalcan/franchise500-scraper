from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import FranchisesItem


class FranchiseSpider(CrawlSpider):
    name = "franchise"
    allowed_domains = ["www.entrepreneur.com"]
    start_urls = ["https://www.entrepreneur.com/franchise500"]

    franchiseLinks = Rule(LinkExtractor(restrict_css=".md\:pr-6 .py-4"), callback="parse_item", follow=False)
    next_page = Rule(LinkExtractor(restrict_css=".pl-1"), follow=True)
    rules = (franchiseLinks, next_page)

    def parse_item(self, response):
        loader = ItemLoader(item=FranchisesItem(), response=response)

        loader.add_css("name", ".leading-8.mb-2::text")
        loader.add_css("description", ".font-light.hover\:underline::text")
        loader.add_css("ranking", ".text-white > span::text")
        loader.add_css("ranking_last_year", ".font-light.text-white::text")
        loader.add_css("initial_investment", ".md\:rounded-tr-none span::text")
        loader.add_css("industry", ".py-5:nth-child(1) .hover\:underline::text")
        loader.add_css("founded", ".mb-12:nth-child(4) .py-5:nth-child(3) .sm\:pl-4::text")
        loader.add_css("parent_company", ".mb-12:nth-child(4) .py-5:nth-child(4) .sm\:pl-4::text")
        loader.add_css("franchising_since", "#overview .py-5:nth-child(1) .sm\:pl-4::text")
        loader.add_css("units", "div[id='widgetChart']::attr(data-chartdata)")

        yield loader.load_item()

