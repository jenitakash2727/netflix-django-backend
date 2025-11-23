from django.db import models
from django.contrib.auth.models import User
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

    # Poster fields
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    poster_url = models.URLField(blank=True)  # ✅ ADD EXTERNAL POSTER URL

    # Video fields
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True)  # ✅ ADD EXTERNAL VIDEO URL
    trailer_url = models.URLField(blank=True)

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # ✅ ADD METHOD TO GET VIDEO URL (Priority: external URL > local file)
    def get_video_url(self):
        if self.video_url:
            return self.video_url
        elif self.video_file:
            return self.video_file.url
        return None

    # ✅ ADD METHOD TO GET POSTER URL
    def get_poster_url(self):
        if self.poster_url:
            return self.poster_url
        elif self.poster:
            return self.poster.url
        return None


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'movie']

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"