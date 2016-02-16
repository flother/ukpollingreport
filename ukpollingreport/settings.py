BOT_NAME = "ukpollingreport"
SPIDER_MODULES = ["ukpollingreport.spiders"]
NEWSPIDER_MODULE = "ukpollingreport.spiders"
ITEM_PIPELINES = {
    "ukpollingreport.pipelines.PollPipeline": 300,
}
# Order for the fields in the CSV feed export.
FEED_EXPORT_FIELDS = ["date", "pollster", "client", "party", "share"]
# Fix for https://github.com/scrapy/scrapy/issues/1344.
DOWNLOAD_HANDLERS = {"s3": None}
