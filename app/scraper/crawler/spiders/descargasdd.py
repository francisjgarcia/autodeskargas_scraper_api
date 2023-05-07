from scrapy.http import Request, FormRequest
from .settings import DescargasDD
from urllib.parse import urlencode
import hashlib
import scrapy
import json
import re

class GetMovies(scrapy.Spider):
    name = "Scraping DescargasDD site for new movies."
    start_urls = [DescargasDD.base_url + "/login.php"]
    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'do': 'login',
                                            'vb_login_md5password': hashlib.md5(DescargasDD.web_password.encode()).hexdigest(),
                                            'vb_login_md5password_utf': hashlib.md5(DescargasDD.web_password.encode("utf-8")).hexdigest(),
                                            's': '',
                                            'securitytoken': 'guest',
                                            'url': DescargasDD.base_url,
                                            'vb_login_username': DescargasDD.web_user,
                                            'vb_login_password': '',
                                            },
                                        callback=self.scraping_pages)

    def scraping_pages(self, response):
        yield Request(
            url = DescargasDD.base_url + '/forumdisplay.php?f=' + getattr(self, 'page', '#'),
            callback=self.get_movies)

    def get_movies(self, response):
        movies = []
        movie = response.css('ol.threads > li.threadbit.hot'+ DescargasDD.scrapy_always)
        if movie:
            for item in movie:
                register = item.css('div.inner > h3.threadtitle > a.title::text').get()
                if re.search("1080p|2160p", register):
                    if re.search("1080p", register):
                        quality = 3 # FullHD
                    elif re.search("2160p", register):
                        quality = 4 # 4K
                    else:
                        quality = None
                    title = re.sub("[|]", "", re.split('[|([][ ]{0,1}([0-9]{4})[ ]{0,1}', item.css('div.inner > h3.threadtitle > a.title::text').get())[0].replace("4K","").replace("UHD","")).rstrip()
                    poster = item.css('div.inner > h3.threadtitle > a[rel="nofollow"] > img::attr(src)').get()
                    year = int(re.split('[|([][ ]{0,1}([0-9]{4})[ ]{0,1}', item.css('div.inner > h3.threadtitle > a.title::text').get())[1])
                    link = int(item.css('div.inner > h3.threadtitle > a.title::attr(href)').get().split('&s=')[0].split('?t=')[1])
                    last_post = item.css('dl.threadlastpost > dd > a.lastpostdate::attr(href)').get()
                    data = f'{{ "type": 1, "site": 1, "link": {link}, "quality": {quality}, "title": "{title}", "year": {year}, "poster": "{poster}" }}'
                    movies.append(json.loads(data))
                    yield Request(DescargasDD.base_url + '/' + last_post)
        else:
            data = {"No new movies."}
        print(json.dumps(movies, indent=2, ensure_ascii=False))

class GetSeries(scrapy.Spider):
    print("HOLA")

class ThanksButton(scrapy.Spider):
    name = "Scraping DescargasDD site and push thanks button."
    start_urls = [DescargasDD.base_url + "/login.php"]

    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'do': 'login',
                                            'vb_login_md5password': hashlib.md5(DescargasDD.web_password.encode()).hexdigest(),
                                            'vb_login_md5password_utf': hashlib.md5(DescargasDD.web_password.encode("utf-8")).hexdigest(),
                                            's': '',
                                            'securitytoken': 'guest',
                                            'url': DescargasDD.base_url,
                                            'vb_login_username': DescargasDD.web_user,
                                            'vb_login_password': '',
                                            },
                                        callback=self.scrapy_page_button)

    def scrapy_page_button(self, response):
        yield Request(
            url= DescargasDD.base_url + "/showthread.php?t=" + str(getattr(self, 'link', '#')),
            callback=self.push_thanks_button)
                
    def push_thanks_button(self, response):
        yield scrapy.FormRequest(
            url = DescargasDD.base_url + '/post_thanks.php',
            formdata={
                'do': 'post_thanks_add',
                'using_ajax': '1',
                'p': response.css('.postlinking > a.post_thanks_button::attr(href)').get().split('&')[1].split('=')[1],
                'securitytoken': response.css('.postlinking > a.post_thanks_button::attr(href)').get().split('&')[2].split('=')[1],
            }
        )

class GetDownloadURLs(scrapy.Spider):
    name = "Scraping DescargasDD site and get download URLs."
    start_urls = [DescargasDD.base_url + "/login.php"]

    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'do': 'login',
                                            'vb_login_md5password': hashlib.md5(DescargasDD.web_password.encode()).hexdigest(),
                                            'vb_login_md5password_utf': hashlib.md5(DescargasDD.web_password.encode("utf-8")).hexdigest(),
                                            's': '',
                                            'securitytoken': 'guest',
                                            'url': DescargasDD.base_url,
                                            'vb_login_username': DescargasDD.web_user,
                                            'vb_login_password': '',
                                            },
                                        callback=self.scrapy_page_urls)

    def scrapy_page_urls(self, response):
        yield Request(
            url = DescargasDD.base_url + "/showthread.php?t=" + getattr(self, 'link', '#'),
            callback=self.scrapy_download_urls)

    def scrapy_download_urls(self, response):
        url = ""
        links = response.css('.unhiddencontentbox > .bbcode_container > .bbcode_code ::text').getall()
        for link in links:
            url+=str(link.split('\n'))+","
        raw_data = '{ "urls" : [ '+re.sub(r"\b[oO]\b", "", (url.replace("[","").replace("]","").replace("'", '"').rstrip(',')))+' ] }'
        # Convertir JSON en un diccionario de Python
        json_dict = json.loads(raw_data)
        # Eliminar elementos vacíos de la lista "urls"
        json_dict['urls'] = [url for url in json_dict['urls'] if url]
        # Convertir el diccionario de Python de nuevo a JSON
        data = json.dumps(json_dict)
        print(json.dumps(json.loads(data), indent=2, ensure_ascii=False))

class AddComment(scrapy.Spider):
    name = "Add comment to a post into DescargasDD forum."
    start_urls = [DescargasDD.base_url + "/login.php"]

    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'do': 'login',
                                            'vb_login_md5password': hashlib.md5(DescargasDD.web_password.encode()).hexdigest(),
                                            'vb_login_md5password_utf': hashlib.md5(DescargasDD.web_password.encode("utf-8")).hexdigest(),
                                            's': '',
                                            'securitytoken': 'guest',
                                            'url': DescargasDD.base_url,
                                            'vb_login_username': DescargasDD.web_user,
                                            'vb_login_password': '',
                                            },
                                        callback=self.scrapy_page_comment)

    def scrapy_page_comment(self, response):
        yield Request(
            url= DescargasDD.base_url + "/showthread.php?t=" + getattr(self, 'link', '#'),
            callback=self.add_comment)

    def add_comment(self, response):
        data = {
            'message': getattr(self, 'comment', '¡Muchas gracias! :D'),
            's': response.css('form#quick_reply > input[name="s"]').attrib['value'],
            'securitytoken': response.css('form#quick_reply > input[name="securitytoken"]').attrib['value'],
            'do': response.css('form#quick_reply > input[name="do"]').attrib['value'],
            't': response.css('form#quick_reply > input[name="t"]').attrib['value'],
        }
        yield FormRequest(
            url = DescargasDD.base_url + "/newreply.php",
            method='POST',
            formdata=data
        )
