from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno=forms.IntegerField()
    email = forms.EmailField()
    # password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    # rpassword = forms.CharField(label='Enter Password (Again)', widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)


    def clean(self):
        print('totalform validation ')
        total_cleaned_data = super().clean()

        print('Validating Name')
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 's':
            error_message='Name should starts with s '
            raise forms.ValidationError(error_message)
        
        print('Validating rollno')
        inputrollno = total_cleaned_data['rollno']
        if inputrollno <= 0:
            error_message='Rollno should be > 0'
            raise forms.ValidationError(error_message)
        
        print('Validating email')
        inputemail = total_cleaned_data['email']
        if inputemail[-10:] != '@gmail.com':
            error_message='Email extension should be gmail'
            raise forms.ValidationError(error_message)
        
        #for password verification...
        # pwd = total_cleaned_data['password']
        # rpwd = total_cleaned_data['rpassword']
        # if pwd != rpwd:
        #     error_message='please enter the same password '
        #     raise forms.ValidationError(error_message)
        
        # prevent request from BOT....

        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            error_message='Request from BOT can not submiitted'
            raise forms.ValidationError(error_message)

        return total_cleaned_data





