from tokenize import blank_re
from django.db import models

# Create your models here.

class Connections(models.Model):
    id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=255,blank=True)
    ld_number=models.CharField(max_lenth=10, blank=True, unique=True)
    person_met=models.CharField(max_length=255, blank=True)
    date_met=models.DateField()
    meeting_details=models.CharField(max_length=500, blank=True)
    fun_fact=models.CharField(max_length=500)
    points=models.IntegerField(max_length=100)

    class Meta:
        ordering=[id]

    def __str__(self):
        return self.ld_number
