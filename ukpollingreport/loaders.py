import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


def strip_whitespace(v):
    return v.strip()


def make_number(v):
    if v is not None:
        try:
            v = int(v)
        except ValueError:
            v = float(v)
    return v


def make_date(v):
    return datetime.date(*(int(i) for i in v.strip("*").split("-")))


class PollLoader(ItemLoader):

    default_output_processor = TakeFirst()
    pollster_in = MapCompose(strip_whitespace)
    client_in = MapCompose(strip_whitespace)
    date_in = MapCompose(strip_whitespace, make_date)
    party_in = MapCompose(strip_whitespace)
    share_in = MapCompose(make_number)
