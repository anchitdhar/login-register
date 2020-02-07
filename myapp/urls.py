from django.urls import path
from myapp.views import *

urlpatterns = [
    path('add',views.add),
    path('delete',views.remove),
    path('search',views.search),
]
