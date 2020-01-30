from django.db import models


# Create your models here.

class ShortedUrls(models.Model):
    main_url = models.URLField()
    slug = models.CharField(max_length=16)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return f'<URL id={self.pk} slug={self.slug} >'
