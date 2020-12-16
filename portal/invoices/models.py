from django.db import models


class InvoicesList(models.Model):
    DocumentId = models.TextField()
    SiteId = models.TextField()
    DocumentNumber = models.CharField(max_length=200)
    DocumentDate = models.DateTimeField(auto_now_add=True)
    DocumentTypeId = models.TextField()


def __str__(self):
    return self.title
