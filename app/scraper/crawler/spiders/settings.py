from dotenv import load_dotenv
import os
import time

# Set timezone
os.environ['TZ'] = 'Europe/Madrid'
time.tzset()

# Set dotenv
load_dotenv()

# General settings
settings = {
    'FEED_EXPORT_ENCODING': 'utf-8',
    'LOG_ENABLED': 'False',
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
}

class DescargasDD():
    # Scraping DescargasDD
    base_url = os.getenv('BASE_URL', 'https://descargasdd.org')
    web_user = os.getenv('WEB_USER', 'username')
    web_password = os.getenv('WEB_PASSWORD', 'password')
    movies_pages = {
        "micro1080": 143, # Micro FullHD
        "bdrip1080": 142, # BDrip FullHD
        "h265": 250, # H265
        "4k": 164, # 4K
        "animation_micro1080": 324, # Animation Micro FullHD
        "animation_bdrip1080": 323, # Animation BDrip FullHD
        "animation_h265": 339, # Animation H265
        "animation_4k": 315, # Animation 4K
        "anime_micro1080": 396, # Anime Micro FullHD
        "anime_micro1080_vose": 397, # Anime Micro FullHD VOSE
        "anime_bdrip1080": 399, # Anime BDrip FullHD
        "anime_bdrip1080_vose": 400, # Anime BDrip FullHD VOSE
        "anime_h265": 402, # Anime H265
        "anime_h265_vose": 403, # Anime 4K VOSE
    }
    series_pages = {
        "micro1080": 118, # Micro FullHD
        "hd_1080": 51, # HD 1080
        "h265": 102, # H265
        "4k": 342, # 4K
        "miniseries_micro1080": 120, # Miniseries Micro FullHD
        "miniseries_hd_1080": 53, # Miniseries HD 1080
        "miniseries_h265": 104, # Miniseries H265
        "miniseries_4k": 344, # Miniseries 4K
        "animation_micro1080": 122, # Animation Micro FullHD
        "animation_hd_1080": 112, # Animation HD 1080
        "animation_h265": 113, # Animation H265
        "animation_4k": 345, # Animation 4K
        "anime_micro1080": 384, # Anime Micro FullHD
        "anime_hd_1080": 385, # Anime HD 1080
        "anime_h265": 386, # Anime H265
        "anime_4k": 387, # Anime 4K
    }
    # Scrapy always or only news
    if os.getenv('SCRAPY_ALWAYS', 'False') == "False":
        scrapy_always = ".new"
    else:
        scrapy_always = ""
