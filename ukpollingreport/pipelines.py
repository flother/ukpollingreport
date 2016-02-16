from scrapy.exceptions import DropItem


class PollPipeline(object):

    PARTY_ABBREVIATIONS = {
        "CON": "Conservative",
        "LAB": "Labour",
        "LD": "Liberal Democrats",
        "LDEM": "Liberal Democrats",
        "All/LD": "Liberal Democrats",
        "C.SDP": "SDP",
        "LIB/SDP": "SDP-Liberal Alliance",
        "LIB": "Liberal",
        "UKIP": "UKIP",
        "Grn": "Green",
    }
    POLLSTER_CORRECTIONS = {
        "CommRes": u"ComRes",
    }
    CLIENT_CORRECTIONS = {
        "DailyMail": u"Daily Mail",
        "FT": u"Financial Times",
        "Ind on Sun": u"Independent on Sunday",
        "Ind on Sun/S. Mirror": u"Independent on Sunday/Sunday Mirror",
        "Independent (O)": "Independent",
        "Independent on Sunday (O)": "Independent on Sunday",
        "Independent on Sunday/S. Mirror": "Independent on Sunday/Sunday Mirror",
        "ITV/Mail": "ITV/Daily Mail",
        "Mail": "Daily Mail",
        "n/a": "",
        "null": "",
        "Observor": u"Observer",
        "Political Betting": u"PoliticalBetting.com",
        "PoliticalBetting": u"PoliticalBetting.com",
        "S. Mirror": u"Sunday Mirror",
        "SkyNews": u"Sky News",
        "Sumday Telegraph": u"Sunday Telegraph",
        "the Sun": u"Sun",
        "The Sun": u"Sun",
        "Today on S": u"Today on Sunday",
    }

    def process_item(self, item, spider):
        if item["pollster"] == "GENERAL ELECTION":
            raise DropItem("dropping general election result")
        if not item["party"]:
            raise DropItem("missing party in {}".format(item))
        item["pollster"] = self.POLLSTER_CORRECTIONS.get(item["pollster"],
                                                         item["pollster"])
        try:
            item["client"] = self.CLIENT_CORRECTIONS.get(item["client"],
                                                        item["client"])
        except KeyError:
            pass  # Pollster had no client.
        item["party"] = self.PARTY_ABBREVIATIONS.get(item["party"],
                                                     item["party"])
        return item
