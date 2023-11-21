from email.mime import image
from enum import auto
from pydoc import describe
from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=100,verbose_name = "إسم التخصص")
    short_name = models.CharField(max_length=100,verbose_name = "إختصار الإسم")
    class Meta:
        ordering = ['-id']
        verbose_name = "تخصص"
        verbose_name_plural = "التخصصات"
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100,verbose_name = "إسم الدورة")
    short_name = models.CharField(max_length=100,verbose_name = "إختصار الإسم")
    description = models.TextField(verbose_name = "وصف الدورة")
    price = models.CharField(max_length=100,verbose_name = "السعر")
    class Meta:
        ordering = ['-id']
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
        ordering = ['-id']
        verbose_name = "حدث"
        verbose_name_plural = "الأحداث"
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100,verbose_name = "العنوان")
    link = models.URLField(verbose_name = "اللينك")
    body = models.TextField(verbose_name = "تفاصيل الخبر")
    image  = models.URLField(verbose_name = "لينك صورة الخبر")
    added_date = models.DateField(auto_now_add=True,verbose_name = "تاريخ الاضافة")
    class Meta:
        ordering = ['-id']
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"
    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100,verbose_name = "الاسم")
    description = models.TextField(verbose_name = "الوصف")
    image = models.ImageField(max_length=100,verbose_name = "الصورة",upload_to = 'team/')
    mail = models.EmailField(max_length=100,verbose_name = "البريد الالكتروني")
    facebook = models.URLField(max_length=100,verbose_name = "الفيس بوك")
    youtube = models.URLField(max_length=100,verbose_name = "اليوتيوب")
    class Meta:
        ordering = ['-id']
        verbose_name = "فريق"
        verbose_name_plural = "الفريق"
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100,verbose_name = 'العنوان')
    link = models.URLField(max_length = 200 , verbose_name = 'لينك الفيديو') 
    background_img_link = models.URLField(max_length = 200, verbose_name = 'لينك صورة الفيديو')
    created_at = models.DateField(auto_now = True,verbose_name = 'تاريخ النشر')
    class Meta:
        verbose_name = 'المدونة'
        verbose_name_plural = "المدونات"
    def __str__(self):
        return self.title