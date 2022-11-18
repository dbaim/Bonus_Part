from django.db import models


class country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

    class Meta:
        db_table = "country"


class diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    class Meta:
        db_table = "diseasetype"


class disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(diseasetype, db_column='id', default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = "disease"


class discover(models.Model):
    cname = models.ForeignKey(country, db_column='cname', on_delete=models.CASCADE)
    disease_code = models.OneToOneField(disease, db_column='disease_code', on_delete=models.CASCADE, primary_key=True)
    first_enc_date = models.DateField()

    class Meta:
        db_table = "discover"


class users(models.Model):
    email = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(country, db_column='cname', on_delete=models.CASCADE)

    class Meta:
        db_table = "users"


class doctor(models.Model):
    email = models.ForeignKey(users, db_column='email', on_delete=models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=20)

    class Meta:
        db_table = "doctor"


class publicservant(models.Model):
    email = models.ForeignKey(users, db_column='email', on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)

    class Meta:
        db_table = "publicservant"


class record(models.Model):
    email = models.ForeignKey(users, db_column='email', on_delete=models.CASCADE, primary_key=True)
    cname = models.OneToOneField(country, db_column='cname', on_delete=models.CASCADE)
    disease_code = models.OneToOneField(disease, db_column='disease_code', on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        db_table = "record"


class specialize(models.Model):
    id = models.ForeignKey(diseasetype, db_column='id', default=None, on_delete=models.CASCADE)
    email = models.OneToOneField(users, db_column='email', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = "specialize"
