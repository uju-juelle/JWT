from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_homepage(request):
    all_blogs = Blog.objects.all()
    serializer = BlogSerializer(all_blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# class Homepage(ListCreateView):
#     permission_class = [IsAuthenticated]






