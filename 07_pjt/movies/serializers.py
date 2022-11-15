from dataclasses import field
from .models import Actor, Movie, Review
from rest_framework import serializers



class MovieSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields=('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies=MovieSerializer1(many=True,)
    class Meta:
        model=Actor
        fields = "__all__"








class MovieSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields=('title','overview',)







class ActorSerializer2(serializers.ModelSerializer):

    class Meta:
        model=Actor
        fields = ("name",)

class ReviewSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields=('title','content',)



class MovieSerializer(serializers.ModelSerializer):
    actors=ActorSerializer2(many=True)
    review_set = ReviewSerializer2(many=True)
    class Meta:
        model = Movie
        fields="__all__"






class MovieSerializer3(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ("title",)




class ReviewSerializer(serializers.ModelSerializer):
    movie=MovieSerializer3(read_only=True) # many true 안써도 됨 영화가 한개니깐
    class Meta:
        model = Review
        fields="__all__"

