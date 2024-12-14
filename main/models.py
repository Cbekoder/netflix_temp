from django.db import models

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=4)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_alive = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    producer = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


