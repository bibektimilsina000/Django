from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Movies
from .serializers import MovieSerializer


@api_view(["GET", "POST"])
def movieList(request):
    if (request.method == "GET"):
        movie_list = Movies.objects.all()
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)
    elif (request.method == "POST"):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(["GET", "PUT","DELETE"])
def movie(request, pk):

    if (request.method == 'GET'):
        movie = Movies.objects.get(id=pk)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    if (request.method == 'PUT'):
        movie = Movies.objects.get(id=pk)

        serializer = MovieSerializer(data=movie)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if (request.method == "DELETE"):
        movie = Movies.objects.get(id == pk)
        movie.delete()
        return Response(serializer.data)
