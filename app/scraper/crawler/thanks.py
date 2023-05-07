from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import ThanksButton
from spiders.settings import settings
import sys

link = sys.argv[1]
process = CrawlerProcess(settings)
process.crawl(ThanksButton, link=link)
process.start()
