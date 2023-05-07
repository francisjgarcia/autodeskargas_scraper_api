from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import GetSeries
from spiders.settings import DescargasDD
from spiders.settings import settings

process = CrawlerProcess(settings)
print("JAJAJAJA")
for page in DescargasDD.series_pages:
    process.crawl(GetSeries, page=str(DescargasDD.series_pages[page]))
process.start()
