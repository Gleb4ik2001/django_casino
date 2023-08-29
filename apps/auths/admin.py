from django.contrib import admin

from .models import (
    MyUserManager,
    MyUser,
    ActivationCode,
    BankCard,
    Transaction,

)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname', 'currency', 'balance']
    list_filter = ['email', 'nickname', 'currency']
    ordering = ['email', 'nickname']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amout', 'datetime_created', 'is_filled']
    list_filter = ['user', 'amout', 'datetime_created', 'is_filled']
    ordering = ['user', 'amout']


# admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(Transaction, TransactionAdmin)
