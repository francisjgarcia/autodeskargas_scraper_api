from django.urls import path
import os
from .views import thanks, download_urls, comments
    
urlpatterns = [
    path('thanks', thanks, name='thanks'),
    path('download_urls', download_urls, name='download_urls'),
    path('comments', comments, name='comments')
]

if os.environ['SCRAPY_TYPE'] == 'movies':
    from .views import movies
    urlpatterns += [
        path('movies', movies, name='movies'),
    ]
elif os.environ['SCRAPY_TYPE'] == 'series':
    from .views import series
    urlpatterns += [
        path('series', series, name='series'),
    ]
