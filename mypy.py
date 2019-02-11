import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://119.205.79.142/wordpress/')
soup = bs(r.text, 'html.parser')
main = soup.find('main', id='main')
posts = main.find_all('article', class_='post')

data = []
for post in posts:
    tp = [
        {
            'title' : post.find('h3', class_='entry-title').find('a').string,
            'link' : post.find('h3', class_='entry-title').find('a').get('href')
        }
    ]
    data.append(tp)
    
print(data)