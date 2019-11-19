from django.contrib import admin
from location.models import Country_group
from location.models import Visa_group
from location.models import Age_group

# Register your models here.
admin.site.register(Country_group)
admin.site.register(Visa_group)
admin.site.register(Age_group)