from django.urls import path
from .views import DataCreateView, DataListView, login_view, home_view

urlpatterns = [
    path('data/create/', DataCreateView.as_view(), name='data_create'),
    path('data/', DataListView.as_view(), name='items_list'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home')
]