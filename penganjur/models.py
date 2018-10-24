from django.db import models


# Create your models here.
class Aktiviti(models.Model):
	tajuk = models.CharField('Tajuk',blank=False,null=False,max_length=255)
	tempat = models.CharField('Tempat',blank=False,null=False,max_length=255)
	penceramah = models.CharField('Penceramah',blank=False,null=False,max_length=255)
	hadpeserta = models.CharField('Had Peserta',blank=False,null=False,max_length=255)
	
	def __str__(self):
		return str(self.pk)	
