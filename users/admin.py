from django.contrib import admin
from .models import Interest, Profile


class InterestAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","email","location","hometown","bio","avatar","birthdate",)

admin.site.register(Interest, InterestAdmin)
admin.site.register(Profile, ProfileAdmin)
