from django.contrib import admin

from .models import DiscontCard

@admin.register(DiscontCard)
class DiscontCardAdmin(admin.ModelAdmin):
    list_display = ('id','user','pension','accumulative','active')


