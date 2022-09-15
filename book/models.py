from django.db import models


# Create your models here.

class BookModel(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.CharField(max_length=230)

    price = models.IntegerField()


def __str__(self):
    return "Book Name={0}, subject={1},price={2} ".format(self.bookname, self)
