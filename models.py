from django.db import models

# Create your models here.
class Person(models.Moddel):
  dob = models.DateField(verbose_name = 'Date Of Birth')
  age = models.PositiveSmallIntegerField()

class Article(models.Model):
  title = models.CharField(maxlength = 120)
  doc = models.DateField(auto_now_add = TRUE, varbose_name = 'Date Of Creation')
  dom = models.DateField(auto_now = TRUE, verbose_name = 'Last modified')
  summary = models.TextField(maxength = 300)
  description = models.TextField()
  source = models.URLField()
  images = models.ImageField(upload_to = 'images/'strftime)
  class Meta:
    ordering = ['title']

class Disease(Article):
  treatment = models.TextField()
  considerations = models.TextField(null = TRUE)
  protection = models.TextField()

class Contraception(Article):
  advantages = models.TextField()
  disadvantages = models.TextField()

class HealthCentre(models.Model):
  telephone = models.CharField(maxlength = 120, null = TRUE)
  fax = models.CharField(maxlength = 120, null = TRUE)
  email = models.EmailField(null = TRUE)
  website = models.URLField(null = TRUE)
  postal_address = models.TextField(maxlength = 300, null = TRUE)
  physical_address = models.Textfield(maxlength = 300, null = TRUE)
  geo_data = models.TextField(null = TRUE)
