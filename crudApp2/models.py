from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to="images/")
    author = models.CharField(max_length = 30)
    email = models.EmailField()
    describe = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"

