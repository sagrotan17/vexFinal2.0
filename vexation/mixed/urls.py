from django.conf.urls import url

from . import views

app_name='mixed'

urlpatterns = [
    url(r'^$',views.home, name='home'),

]