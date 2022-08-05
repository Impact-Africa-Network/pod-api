# from tokenize import blank_re
from django.db import models

from ian_account.models import User

# Create your models here.

class Connections(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=255,blank=False)
    ld_number=models.CharField(max_length=10, blank=False, unique=True)
    person_met=models.CharField(max_length=255, blank=False)
    date_met=models.DateField()
    meeting_details=models.CharField(max_length=500, blank=False)
    fun_fact=models.CharField(max_length=500,blank=False)
    # owner=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    points=models.IntegerField()

    # class Meta:
    #     ordering=[id]

    def __str__(self):
        return self.ld_number
