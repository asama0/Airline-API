from django.contrib import admin
from .models.models import *

admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(Customer)
admin.site.register(Airport)
admin.site.register(PaymentProvider)
admin.site.register(Ticket)
admin.site.register(Booking)

