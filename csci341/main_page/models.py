from django.db import models


class diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = "diseasetype"


class country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "country"


class disease(models.Model):
    disease_code = models.CharField(max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    models.ForeignKey(diseasetype, default=None, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "disease"


class discover(models.Model):
    cname = models.OneToOneField(country, models.DO_NOTHING, db_column='cname', primary_key=True)
    id = models.OneToOneField(diseasetype, models.DO_NOTHING, db_column='id')
    first_enc_date = models.DateField()

    class Meta:
        managed = False
        db_table = "discover"


class users(models.Model):
    email = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    models.ForeignKey(country, on_delete=models.CASCADE)

    class Meta:
        db_table = "users"


class doctor(models.Model):
    email = models.ForeignKey(users, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20)

    class Meta:
        db_table = "doctor"


class publicservant(models.Model):
    email = models.ForeignKey(users, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    class Meta:
        db_table = "publicservant"


class record(models.Model):
    email = models.ForeignKey(users, on_delete=models.CASCADE)
    cname = models.ForeignKey(country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        db_table = "record"


class specialize(models.Model):
    models.ForeignKey(diseasetype, default=None, on_delete=models.CASCADE, primary_key=True)
    email = models.ForeignKey(users, on_delete=models.CASCADE)

    class Meta:
        db_table = "specialize"
