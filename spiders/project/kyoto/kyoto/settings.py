# Scrapy settings for kyoto project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (Windows; U; Windows NT 6.1;en-US; rv:2.0.0) Gecko/20110320 Firefox/4.0.0'
BOT_VERSION = ''

SPIDER_MODULES = ['kyoto.spiders']
NEWSPIDER_MODULE = 'kyoto.spiders'
DEFAULT_ITEM_CLASS = 'kyoto.items.KyotoItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
	'kyoto.pipelines.MySQLStorePipeline'
]
DEFAULT_RESPONSE_ENCODING = 'utf-8'
EXPORT_ENCODING = 'utf-8'

