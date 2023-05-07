from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json
import os

if os.environ['SCRAPY_TYPE'] == 'movies':
    @csrf_exempt
    def movies(request):
        try:
            if request.method == 'POST':
                result = subprocess.run(['python', 'scraper/crawler/movies_id.py', str(json.loads(request.body.decode('utf-8'))["quality"])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return HttpResponse(result.stdout, status=200)
            else:
                result = subprocess.run(['python', 'scraper/crawler/movies.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return HttpResponse(result.stdout, status=200)
        except:
            return HttpResponse(status=500)
elif os.environ['SCRAPY_TYPE'] == 'series':
    @csrf_exempt
    def series(request):
        try:
            if request.method == 'POST':
                result = subprocess.run(['python', 'scraper/crawler/series_id.py', str(json.loads(request.body.decode('utf-8'))["quality"])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return HttpResponse(result.stdout, status=200)
            else:
                result = subprocess.run(['python', 'scraper/crawler/series.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return HttpResponse(result.stdout, status=200)
        except:
            return HttpResponse(status=500)
else:
    def error(request):
        return HttpResponse(status=404)

@csrf_exempt
def thanks(request):
    try:
        if request.method == 'POST':
            result = subprocess.run(['python', 'scraper/crawler/thanks.py', str(json.loads(request.body.decode('utf-8'))["link"])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return HttpResponse(result.stdout, status=200)
        else:
            return HttpResponse(status=400)
    except:
        return HttpResponse(status=500)

@csrf_exempt
def download_urls(request):
    try:
        if request.method == 'POST':
            result = subprocess.run(['python', 'scraper/crawler/download_urls.py', str(json.loads(request.body.decode('utf-8'))["link"])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return HttpResponse(result.stdout, status=200)
        else:
            return HttpResponse(status=400)
    except:
        return HttpResponse(status=500)

@csrf_exempt
def comments(request):
    try:
        if request.method == 'POST':
            result = subprocess.run(['python', 'scraper/crawler/comments.py', str(json.loads(request.body.decode('utf-8'))["link"]), json.loads(request.body.decode('utf-8'))["comment"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return HttpResponse(result.stdout, status=200)
        else:
            return HttpResponse(status=400)
    except:
        return HttpResponse(status=500)