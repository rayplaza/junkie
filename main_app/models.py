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

    def __srr__(self):
        return self.album_name
    
    def get_absolutle_url(self):
        return reverse('records_detail', kwargs={'pk': self.id})

    