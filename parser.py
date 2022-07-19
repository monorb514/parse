import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "accept": "*/*"}
URL = 'https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c093b'
LINK = "https://cars.kg"
FILE = 'result.csv'


def get_html(headers, url):
    response = requests.get(url, headers=headers)
    return response


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="catalog-list-item")
    cars = []
    for i in items:
        cars.append({
            "title": i.find("span", class_="catalog-item-caption").get_text().strip(),
            "image": LINK+i.find("img").get('src'),
            "description": i.find("span", class_="catalog-item-descr").get_text().replace("\n", ""),
            "price": i.find("span", class_="catalog-item-price").get_text().replace("\n", ""),
        })

    return cars


def save_file(content, file):
    with open(file, "w") as f:
        writer = csv.writer(f, delimiter =';')
        writer.writerow(["Название продукта", "Картинка", "Описание", "Цена"])
        for i in content:
            writer.writerow([i['title'], i['image'], i['description'], i['price']])


def get_parse_result():
    html = get_html(url=URL, headers=HEADERS)
    content = get_content(html.text)
    save_file(content, FILE)


get_parse_result()


