from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CommentSerializer
from .models import Comment

# Create your views here.

class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.user == request.user:
                serializer = CommentSerializer(comment, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'You do not have permission to edit this comment.'}, status=status.HTTP_403_FORBIDDEN)
        except Comment.DoesNotExist:
            return Response({'message': 'Comment does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.user == request.user:  # Ensure the user owns the comment
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'message': 'You do not have permission to delete this comment.'}, status=status.HTTP_403_FORBIDDEN)
        except Comment.DoesNotExist:
            return Response({'message': 'Comment does not exist.'}, status=status.HTTP_404_NOT_FOUND)



class CommentListAPIView(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)