from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('lattitude','longtitude','vehicle','datetimeC')
        labels = {
            'longtitude':'Longtitude',
            'lattitude':'Lattitude'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['vehicle'].empty_label = "Select"
        self.fields['lattitude'].required = False
