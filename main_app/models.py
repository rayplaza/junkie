from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

GRADES = (
    ('M', 'Mint'),
    ('E', 'Excellent'),
    ('VG+', 'Very Good Plus'),
    ('VG', 'Very Good'),
    ('G', 'Good'),
    ('F', 'Fair'),
    ('P', 'Poor')
)

CONDITION = (
    ('E', 'Excellent'),
    ('G', 'Good'),
    ('P', 'Poor')
)

class Record(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    label = models.CharField(max_length=100)
    condition = models.CharField(
        max_length=3,
        choices=GRADES,
        default=GRADES[4][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
    
    def get_absolute_url(self):
        return reverse('records_detail', kwargs={'pk': self.id})

class Comic(models.Model):
    comic_name = models.CharField(max_length=100)
    edition = models.IntegerField()
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    condition = models.CharField(
        max_length=1,
        choices=CONDITION,
        default=GRADES[1][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comic_name
    
    def get_absolute_url(self):
        return reverse('comics_detail', kwargs={'pk': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  record = models.ForeignKey(Record, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for record_id: {self.record_id} @{self.url}"
    