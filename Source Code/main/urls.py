from django.urls import path
from .views import HomePage, uploadBook

urlpatterns = [
    path('home/', HomePage.as_view(), name="home"),
    path('uploadBook/', uploadBook, name="upload_book"),
]