from ecommerce.models import Setting
from django.contrib import admin
from ecommerce.models import Setting, ContactMessage
# Register your models here.

admin.site.register(Setting)
admin.site.register(ContactMessage)
