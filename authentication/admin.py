from django.contrib import admin

from authentication.models import SteamUser


@admin.register(SteamUser)
class SteamUserAdmin(admin.ModelAdmin):
    pass
