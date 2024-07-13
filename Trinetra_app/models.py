from django.db import models


# Create your models here.
class CareerForm(models.Model):
    # CHOICES = (
    #     ('Project Engineer', 'Project Engineer'),
    #     ('Service Engineer', 'Service Engineer'),
    #     ('Electrician', 'Electrician'),
    #     ('Web Developer', 'Web Developer'),
    #     ('Web Designer', 'Web Designer'),
    #     ('App Developer', 'App Developer'),
    #     ('Digital Marketing', 'Digital Marketing'),
    # )

    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255)
    address = models.TextField(null=False, blank=False)
    address2 = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=10)
    choose_position = models.CharField(max_length=100)
    year_of_experience = models.IntegerField()
    resume = models.FileField(upload_to='uploads/', max_length=255,null=False)
