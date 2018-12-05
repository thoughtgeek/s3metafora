from django.db import models
import os
import random


def randomizer(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(10))
    basefilename = basefilename[:10]
    return '{basename}_{randomstring}{ext}'.format(basename= basefilename, randomstring= randomstr, ext= file_extension)


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=randomizer, null=True)

    # @property
    # def delFile(self):
    #     print('Clicked')
    #     return 'True'
