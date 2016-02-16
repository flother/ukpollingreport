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


class PollLoader(ItemLoader):

    default_output_processor = TakeFirst()
    pollster_in = MapCompose(strip_whitespace)
    client_in = MapCompose(strip_whitespace)
    date_in = MapCompose(strip_whitespace)
    party_in = MapCompose(strip_whitespace)
    share_in = MapCompose(make_number)
