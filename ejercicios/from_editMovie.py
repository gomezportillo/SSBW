from django import forms

class EditForm(forms.Form):

    title = forms.CharField(max_length=100)
    year = forms.IntegerField()
    director = forms.CharField(max_length=100)
    plot = forms.CharField(widget=forms.Textarea)
