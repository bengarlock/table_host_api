from rest_framework import routers
from books.views import BookView
from guests.views import GuestView
from slots.views import SlotView
from django.contrib import admin
from django.conf.urls import url

router = routers.SimpleRouter()

router.register(r'books', BookView)
router.register(r'guests', GuestView)
router.register(r'slots', SlotView)

urlpatterns = [
    url('admin/', admin.site.urls),
]

urlpatterns += router.urls
