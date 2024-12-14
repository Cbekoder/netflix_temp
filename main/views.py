from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieModelSerializer, ActorSerializer, MovieGetModelSerializer
from .models import Movie, Actor


class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            Actor.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)


class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieGetModelSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieGetModelSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieModelSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=204)