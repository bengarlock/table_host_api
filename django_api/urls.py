from rest_framework import routers
from books.views import BookView
from guests.views import GuestView
from slots.views import SlotView

router = routers.SimpleRouter()

router.register(r'books', BookView)
router.register(r'guests', GuestView)
router.register(r'slots', SlotView)

urlpatterns = router.urls
