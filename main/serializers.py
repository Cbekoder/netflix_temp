from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Movie, Actor

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
        # fields = ["name", "country", "birth_year", "gender", "is_alive",]

    def validate_gender(self, value):
        if value not in ["male", "female"]:
            raise ValidationError("Gender must be 'male' or 'female'.")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Actor name must be at least 3 characters long.")
        return value


class MovieModelSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"




class MovieGetModelSerializer(ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = "__all__"
