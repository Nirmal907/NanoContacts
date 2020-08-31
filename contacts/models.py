from django.db import models

# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.msg_id)
