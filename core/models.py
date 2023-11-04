from pydoc import describe
from tabnanny import verbose
from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=100,verbose_name = "إسم التخصص")
    short_name = models.CharField(max_length=100,verbose_name = "إختصار الإسم")
    class Meta:
        verbose_name = "تخصص"
        verbose_name_plural = "التخصصات"
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100,verbose_name = "إسم الدورة")
    short_name = models.CharField(max_length=100,verbose_name = "إختصار الإسم")
    description = models.TextField(verbose_name = "وصف الدورة")
    price = models.CharField(max_length=100,verbose_name = "سعر")
    class Meta:
        verbose_name = "دورة"
        verbose_name_plural = "الدورات"
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100,verbose_name = "إسم الحدث")
    image = models.CharField(max_length=100,verbose_name = "الصورة")
    date = models.CharField(max_length=100,verbose_name = "تاريخ الحدث")
    type = models.CharField(max_length=100,verbose_name = "نوع الحدث")
    class Meta:
        verbose_name = "حدث"
        verbose_name_plural = "الأحداث"
    def __str__(self):
        return self.name

