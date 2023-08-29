"""MAIN APP"""

from django.shortcuts import render
from randoms.models import Banner
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def main_page(request:HttpRequest) -> HttpResponse:
    active_banners = Banner.objects.filter(is_active=True)
    context = {'active_banners': active_banners}
    return render(
        template_name='new_main.html',
        request=request,
        context = context
    )

def add_balance(request:HttpRequest) -> HttpResponse:
    template_name = 'add_balance.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )
    


# def banner_display(request):
#     active_banners = Banner.objects.filter(is_active=True)
#     return render(request, 'new_main.html', {'active_banners': active_banners})