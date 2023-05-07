from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import AddComment
from spiders.settings import settings
import sys

link = sys.argv[1]
comment = sys.argv[2]
process = CrawlerProcess(settings)
process.crawl(AddComment, link=link, comment=comment)
process.start()
