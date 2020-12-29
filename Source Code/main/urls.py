from django.urls import path
from .views import HomePage, BookUploadView, BookDetailView, BookUpdateView, BookDeleteView, SearchResultsView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('uploadBook/', BookUploadView.as_view(), name="upload_book"),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]