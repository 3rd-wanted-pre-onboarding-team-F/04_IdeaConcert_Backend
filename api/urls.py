from django.urls import path

from api.views import home


urlpatterns = [
    path('hello/', home, name='home'),
]