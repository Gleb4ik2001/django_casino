'''RANDOM VIEWS'''
import random


from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .models import Banner


class RandomView(View):
    """Класс, который служит для рандомных штук"""

    def get(self, request):
        random_number = random.randint(-100, 100)
        active_banners = Banner.objects.filter(is_active=True)
        context = {'random_number': random_number,
                   'active_banners': active_banners}
        return render(
            template_name='random/wheel.html',
            request=request,
            context = context
        )
    

def slot_mashine(request):
    active_banners = Banner.objects.filter(is_active=True)
    context = {'active_banners': active_banners}
    return render(
        template_name='random/slot_mashine.html',
        request=request,
        context = context
    )


class BaseView(View):
    def get(self, request):
        active_banners = Banner.objects.filter(is_active=True)
        context = {'active_banners': active_banners}
        return render(
            template_name='random/base.html',
            request=request,
            context = context
        )
    
def base(request):
    active_banners = Banner.objects.filter(is_active=True)
    context = {'active_banners': active_banners}
    return render(
        template_name='random/slot_mashine.html',
        request=request,
        context = context
    )