import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from lib_c.redis import RedisCahche
from django.http import HttpResponse

redis = RedisCahche()
FASTAPI_URL = 'http://fastapi:9000/data/'


class DataCreateView(View):

    def get(self, request):
        return render(request, 'data_create.html')
    
    def post(self, request):
        key = request.POST.get('key')
        value = request.POST.get('value')
        pot = request.POST.get('pot')
        if pot:
            return HttpResponse('<div><h2>Nice try m8</h2></div>')
        
        response = requests.post(FASTAPI_URL, json={'key': key, 'value': value})
        if response.status_code == 200:
            redis.write(key, value)

            redirect('items_list')
        return render(request, 'data_create.html', {'error': 'Filed to create Item'})
    
class DataListView(View):
    def get(self, request):
        key = request.GET.get('key')
        if not key:
            return render(request, 'item_list.html')
        cached_item = redis.read(key)
        if cached_item:
            cached_item = str(cached_item, 'utf-8')
            data = {'key': key, 'value': cached_item}
            return render(request, 'item_list.html', {'data': data})
        response = requests.get(f'{FASTAPI_URL}{key}')
        if response.status_code == 200:
            value = response.json().get('value')
            redis.write(key, value)
            data = {'key': key, 'value': value}
            return render(request, 'item_list.html', {'data': data})
        return render(request, 'item_list.html', {'error': 'Filed to read Item'})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return HttpResponse('Invalid login credentials', status=401)
    else:
        return render(request, 'login.html')
    
def home_view(request):
    username = request.user.username
    return render(request, 'home_page.html', {'username': username.removeprefix('hillel_')})
