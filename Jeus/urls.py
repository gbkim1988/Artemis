from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /Jeus/
    url(r'^$', views.home, name="home"),
]
