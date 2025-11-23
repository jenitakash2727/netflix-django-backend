from django.db import models
from django.contrib.auth.models import User  # Add this import
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    LANGUAGE_CHOICES = [
        ('TAMIL', 'Tamil'),
        ('HINDI', 'Hindi'),
        ('ENGLISH', 'English'),
        ('TELUGU', 'Telugu'),
        ('MALAYALAM', 'Malayalam'),
        ('KANNADA', 'Kannada'),
    ]
    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='TAMIL'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    # Video fields
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    trailer_url = models.URLField(blank=True)

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Now User is defined
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'movie']

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"