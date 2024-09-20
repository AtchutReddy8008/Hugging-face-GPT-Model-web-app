from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(
        label='Your Input',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Enter your question here...',
            'class': 'form-control'
        }),
        max_length=500,  # You can set a max length if necessary
        required=True
    )
