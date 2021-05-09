from django import forms
class student(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    marks=forms.FloatField()