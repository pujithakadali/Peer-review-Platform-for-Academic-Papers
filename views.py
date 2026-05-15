from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated  # ✅ CORRECT PLACE TO IMPORT

from .models import Paper, Review
from .serializers import UserSerializer, PaperSerializer, ReviewSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class PaperUploadView(generics.CreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [IsAuthenticated]  # ✅ ADD THIS HERE

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PaperListView(generics.ListAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # keep this line only once


