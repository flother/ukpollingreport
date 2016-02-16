import scrapy


class PollItem(scrapy.Item):

    date = scrapy.Field()
    pollster = scrapy.Field()
    client = scrapy.Field()
    party = scrapy.Field()
    share = scrapy.Field()
