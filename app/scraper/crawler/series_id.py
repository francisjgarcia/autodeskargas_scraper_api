from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import GetSeries
from spiders.settings import DescargasDD
from spiders.settings import settings
import sys

try:
    page = sys.argv[1]
    print("JEJEJEJEJEJE")
    if page in DescargasDD.series_pages:
        process = CrawlerProcess(settings)
        process.crawl(GetSeries, page=str(DescargasDD.series_pages[page]))
        process.start()
    else:
        print("No existe la página")
except IndexError:
    print("No se ha introducido una página válida")
