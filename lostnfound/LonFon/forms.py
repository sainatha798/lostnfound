from django.forms import ModelForm
from django import forms
from . import models
from lostnfound.settings import DATE_INPUT_FORMATS
class Add(ModelForm):
    lost_or_found = forms.ChoiceField(required=True,label='Lost/Found',choices=(('Lost','Lost'),('Found','Found')))
    date = forms.DateField(required=True,widget=forms.DateInput(format="%dd/%mm/%yyyy"))
    subject = forms.CharField(required=False,max_length=200)
    description = forms.CharField(required=False,max_length=2000)
    location = forms.CharField(max_length=50)
    image = forms.FileField(required=False)

    class Meta:
        model = models.LostAndFound
        fields = ['lost_or_found','date','contact_id','subject','description','location','image']

class Search(forms.Form):
    date = forms.DateField(required=False,widget=forms.DateInput(format="%dd/%mm/%yyyy"))
    subject = forms.CharField(required=False,max_length=200)
    lost_or_found = forms.ChoiceField(required=False,label='Lost/Found',choices=(('Lost','Lost'),('Found','Found')))
    location = forms.CharField(required=False,max_length=100)