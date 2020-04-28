from django.db import models

# Create your models here.
class Banner(models.Model):
    bg_img = models.ImageField(upload_to='images/')
    small_text= models.CharField(max_length=50)
    large_text= models.CharField(max_length=150)
    def __str__(self):
        return self.small_text

class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/sponsors')
    def __str__(self):
        return self.sponsor_name


class Member(models.Model):
    member_name = models.CharField(max_length=50)
    post = models.CharField(max_length=300)
    insta = models.URLField(default="")
    linkdin = models.URLField(default="")
    member_img = models.ImageField(upload_to='images/members')
    sig_head = models.BooleanField(default=False)
    def __str__(self):
        return self.member_name

class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)
    display_on_index = models.BooleanField()
    def __str__(self):
        return self.alt_text

