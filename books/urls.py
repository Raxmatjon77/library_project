from django.urls import  path
from rest_framework.routers import SimpleRouter
from .views import BookListApi,book_list_view,BookDetailApiView,\
    BookDeleteApiView,BookUpdateApiView,BookCreateApiView,BookListCreateApiView,\
BookUpdateDeleteApiView,BookViewSet

router=SimpleRouter()
router.register('books',BookViewSet,basename='books')
urlpatterns=[
    path('books/',BookListApi.as_view(),),
    path("books/<int:pk>/",BookDetailApiView.as_view(),),
    path("books/<int:pk>/update/", BookUpdateApiView.as_view(), ),
    path("books/<int:pk>/delete/", BookDeleteApiView.as_view(), ),
    path('books/create/',BookCreateApiView.as_view()),
    path('book/',BookListCreateApiView.as_view()),
    path('book/updatedelete/<int:pk>/',BookUpdateDeleteApiView.as_view()),

]
urlpatterns=urlpatterns+router.urls