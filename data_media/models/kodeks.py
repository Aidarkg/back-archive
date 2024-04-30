from django.db import models

class KODEKS(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdf_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



