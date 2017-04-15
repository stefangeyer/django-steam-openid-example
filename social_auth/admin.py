from django.contrib import admin

from social_auth.models import SteamUser


class SteamUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(SteamUser, SteamUserAdmin)
