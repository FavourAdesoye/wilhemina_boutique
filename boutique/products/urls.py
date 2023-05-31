from django.urls import path
from . import views
# from .views import cloth_view


urlpatterns = [
    path('', views.cloth_view)

]
