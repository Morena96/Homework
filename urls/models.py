from django.db import models

class Url(models.Model):
    url        = models.CharField(max_length = 200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = "Urls"