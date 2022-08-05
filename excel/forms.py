from django import forms

from excel.models import Document

class DocumentForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields = ('description', 'document', )


class SingleFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
