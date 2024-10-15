from django.contrib import admin


from .models import Profile, PhoneNumber
#admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','balance','get_phone_number')
    

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display=('phone_number',)
