from django.db import models

class teachers(models.Model):
    email=models.EmailField()
    pas=models.CharField(max_length=20)

    def __str__(self):
        return self.email
