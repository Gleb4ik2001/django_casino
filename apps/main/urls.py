
''' MAIN URLS'''



from django.urls import path

from main.views import main_page ,add_balance

urlpatterns = [
    path('', main_page , name='main_page'),
    path('add_balance/', add_balance,name='add_balance')
]
