from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    author_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

# class PublisherSerializer(serializers.Serializer):
#      pub_name = serializers.CharField(max_length=100)  

# class BookSerializer(serializers.Serializer):
#     slug = serializers.SlugField(max_length=100)
#     book_name = serializers.CharField(max_length=100)
#     book_price = serializers.IntegerField()
#     book_page = serializers.IntegerField()
#     author = serializers.ManyToManyField(Author)
#     publisher = serializers.ForeignKey(Publisher, on_delete=models.CASCADE)
#     pub_date = serializers.DateField()