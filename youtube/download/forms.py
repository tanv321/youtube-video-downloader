from django import forms
class HomeForm(forms.Form):
    textInput1 = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }

    ))

    class Meta:
        fields = {'textInput1',} 