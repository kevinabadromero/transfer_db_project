import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_rama.settings")
django.setup()
arr_new_topics = []
from app.models import Article, PhpbbAlbum, Answer, topics
articulos = Article.objects.all()
respuestas = Answer.objects.all()
for f in articulos:
    arr_new_topics.append(f.title)


arr_new_topics = list(set(arr_new_topics))

for a in arr_new_topics:
    topics(topic = a)
#first you have to makemigrations, after migrate after run!