from django.db import models

from ian_account.models import User

# category choices 
categories=(
    ('Finance','Finance'),
    ('Legal','Legal'),
    ('Marketing','Marketing'),
    ('Sales','Sales'),
    ('Social Media','Social Media'),
    ('Design','Design'),
    ('Product','Product'),
    ('Leadership','Leadership'),
    ('Mindset','Mindset'),
    ('Communication & Story Telling','Communication & Story Telling'),
    ('Culture','Culture'),
    ('OKRS','OKRS'),
    ('General','General'),
)
# Create your models here.
class Podcasts(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=255,blank=False)
    ld_number=models.CharField(max_length=10, blank=False)
    date_listened=models.DateField()
    podcast_name=models.CharField(max_length=255, blank=False)
    podcast_link=models.CharField(max_length=500,blank=False, unique=True)
    podcast_category=models.CharField(max_length=500,choices=categories,default="General")
    podcast_group=models.CharField(max_length=255,blank=False)
    podcast_notes=models.CharField(max_length=1024,blank=False)
    # owner=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    points=models.IntegerField()


    # class Meta:
    #     ordering=[id]

    def __str__(self):
        return self.podcast_name