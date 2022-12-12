from django.urls import path
from . import views

urlpatterns = [
    path('',views.startingPage,name='starting-page'),
    path('post',views.post,name='post-page'),
    path('post/<slug:slug>',views.postDetail,name="detail-page")
]
