from django.db import models


class Article(models.Model):
    user_name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField()
    category = models.CharField(max_length=200, blank=True)
    sub_category = models.CharField(max_length=200, blank=True)

class Answer(models.Model):
    owner = models.TextField()
    quote = models.TextField()
    anspost = models.TextField()
    title = models.TextField()
    category = models.TextField()
    sub_category = models.TextField()

class topics(models.Model):
    topic = models.TextField()
#makemigrations >>>> migrate
class PhpbbAlbum(models.Model):
    pic_id = models.AutoField(primary_key=True)
    pic_filename = models.CharField(max_length=255)
    pic_thumbnail = models.CharField(max_length=255, blank=True, null=True)
    pic_title = models.CharField(max_length=255)
    pic_username = models.CharField(max_length=32, blank=True, null=True)
    pic_cat_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb_album'


class PhpbbAlbumCat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=255)
    cat_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phpbb_album_cat'
