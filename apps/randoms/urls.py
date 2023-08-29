
''' RANDOMS URLS'''


from django.contrib import admin
from django.urls import path

from randoms.views import RandomView, slot_mashine, BaseView, base

urlpatterns = [
    
    path('slot_mashine/', slot_mashine , name='slot_machine'),
    path('wheel/', RandomView.as_view(), name='random'),
    path('slot_mashine/', slot_mashine),
    # path('base/', BaseView.as_view()),
    path('', base),
    
    # path('', RandomView.as_view(), name='random'),
]
