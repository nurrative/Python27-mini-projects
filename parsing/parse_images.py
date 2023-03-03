import requests,json

image_url = 'https://avatars.mds.yandex.net/get-mpic/4262452/img_id5635830207981014623.jpeg/orig'

response = requests.get(image_url)

with open('images/test.jpg','wb') as file:
    file.write(response.content)