import scrapy

from ukpollingreport.items import PollItem
from ukpollingreport.loaders import PollLoader


class PollsSpider(scrapy.Spider):

    name = "polls"
    allowed_domains = ["ukpollingreport.co.uk"]
    start_urls = (
        "http://ukpollingreport.co.uk/voting-intention-2",
        "http://ukpollingreport.co.uk/voting-intention-2005-2010",
        "http://ukpollingreport.co.uk/historical-polls/voting-intention-2001-2005",
        "http://ukpollingreport.co.uk/historical-polls/voting-intention-1997-2001",
        "http://ukpollingreport.co.uk/historical-polls/voting-intention-1992-1997",
        "http://ukpollingreport.co.uk/historical-polls/voting-intention-1987-1992",
        "http://ukpollingreport.co.uk/voting-intention-1983-1987",
        "http://ukpollingreport.co.uk/voting-intention-1979-1983",
        "http://ukpollingreport.co.uk/voting-intention-1974-1979",
        "http://ukpollingreport.co.uk/vote-intention-1970-oct1974",
    )

    def parse(self, response):
        parties = response.xpath("//div[@class='polltable']/table/tr[1]"
                                 "/td[position()>2][position() < last()]"
                                 "//text()").re("(.+) \(%\)")
        for row in response.xpath("//div[@class='polltable']/table/tr[position()>2]"):
            try:
                pollster, client = row.xpath("td[1]//text()").extract_first().split("/", 1)
            except ValueError:
                pollster = row.xpath("td[1]//text()").extract_first()
                client = ""
            date = row.xpath("td[2]/text()").extract_first()
            shares = row.xpath("td[position() > 2][position() < last()]//text()").extract()
            for party, share in zip(parties, shares):
                l = PollLoader(PollItem(), row)
                l.add_value("pollster", pollster)
                l.add_value("client", client)
                l.add_value("date", date)
                l.add_value("party", party)
                l.add_value("share", share)
                yield l.load_item()
