from django.contrib import admin
from member.models import Member
from member.models import Country

# Register your models here.
admin.site.register(Member)
admin.site.register(Country)