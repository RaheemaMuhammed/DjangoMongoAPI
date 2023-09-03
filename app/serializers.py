from .models import Blog


from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','body','posted_at']

class PostBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'