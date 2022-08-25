from django import forms

class CargaInstrumento(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    tipoinstrumento = forms.CharField()
    color = forms.CharField()

class CargaDisco(forms.Form):
    artista = forms.CharField (max_length = 35)
    album = forms.CharField (max_length = 35)
    fechaLanzamiento = forms.DateField()