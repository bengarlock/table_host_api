from guests.models import Guest
from restaurants.models import Restaurant

# root_user = Guest.objects.create(
#     first_name='',
#     last_name='',
#     phone_number='',
#     guest_notes='',
#     root_user=True,
#     slot=[]
# )

root_restaurant = Restaurant.objects.create(
    name='ilili',
)