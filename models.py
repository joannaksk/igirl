from django.db import models
from django.db.models import Max, Sum, Count, Avg

# Create your models here.
class Person(models.Model):
  dob = models.DateField(verbose_name = 'Date Of Birth')
  age = models.PositiveSmallIntegerField()

class Article(models.Model):
  title = models.CharField(max_length = 120)
  doc = models.DateField(auto_now_add = 'TRUE', verbose_name = 'Date Of Creation')
  dom = models.DateField(auto_now = 'TRUE', verbose_name = 'Last modified')
  summary = models.CharField(max_length = 300)
  description = models.CharField(max_length = 1200)
  source = models.URLField()
  images = models.ImageField(upload_to = 'images/%D')
  positive_votes = models.IntegerField(default = 0)
  negative_votes = models.IntegerField(default = 0)
  def __str__(self):
    return self.title
  def get_positive_votes(self):
    return self.positive_votes
  def get_negative_votes(self):
    return self.negative_votes
  class Meta:
    ordering = ['title']

class Disease(Article):
  treatment = models.CharField(max_length = 1200)
  considerations = models.CharField(max_length = 1200, null = 'TRUE')
  protection = models.CharField(max_length = 1200)

class Contraceptive(Article):
  advantages = models.CharField(max_length = 1200)
  disadvantages = models.CharField(max_length = 1200)

class Product(Article):
  type = models.ForeignKey(Contraceptive)

class HealthCentre(models.Model):
  name =  models.CharField(max_length = 120)
  telephone = models.CharField(max_length = 120, null = 'TRUE')
  fax = models.CharField(max_length = 120, null = 'TRUE')
  email = models.EmailField(null = 'TRUE')
  website = models.URLField(null = 'TRUE')
  postal_address = models.CharField(max_length = 300, null = 'TRUE')
  physical_address = models.CharField(max_length = 300, null = 'TRUE')
  geo_data = models.CharField(max_length = 1200, null = 'TRUE')
  district = models.CharField(max_length = 60)
  # def get_total_healthcentres_per_district():
  #   q = HealthCentre.objects.values('district').annotate('number_of_healthcentres' = Count('name'))
  #   return q
  # def get_average_number_of_heathcentres():
  #   q = HealthCentre.objects.values('district').annotate('number_of_healthcentres' = Count('name')).aggregate(Avg('number_of_heatlhcentres'))
  class Meta:
    ordering = ['name']
