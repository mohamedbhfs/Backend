from django import forms

class RepensesFormulaireForm(forms.Form):
    file=forms.FileField()
    Id_visite=forms.IntegerField()