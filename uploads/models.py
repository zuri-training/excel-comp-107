from django.db import models
import os
from django.conf import settings
# Create your models here.


class ExcelFilePair(models.Model):
    file1 = models.FileField(upload_to='docs/excel/file1', max_length=500)
    file2 = models.FileField(upload_to='docs/excel/file2', max_length=500)

    class Meta:
        db_table = 'Excel File'
    def __str__(self):
        return os.path.basename(self.file1.name) + ' & ' + os.path.basename(self.file2.name)