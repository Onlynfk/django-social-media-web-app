
from rest_framework.generics import ListAPIView
from ..models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.db.models import Q


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the author from the request.
        author = request.user
        req_data = request.data

        # Create a new post instance.
        post = Post.objects.create(
            title=req_data.get('title'),
            content=req_data.get('content'),
            author=author,
        )

        # Save the post instance.
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PostUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # Get the post instance.
        post = get_object_or_404(Post, pk=pk)

        # Check if the authenticated user is the author of the post.
        if post.author != request.user:
            raise PermissionDenied(
                'You are not authorized to update this post.')

        # Get the new data from the request.
        data = request.data

        # Check if the title and content are provided.
        if not data.get('title') or not data.get('content'):
            return Response('Title and content must be provided.', status=status.HTTP_400_BAD_REQUEST)

        # Update the post instance.
        post.title = data.get('title')
        post.content = data.get('content')
        post.save()
        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        # Get the post instance.
        post = get_object_or_404(Post, pk=pk)

        if post.author != request.user:
            raise PermissionDenied(
                'You are not authorized to update this post.')

        # Delete the post instance.
        post.delete()

        return Response(status=204)


class SearchAPIView(APIView):
    def get(self, request):
        query = self.request.query_params.get('query')

        if not query:
            return Response([], status=status.HTTP_200_OK)

        # Perform a case-insensitive search for both title and username
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )

        # Serialize the search results
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserPostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Post.objects.filter(author__username=username).order_by('-date_posted')
    


class SavedPostsAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        saved_posts = user.blogsave.all()
        print(" blogs = saved_posts", saved_posts)
        serializer = PostSerializer(saved_posts)
        return Response (serializer.data, status=status.HTTP_200_OK)