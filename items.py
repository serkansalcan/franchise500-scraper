import scrapy
from itemloaders.processors import TakeFirst, MapCompose


class FranchisesItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    ranking = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    ranking_last_year = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    initial_investment = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    industry = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    founded = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    parent_company = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    franchising_since = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    units = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())

