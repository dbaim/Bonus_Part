from django.forms import ModelForm
from django import forms
from main_page.models import diseasetype, disease, discover, users, doctor, publicservant, specialize, record, country



class countryForms(forms.ModelForm):
    class Meta:
        model = country
        fields="__all__"


class dtForms(forms.ModelForm):
    class Meta:
        model = diseasetype
        fields="__all__"


class disForms(forms.ModelForm):
    class Meta:
        model = disease
        fields="__all__"


class discForms(forms.ModelForm):
    class Meta:
        model = discover
        fields="__all__"


class userForms(forms.ModelForm):
    class Meta:
        model = users
        fields="__all__"


class docForms(forms.ModelForm):
    class Meta:
        model = doctor
        fields="__all__"


class publicForms(forms.ModelForm):
    class Meta:
        model = publicservant
        fields="__all__"


class specForms(forms.ModelForm):
    class Meta:
        model = specialize
        fields="__all__"


class recForms(forms.ModelForm):
    class Meta:
        model = record
        fields="__all__"







