from django import forms


class MotivateMeForm(forms.Form):
    pass


class ChatBotForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
