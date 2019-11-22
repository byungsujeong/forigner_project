from django.contrib import admin
from bbs.models import Bbs
from bbs.models import Review

# Register your models here.
# 어드민 관리 등록
admin.site.register(Bbs)
admin.site.register(Review)