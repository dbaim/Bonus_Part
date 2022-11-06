from django.shortcuts import render
from django.http import HttpResponse
from . import models


def main(request):
    show_country = models.country.objects.all()
    show_disease_type = models.diseasetype.objects.all()
    show_disease = models.disease.objects.all()
    return render(request, 'main_page.html', {"country": show_country, "disease_type": show_disease_type, "disease": show_disease})


def insert(request):
    return 0


def edit(request):
    return 0


def delete(request):
    return 0
