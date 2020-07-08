# How to make migrations
### python manage.py makemigration
# Before make a migrations, you must to create property in the models
# How to migrate the migrations
### python manage.py migration

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug  = models.CharField(max_length = 100)
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add = True)
    # poster = models.ImageField(default = 'default.png', blank = True)
    # author

    def __str__(self):
        return self.title

    # mengembalikan articles.body sepanjang 50 karakter
    def snippet(self):
        return self.body[0:50] + '...'