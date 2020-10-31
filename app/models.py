from django.db import models

# Create your models here.
class Name(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 10)
    class Meta:
        db_table = "Name"