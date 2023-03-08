from bs4 import BeautifulSoup as BS
import requests 
# source = requests.get('http://www.example.com/').text

# soup = BS(source , 'lxml')
# my_div = soup.find('div', {'h1':'p'})
# print(my_div)


# import csv 
# source = requests.get('http://www.example.com/').text 
# my_page = BS(source, 'lxml') 
# h1 = 'h1:', my_page.h1.text
# print(h1)
# print('p:', my_page.p.text) 
# print('a:', my_page.a.get('href'))

"3"
# source = requests.get('https://www.wikipedia.org/')
# my_page = BS(source.text, 'lxml') 
# # print(my_page)
# wiki = my_page.find('div',{'class':'central-featured-lang lang4'})
# title = wiki.find('strong').text
# title1 = wiki.find('small').text

# print(title)
# print(title1)

"4"
# def getTitle(url:str):

#         source = requests.get(url)
#         my_page = BS(source.text, 'lxml').find('h1')
#         if my_page==None:
#             return "Title could not be found"
#         else:
#             return my_page

    
# print(getTitle('http://www.example.com/'))
'6'
source = requests.get('https://www.imdb.com/chart/top')
my_page = BS(source.text, 'lxml')
# my_list = my_page.find('div',{'class':'lister'}).find_a('img')
my_list = my_page.find('td',{'class':'titleColumn'}).text.strip().split("\n")[1]
# print(my_list)
# title =my_page.find_all('div',{'class':'lister'}).find('img').get('alt')
# print(len(title))

title = my_page.find('tbody',{'class':'lister-list'})
print(title)
box = title.find_all('td',{'class':'titleColumn'})

# print(len(w))
list_=[]


# print(box[0].text.split('"'))




# for product in box:
#     title = product.text.strip().split("\n")[1]
#     www = "https://www.imdb.com"
#     list_.append(title.strip())
# print(list_)

# def get_link(list_:list, s:str):





    
