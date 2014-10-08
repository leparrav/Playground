from django.db import models

class Job(models.Model):
    role = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    company_url = models.URLField()
    pic1 = models.ImageField(upload_to="images/")
    pic2 = models.ImageField(upload_to="images/")
    pic3 = models.ImageField(upload_to="images/")