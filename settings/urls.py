from django.urls import path
from settings.views import index

urlpatterns = [
    path("", index, name='index')
]
