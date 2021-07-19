from rest_framework import serializers
from .models import book

class bookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    ISBN_number = serializers.IntegerField()

    def create(self, book_data):
        return book.objects.create(**book_data)

    def update(self, instance, book_data):
        instance.name = book_data.get('name', instance.name)
        instance.ISBN_number = book_data.get('ISBN_number', instance.ISBN_number)
        instance.save()
        return instance