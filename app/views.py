from rest_framework.views import APIView
from .models import Blog
from .serializers import *
from rest_framework.response import Response

# Create your views here.

class PostList(APIView):
    def get(self,request):
        blogs=Blog.objects.all()
        serializer= BlogSerializer(blogs,many=True)
        return Response({'payload':serializer.data,'status':200})

    def post(self,request):
        data=request.data
        serializer = PostBlogSerializer(data=data)
        if not serializer.is_valid():
                return Response({'status':300,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        return Response({'status':200,'message':'blog is added successfully'})
    
class BlogPost(APIView):
     def get(self,request):
          try:
               
                id=request.GET.get('id')
                blog=Blog.objects.get(pk=id)
                serializer=BlogSerializer(blog)
                return Response({'payload':serializer.data,'status':200})
          except Exception as e:
               return Response({'error':str(e),'status':404})
          
     def patch(self,request):
          try:
               data=request.data
               id=request.GET.get('id')
               blog=Blog.objects.get(pk=id)
               serializer=PostBlogSerializer(instance=blog,data=data,partial=True)
               if not serializer.is_valid():
                    return Response({'status':300,'error':serializer.errors,'message':'somthing went wrong in serializer'})   
               serializer.save()
               return Response({'status':200,'message': 'blog updated successfully'})


          except Exception as e:
               return Response({'error':str(e),'status':404})
          
     def delete(self,request):
                try:
                 id=request.GET.get('id')
                 print(id)
                 blog=Blog.objects.get(pk=id)
                 blog.delete()
                 return Response({'status':200,'message':'blog deleted successfully'})
                except Exception as e:
                    return Response({'error':str(e)})

           