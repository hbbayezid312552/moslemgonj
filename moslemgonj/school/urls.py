
from django.urls import path
from . import views

urlpatterns = [

    path('jbhs/',views.jbhs,name='jbhs'),
    path('mhs/',views.mhs,name='mhs'),
    path('login/',views.login,name='login'),
    path('singup/',views.singup,name='singup'),
    
]