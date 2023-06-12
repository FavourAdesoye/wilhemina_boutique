from django.urls import path
from . import views
# from .views import bag_view


urlpatterns = [
    path('', views.bag_view)
]
