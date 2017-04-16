from django.contrib import admin

from social_auth.models import SteamUser


@admin.register(SteamUser)
class SteamUserAdmin(admin.ModelAdmin):
    pass
