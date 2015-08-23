from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Person, Article, Disease, Contraceptive, Product, HealthCentre, 

# Index view
class IndexView (generic.ListView):
  template_name = 'igirl/index.html'
  context_object_name = 'best_articles_list'
  def get_average_ratings(self):
     r = Article.objects.annotate('average_rating' = Sum(Avg('positive_votes'), Avg('negative_votes'))/2)
     return r
  def get_queryset(self):
    """Return the twenty highest rated articles"""
    average_ratings_list = Article.get_average_ratings().order_by('average_rating')[:20]
    return average_ratings_list

# Article view
class ArticleView (generic.DetailView):
  model = Article
  template_name = 'igirl/article.html'
  def get_queryset(self):
    """Return all articles."""
    return Article.objects.all

# Disease view
class DiseaseView (generic.DetailView):
  model = Disease
  template_name = 'igirl/disease.html'
  def get_queryset(self):
    """Return all diseases."""
    return Disease.objects.all

# Contraceptive view
class ContraceptiveView (generic.DetailView):
  model = Contraceptive
  template_name = 'igirl/contraceptive.html'
  def get_queryset(self):
    """Return all contraceptives."""
    return Contraceptive.objects.all

# Product view
class ProductView (generic.DetailView):
  model = Product
  template_name = 'igirl/product.html'
  def get_queryset(self):
    """Return all products."""
    return Product.objects.all

# HealthCentre view
class HealthCentreView (generic.DetailView):
  model = HealthCentre
  template_name = 'igirl/healthcentre.html'
  def get_queryset(self):
    """Return all products."""
    return HealthCentre.objects.all

# Person view
class PersonView (generic.DetailView):
  model = Person
  template_name = 'igirl/person.html'
  def get_queryset(self):
    """Return all products."""
    return Person.objects.all