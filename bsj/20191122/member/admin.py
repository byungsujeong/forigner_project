from django.contrib import admin
from member.models import Member
from member.models import Country

# Register your models here.
# 어드민 관리 등록
admin.site.register(Member)
admin.site.register(Country)