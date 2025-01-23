from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)