from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from rest_framework import generics,status
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApi(APIView):

    def get(self,request):
        books=Book.objects.all()
        seriaalizer_data=BookSerializer(books,many=True).data
        data={
            'status':f"returned { len(books)} books ",
            'books':seriaalizer_data
        }
        return Response(data)


#function based view
@api_view(['GET'])
def book_list_view(request,*args,**kwargs):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self,request,pk):
       try:
            book=Book.objects.get(id=pk)
            serializer_date=BookSerializer(book).data
            data={
                'book':serializer_date,
                "status":'successful'

            }
            return  Response(data,status=status.HTTP_200_OK)
       except Exception:
            return Response({'status':'False',
                             'message':'book is not found'},status=status.HTTP_404_NOT_FOUND)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self,request,pk):
        try:
            book=Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status':True,
                'message':'Successfully deleted'
            },status=status.HTTP_200_OK)

        except Exception:
            return Response({
                'status':False,
                'message':'book is noit found'
            },status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):

    def put(self,request,pk):

        book=get_object_or_404(Book.objects.all(),id=pk)
        data=request.data
        serializer=BookSerializer(instance=book,data=data,partial=True)
        if serializer.is_valid():
            book_saved=serializer.save()
        return Response(
            {
                'status':True,
                'message': f" {book_saved} updated successfully"
            }
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApiView(APIView):

    def post(self,request):
        data=request.data
        serializer=BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data={
                "status": f"books are saved to database",
                'books':data

            }
        return Response(data)
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer