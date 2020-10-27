import requests
from datetime import timedelta, date



today = date.today()

get = requests.get('http://www.bengarlock.com:8080/books/?date=2020-10-26')
for item in get:
    print(get.json())


EndDate = today + timedelta(days=0)

obj = {
    "date": EndDate,
    "restaurant_id": 1,
    "slots": [],
}

url = "http://www.bengarlock.com:8080/books/"

post = requests.post(url, data=obj)
print(post.content)


# index = -1000
# while index <= 100:

#     index += 1