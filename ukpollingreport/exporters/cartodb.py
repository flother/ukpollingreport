import csv
from urlparse import urlparse

import requests
from scrapy.extensions.feedexport import BlockingFeedStorage


class CartoDBFeedStorage(BlockingFeedStorage):

    def __init__(self, uri):
        self.uri = uri
        u = urlparse(uri)
        self.account = u.username
        self.api_key = u.password
        self.table_name = u.hostname

    def open(self, spider):
        # FIXME: Hijacking this so we can access settings properly, see
        # https://github.com/scrapy/scrapy/issues/1567.
        self.settings = spider.settings
        return super(CartoDBFeedStorage, self).open(spider)

    def _store_in_thread(self, file):
        url = "https://{}.cartodb.com/api/v2/sql".format(self.account)

        seq_sql = "SELECT pg_catalog.pg_get_serial_sequence('{}', 'cartodb_id')"
        response = requests.post(url,
                                 data=dict(q=seq_sql.format(self.table_name)))
        cartodb_id_seq = response.json()["rows"][0]["pg_get_serial_sequence"]
        sql = ["BEGIN"]
        from scrapy.conf import settings
        if self.settings["CARTODB_TRUNCATE"] is True:
            sql.append("TRUNCATE {}".format(self.table_name))
        if self.settings["CARTODB_RESET_IDS"] is True:
            sql.append("ALTER SEQUENCE {} RESTART WITH 1".format(cartodb_id_seq))
        file.seek(0)
        rows = csv.reader(file)
        headers = rows.next()
        sql.append("INSERT INTO {} ({}) VALUES {}".format(
            self.table_name,
            ", ".join(headers),
            ", ".join(
                "({})".format(", ".join(("'{}'".format(r) for r in row)))
                for row in rows
            )
        ))
        sql.append("COMMIT")
        requests.post(url, data=dict(q="; ".join(sql), api_key=self.api_key))
