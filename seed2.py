from guests.models import Guest

root_user = Guest.objects.create(
    first_name='',
    last_name='',
    phone_number='',
    guest_notes='',
    root_user=True,
    slot=[]
)

