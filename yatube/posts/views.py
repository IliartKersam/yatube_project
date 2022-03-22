#from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Группа {slug}')
# Create your views here.
