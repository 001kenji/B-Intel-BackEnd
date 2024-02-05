from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField()
    pass_code = models.CharField(max_length=100,null=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.email}"


    