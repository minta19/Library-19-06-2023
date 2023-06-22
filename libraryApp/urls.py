from django.urls import path
from . import views
from .views import AuthorListView
urlpatterns=[
    path('',views.home,name='home'),
    path('booklist/',views.book_list,name='booklist'),
    path('bookdetails/<int:book_id>/',views.book_details,name='bookdetails'),
    path('authorlist/',AuthorListView.as_view(),name='author_list'),
]