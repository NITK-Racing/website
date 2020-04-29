from django.db import models


# Create your models here.
class Banner(models.Model):
    page_to_display = models.IntegerField(default=1)
    bg_img = models.ImageField(upload_to='images/')
    small_text = models.CharField(max_length=50)
    large_text = models.CharField(max_length=150)

    def __str__(self):
        return self.small_text


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/sponsors')

    def __str__(self):
        return self.sponsor_name


# 12345678
class Member(models.Model):
    roll_number = models.CharField(max_length=8, primary_key=True)
    sig = models.IntegerField(default=0)
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


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
