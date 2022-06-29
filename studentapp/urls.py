from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view),
    path('features/',features_view),
    path('login/',login_view),
    path('formula/',formula_view),
    path('signup/',signup_view),
    path('register/',register_view),
    path('add/',add_view)
]