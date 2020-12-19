from django.urls import path
from .views import HomePage, BookUploadView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('uploadBook/', BookUploadView.as_view(), name="upload_book"),
]