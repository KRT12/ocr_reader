from django import forms

from user.models import User, FileUpload


class UserForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                          input_formats=('%d/%m/%Y',))

    class Meta:
        model = User
        fields = ('name', 'fathers_name', 'dob', 'pan_image', 'pan_number')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('file',)
