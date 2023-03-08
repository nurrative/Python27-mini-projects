import requests
from bs4 import BeautifulSoup as BS
import csv

BASE_URL = 'https://www.mashina.kg'

# функция которая превращает url в BS для парсинга
def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

# так как каждая характеристика машины хранится в разных классах, я решил отдельную 
# функцию создать, чтобы не перегружать функцию get_product_info
def description_info(product:BS):
    engine=product.find('p',{'class':'body-type'}).text.strip()
    specifications=product.find('p',{'class':'volume'}).text.strip()
    age = product.find('p',{'class':'year-miles'}).text.strip()
    city =product.find('p',{'class':'city'}).text.strip().split("\n")[0]
    return f'Двигатель: {engine} Спецификации: {specifications} Год {age} Город: {city}'

# функция get_product_info достает из BS название, цену, ссылку на фото и
# вызывает функцию write_to_csv для добавления в файл csv
def get_product_info(product:BS) -> dict:
    title = product.find('h2').text.strip()
    let =product.find('p').text.strip().split('\n')
    price = let[0]+'/'+let[-1].lstrip()
    image = product.find('img').get('data-src')
    description = description_info(product)
    list_data=[title,price, description, image]
    write_to_csv(list_data)
    return list_data

# благодаря get_last_page мы узнаем последнюю страницу категории которую парсим
def get_last_page(url)->int:
    soup = get_soup(url)
    pages = soup.find_all('li', {'class' : "page-item"})[-1].find('a').get('data-page')

    return int(pages)

# достаем всю информацию со всех страниц сайта
def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div',{'class':'table-view-list'})
    products = box.find_all('div',{'class':'list-item'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
        # write_to_csv(product_info)
    return res

# получаем с функции get_product_info инфо каждой машины и записываем в car_data.csv
def write_to_csv(data):
    filename = 'car_data.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for i in data:
            writer.writerow([i])

# главная функция main в которой создается url категории и вызывается функция 
# get_all_products_from_page для прасинга  
def main():
    category = '/specsearch/all/'
    data = []
    last_page = get_last_page(BASE_URL+category)
    for page in range(1,last_page+1):
        url = (BASE_URL+category+'?page='+str(page))
        print(url)
        one_page_data=get_all_products_from_page(url)
        data.append(one_page_data)

# я спарсил страницу спецтехники(тракторы,комбайны и т.д. сайта mashina.kg)
main()

