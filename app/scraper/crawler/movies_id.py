from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import GetMovies
from spiders.settings import DescargasDD
from spiders.settings import settings
import sys

try:
    page = sys.argv[1]
    if page in DescargasDD.movies_pages:
        process = CrawlerProcess(settings)
        process.crawl(GetMovies, page=str(DescargasDD.movies_pages[page]))
        process.start()
    else:
        print("No existe la página")
except IndexError:
    print("No se ha introducido una página válida")
