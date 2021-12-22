# from django.urls import path
#
# from . import views
#
# app_name = 'main'
#
# urlpatterns = [
#     path('', views.home, name='home'),
# ]
from django.contrib import admin
from django.conf.urls import url,include
from . import views
urlpatterns=[
     url(r'^admin/',admin.site.urls),
     url(r'^register/',include('blog.urls')),
     url(r'^$',views.home),
]