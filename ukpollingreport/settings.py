BOT_NAME = "ukpollingreport"
SPIDER_MODULES = ["ukpollingreport.spiders"]
NEWSPIDER_MODULE = "ukpollingreport.spiders"
ITEM_PIPELINES = {
    "ukpollingreport.pipelines.PollPipeline": 300,
}

FEED_FORMAT = "csv"
FEED_EXPORT_FIELDS = ["date", "pollster", "client", "party", "share"]

FEED_STORAGES = {"cartodb": "ukpollingreport.exporters.cartodb.CartoDBFeedStorage"}
FEED_URI = "cartodb://username:api_key@table_name"
CARTODB_TRUNCATE = True
CARTODB_RESET_IDS = True

# Fix for https://github.com/scrapy/scrapy/issues/1344.
DOWNLOAD_HANDLERS = {"s3": None}
