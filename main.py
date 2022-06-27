from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

def get_data(url):
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
  }

  req = requests.get(url, headers)

  with open('project.html', 'w') as file:
    file.write(req.text)

get_data('http://web.archive.org/web/20200712235623/http://www.edutainme.ru:80/edindex')
