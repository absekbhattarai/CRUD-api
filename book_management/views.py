from .models import book
from .serializers import bookSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class bookViewSet(viewsets.ViewSet):
#Add a books
    def create(self,request):
        serializer = bookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
  
#list all the books
    def list(self,request):
        books = book.objects.all()
        serializer = bookSerializer(books,many=True)
        return Response(serializer.data)
        
#Show book by ID
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            books = book.objects.get(pk=id)
            serializer = bookSerializer(books)
            return Response(serializer.data)

#Update any books
    def update(self,request,pk=None):
        id = pk
        books = book.objects.get(pk=id)
        serializer = bookSerializer(books, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book Updated'})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#delete any book
    def destroy(self,request,pk=None):
        id = pk
        books = book.objects.get(pk=id)
        books.delete()
        return Response({'msg':'Book is deleted'})
