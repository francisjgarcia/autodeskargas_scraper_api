from scrapy.crawler import CrawlerProcess
from spiders.descargasdd import GetMovies
from spiders.settings import DescargasDD
from spiders.settings import settings

process = CrawlerProcess(settings)
for page in DescargasDD.movies_pages:
    process.crawl(GetMovies, page=str(DescargasDD.movies_pages[page]))
process.start()
