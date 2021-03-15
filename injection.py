import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_rama.settings")
django.setup()

from app.models import Article, PhpbbAlbum
articulos = Article.objects.all()
for f in articulos:
    f.delete()
    print(f.user_name)
