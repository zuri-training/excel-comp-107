from django import forms
from .models import ExcelFilePair


class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFilePair
        fields = ['file1', 'file2']
        labels = {'file1': 'First File',
                  'file2': 'Second File'
                  }

    def __init__(self, *args, **kwargs):
        super(ExcelFileForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['file1'].widget.attrs['style'] = 'width:240px; height:35px;'
        self.fields['file2'].widget.attrs['style'] = 'width:240px; height:35px;'
