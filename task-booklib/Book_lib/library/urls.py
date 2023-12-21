from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('aggregation/' , aggregation , name = 'aggregation'),
    
    path('authorform/' , create_authorform , name = 'authorform'),
    path('author-details/<str:pk>/' , author_details , name = 'authordetails'),
    path('author-update/<str:pk>/' , author_update , name = 'authorupdate'),
    path('author-delete/<str:pk>/' , delete_author , name = 'authordelete'),
    
    path('bookform/', create_bookform , name= 'bookform'),
    path('book-details/<str:pk>/' , book_details , name = 'bookdetails'),
    path('update-book/<str:pk>/' , update_bookform , name = 'updatebook'),
    path('delete-book/<str:pk>/' , delete_bookform , name = 'deletebook'),
]