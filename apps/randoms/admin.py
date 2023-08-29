from django.contrib import admin

from .models import Banner, Bet


# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
        'is_active',
        'banner_file',
    )
    list_filter: list[str] = (
        'name',
    )   

admin.site.register(Banner, BannerAdmin)

class BetAdmin(admin.ModelAdmin):
    list_display = ('game', 'amout', 'who', 'coef')  # Corrected 'amout' field name
    list_filter = ('game', 'who')
    search_fields = ('who__username',)

admin.site.register(Bet, BetAdmin)
