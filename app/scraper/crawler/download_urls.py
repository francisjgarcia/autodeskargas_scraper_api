from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import GetDownloadURLs
from spiders.settings import settings
import sys

link = sys.argv[1]
process = CrawlerProcess(settings)
process.crawl(GetDownloadURLs, link=link)
process.start()
