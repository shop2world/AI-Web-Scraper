from django import forms

class ScraperForm(forms.Form):
    url = forms.URLField(label='Website URL')
    parse_description = forms.CharField(
        label='Describe what you want to parse',
        widget=forms.Textarea(attrs={'rows': 4})
    ) 