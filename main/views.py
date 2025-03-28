from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина - Home'
    }
    return render(request, 'main/index.html', context)

def about(request):
   context = {
       'title': 'Home - О нас',
       'content': 'О нас',
       'text_on_page': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint in laborum eius voluptate rerum doloribus veritatis provident odit nesciunt totam laudantium, saepe deleniti vel! Quo sit architecto deserunt ipsum esse.',
   }
   return render(request, 'main/about.html', context)
