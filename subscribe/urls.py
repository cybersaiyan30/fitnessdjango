from django.urls import path,re_path
from django.conf.urls import url

from . import views

app_name='subscribe'

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^demo/[a-zA-Z0-9]*',views.subscribe,name='subscribe'),
    url(r'^store/[a-zA-Z0-9]*',views.store,name='store'),
    url(r'^diet/[a-zA-Z0-9]*',views.diet,name='diet'),
    url(r'^men/[a-zA-Z0-9]*',views.men,name='men'),
    url(r'^register/[a-zA-Z0-9]*',views.register,name='register'),
    url(r'^user_login/[a-zA-Z0-9]*',views.user_login,name='user_login'),
]





