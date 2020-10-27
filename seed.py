import requests
from datetime import timedelta, date

url = "http://www.bengarlock.com:8080/books/"

today = date.today()

print(url)


get = requests.get('http://127.0.0.1:8000/books/')
for item in get:
    print(get.json())


EndDate = today + timedelta(days=0)

obj = {
    "date": EndDate,
    "restaurant_id": 1,
    "booked": False,
}

post = requests.post(url, data=obj)
print(post)





# index = -1000
# while index <= 100:

#     index += 1