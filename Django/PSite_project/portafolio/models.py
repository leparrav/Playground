from django.db import models

class Job(models.Model):
    # URL mapping is 'job/company_name/role'
    role = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    company_url = models.URLField()
    location = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    pic1 = models.ImageField(upload_to="job_images")
    pic2 = models.ImageField(upload_to="job_images")
    pic3 = models.ImageField(upload_to="job_images")

    def __unicode__(self):
        return self.role

class Course(models.Model):
    # URL mapping is 'courses/institution/name'
    name = models.CharField(max_length=128)
    institution = models.CharField(max_length=128)
    course_url = models.URLField()
    materials_url = models.URLField(blank=True)
    end_date = models.DateField()
    pic1 = models.ImageField(upload_to="courses_images")
    pic2 = models.ImageField(upload_to="courses_images")
    description = models.TextField()

    def __unicode__(self):
        return self.name