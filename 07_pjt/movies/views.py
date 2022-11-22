

from django.shortcuts import get_object_or_404
from .models import Actor, Review, Movie
from .serializers import (
    ActorSerializer, ReviewSerializer,
     MovieSerializer, MovieSerializer2,
     ReviewSerializer2,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
@api_view(["GET"])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response (serializer.data, status = status.HTTP_200_OK)
    

@api_view(["GET"])
def actor_detail(request, actor_pk):
    if request.method == "GET":
        actor = Actor.objects.get(pk=actor_pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer2(movies, many=True)
        return Response (serializer.data, status = status.HTTP_200_OK)

@api_view(["GET"])
def movie_detail(request, movie_pk):
    if request.method == "GET":
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer2(reviews, many=True)
        return Response (serializer.data, status = status.HTTP_200_OK)

@api_view(["GET","PUT","DELETE"])
def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response (serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "DELETE":
        review.delete()
        data = {
            'delete':f'review {review_pk} is deleted',
        }
        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_review(request, movie_pk ):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
