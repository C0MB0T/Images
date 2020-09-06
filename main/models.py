from django.db import models


class SetImage(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


def path(instance, filename):
    return f'{instance.setImg.id}/{filename}'


class Image(models.Model):
    img = models.ImageField(upload_to=path)

    setImg = models.ForeignKey(SetImage, on_delete=models.CASCADE, verbose_name="imgs")
