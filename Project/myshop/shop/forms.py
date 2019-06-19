from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True, max_length=30 )
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'field4'}), required=True)

class EnquiryForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True, max_length=30 )
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'field4'}), required=True)
    options = (('a','a'),
               ('b','b'),
               ('c','c'),
               ('d','d'),)
    picked = forms.MultipleChoiceField(choices=options, widget=forms.CheckboxSelectMultiple())
