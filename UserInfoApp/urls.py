from django.conf.urls import url

from . import views

app_name = 'user_info'

urlpatterns = [
    url(r'^$', views.info, name='main'),
]
