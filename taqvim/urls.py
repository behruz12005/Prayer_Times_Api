from django.urls import path
from taqvim import views
urlpatterns = [
    path('',views.taqvim,name='home'),
    path('ajdval/',views.jadval,name='jadval'),
]