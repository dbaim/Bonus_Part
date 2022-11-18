from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def main(request):
    show_country = models.country.objects.all()
    show_disease_type = models.diseasetype.objects.all()
    show_disease = models.disease.objects.all()
    show_discover = models.discover.objects.all()
    show_users = models.users.objects.all()
    show_doctor = models.doctor.objects.all()
    show_publicservant = models.publicservant.objects.all()
    show_record = models.record.objects.all()
    show_specialize = models.specialize.objects.all()

    return render(request, 'main_page.html', {"country": show_country, "disease_type": show_disease_type, "disease": show_disease, "discover": show_discover, "users": show_users, "doctor": show_doctor, "publicservant": show_publicservant, "record": show_record, "specialize": show_specialize})


def insert1(request):
    if request.method == "POST":
        if request.POST.get('cname') and request.POST.get('population'):
            saverecord = models.country()
            saverecord.cname = request.POST.get('cname')
            saverecord.population = request.POST.get('population')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'country_insert.html')
    else:
        return render(request, 'country_insert.html')


def insert2(request):
    if request.method == "POST":
        if request.POST.get('id') and request.POST.get('description'):
            saverecord = models.diseasetype()
            saverecord.id = request.POST.get('id')
            saverecord.description = request.POST.get('description')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'dt_insert.html')
    else:
        return render(request, 'dt_insert.html')


def insert3(request):
    if request.method == "POST":
        if request.POST.get('disease_code') and request.POST.get('pathogen') and request.POST.get('description') and request.POST.get('id'):
            saverecord = models.disease()
            saverecord1 = models.diseasetype()
            saverecord.disease_code = request.POST.get('disease_code')
            saverecord.pathogen = request.POST.get('pathogen')
            saverecord.description = request.POST.get('description')
            saverecord1.id = request.POST.get('id')
            saverecord.id = request.POST.get('id')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'dis_insert.html')
    else:
        return render(request, 'dis_insert.html')


def insert4(request):
    if request.method == "POST":
        if request.POST.get('cname') and request.POST.get('disease_code') and request.POST.get('first_enc_date'):
            saverecord = models.discover()
            saverecord.cname = request.POST.get('cname')
            saverecord.disease_code = request.POST.get('disease_code')
            saverecord.first_enc_date = request.POST.get('first_enc_date')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'discovery_insert.html')
    else:
        return render(request, 'discovery_insert.html')


def insert5(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('surname') and request.POST.get('salary') and request.POST.get('phone') and request.POST.get('cname'):
            saverecord = models.users()
            saverecord.email = request.POST.get('email')
            saverecord.name = request.POST.get('name')
            saverecord.surname = request.POST.get('salary')
            saverecord.phone = request.POST.get('phone')
            saverecord.cname = request.POST.get('cname')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'users_insert.html')
    else:
        return render(request, 'users_insert.html')


def insert6(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('degree'):
            saverecord = models.doctor()
            saverecord.email = request.POST.get('email')
            saverecord.degree = request.POST.get('degree')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'doctor_insert.html')
    else:
        return render(request, 'doctor_insert.html')


def insert7(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('degree'):
            saverecord = models.publicservant()
            saverecord.email = request.POST.get('email')
            saverecord.department = request.POST.get('department')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'publicservant_insert.html')
    else:
        return render(request, 'publicservant_insert.html')


def insert8(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('cname') and request.POST.get('disease_code') and request.POST.get('total_deaths') and request.POST.get('total_patients'):
            saverecord = models.record()
            saverecord.email = request.POST.get('email')
            saverecord.cname = request.POST.get('cname')
            saverecord.disease_code = request.POST.get('disease_code')
            saverecord.total_deaths = request.POST.get('total_deaths')
            saverecord.total_patients = request.POST.get('total_patients')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'record_insert.html')
    else:
        return render(request, 'record_insert.html')


def insert9(request):
    if request.method == "POST":
        if request.POST.get('id') and request.POST.get('email'):
            saverecord = models.specialize()
            saverecord.email = request.POST.get('email')
            saverecord.id = request.POST.get('id')
            saverecord.save()
            messages.success(request, 'Saved successfully!')
            return render(request, 'specialize_insert.html')
    else:
        return render(request, 'specialize_insert.html')


def edit(request):
    return 0


def delete1(request, cname):
    deleterecord = models.country.objects.get(cname=cname)
    deleterecord.delete()
    return render(request, "delete.html")


def delete2(request, id):
    deleterecord = models.diseasetype.objects.get(id=id)
    deleterecord.delete()
    return render(request, "delete.html")


def delete3(request, disease_code):
    deleterecord = models.disease.objects.get(disease_code=disease_code)
    deleterecord.delete()
    return render(request, "delete.html")


def delete4(request, disease_code):
    deleterecord = models.discover.objects.get(disease_code=disease_code)
    deleterecord.delete()
    return render(request, "delete.html")


def delete5(request, email):
    deleterecord = models.users.objects.get(email=email)
    deleterecord.delete()
    return render(request, "delete.html")


def delete6(request, email):
    deleterecord = models.doctor.objects.get(email=email)
    deleterecord.delete()
    return render(request, "delete.html")


def delete7(request, email):
    deleterecord = models.publicservant.objects.get(email=email)
    deleterecord.delete()
    return render(request, "delete.html")


def delete8(request, email):
    deleterecord = models.record.objects.get(email=email)
    deleterecord.delete()
    return render(request, "delete.html")


def delete9(request, email):
    deleterecord = models.specialize.objects.get(email=email)
    deleterecord.delete()
    return render(request, "delete.html")



