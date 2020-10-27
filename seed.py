import requests
from datetime import timedelta, date
import json

today = date.today()

def create_books(date_cap):
    index = 0
    books = []

    while index <= date_cap:
        date = today + timedelta(days=index)
        obj = {
            "date": date,
            "restaurant_id": 1,
            "slots": [],
        }
        book = requests.post(url="http://www.bengarlock.com:8080/books/", data=obj)
        r = book.content.decode('UTF-8')
        res = json.loads(r)
        books.append(res["id"])
        print("Creating book: " + str(date))
        index += 1

    for book in books:
        create_slots(book)


def create_slots(book_id):

    times = [
        '5:00 PM', '5:15 PM', '5:30 PM', '5:45 PM',
        '6:00 PM', '6:15 PM', '6:30 PM', '6:45 PM',
        '7:00 PM', '7:15 PM', '7:30 PM', '7:45 PM',
        '8:00 PM', '8:15 PM', '8:30 PM', '8:45 PM',
    ]

    for time in times:
        obj = {
            "booked": False,
            "time": time,
            "party_size": 2,
            "status": '',
            "tables": [],
            "book_id": 1,
        }

        slot = requests.post('http://www.bengarlock.com:8080/slots/', data=obj)

create_books(10)























# EndDate = today + timedelta(days=0)
#
#
#
# url = "http://www.bengarlock.com:8080/books/"
#
# post = requests.post(url, data=obj)
# print(post.content)
