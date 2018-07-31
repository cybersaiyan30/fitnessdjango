from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from subscribe import views

urlpatterns = [

    url(r'^$',views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^subscribe/',include('subscribe.urls')),
    url(r'^logout/',views.user_logout,name='logout'),
]

