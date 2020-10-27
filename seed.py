import requests
from datetime import timedelta, date

today = date.today()

get = requests.get('http://www.bengarlock.com:8080/books/?date=2020-10-27')
for item in get:
    print(get.json())

times = [
    '5:00 PM', '5:15 PM', '5:30 PM', '5:45 PM',
    '6:00 PM', '6:15 PM', '6:30 PM', '6:45 PM',
    '7:00 PM', '7:15 PM', '7:30 PM', '7:45 PM',
    '8:00 PM', '8:15 PM', '8:30 PM', '8:45 PM',
]




obj = {
    "booked": False,
    "time": "7:00 PM",
    "party_size": 2,
    "status": '',
    "tables": []
}

slot = requests.post('http://www.bengarlock.com:8080/slots/', data=obj)

with open('errors.html', 'w', encoding='utf-8') as file:
    file.write(str(slot.content))



# EndDate = today + timedelta(days=0)
#
#
#
# url = "http://www.bengarlock.com:8080/books/"
#
# post = requests.post(url, data=obj)
# print(post.content)
