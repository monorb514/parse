import requests
from bs4 import BeautifulSoup

URL = 'https://www.kivano.kg/mobilnye-telefony'
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "accept": "*/*"}

def get_html(headers, url, params = None):
    response = requests.get(url, params)
