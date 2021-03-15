from requests_html import  HTMLSession
import os
from bs4 import BeautifulSoup
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_rama.settings")
django.setup()
from app.models import Article
i = 10
session = HTMLSession()
while i<11:

    i = i+1
    o = str(i)
    
    URL = 'http://www.naczyniaki.pl/viewtopic.php?t='+o
    resp = session.get(URL)
    resp.html.render(timeout=20)
    html = resp.html.html
    soup = BeautifulSoup(html, 'html.parser')
    outresult = soup.find(class_='nav')
    results = soup.find(class_='forumline')
    arr_name = []
    arr_post = []
    arr_nav = []
    arr_navb = []
    arr_navc = []
    arr_quote = []
    arr_owner = []
    clean = 0
    dirty = 0
    
    blocks = results.find_all('span', class_='name')
    for block in blocks:
        
        name=block.text.strip()
        arr_name.append(name)

    posts = results.find_all('td', class_='final')
    for post in posts:
        posta = post.text.strip()
        arr_post.append(posta)

    quote = results.find_all('td', class_='quote')
    if len(quote)>0:
        for h in quote:
            properties = h.text.strip()
            arr_quote.append(properties)
    else:
        arr_quote.append('0')
    
    owner = results.find_all('span', class_='owner')    
    if len(owner)>0:
        for o in owner:
            print (o)
            name_space = o.text.strip()
            arr_owner.append(name_space)
    else:
        arr_owner.append("0")
        
    navs = outresult.find_all('a', class_='category')
    for nav in navs:
        nav_transform = nav.text.strip()
        arr_nav.append(nav_transform)

    navsb = outresult.find_all('a', class_='subcategory')
    for nav in navsb:
        nav_transform = nav.text.strip()
        arr_navb.append(nav_transform)
    
    navsc = outresult.find_all('a', class_='topic')
    for nav in navsc:
        nav_transform = nav.text.strip()
        arr_navc.append(nav_transform)
          
    clean = len(arr_name)
    print(len(arr_quote))
    while dirty < clean:
        r = Article(
            user_name = arr_name[dirty],
            title = arr_navc[0],
            content= arr_post[dirty],
            category=arr_nav[0],
            sub_category= arr_navb[0],)
        r.save()
        dirty = dirty+1



    


    