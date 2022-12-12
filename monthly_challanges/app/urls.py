from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('<int:month>',views.challanges_by_num,),
    path('<str:month>',views.challanges,name='appchallanges'),
]
