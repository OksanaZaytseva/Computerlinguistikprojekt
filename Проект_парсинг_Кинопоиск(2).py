#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


get_ipython().system('pip install fake_useragent')
from fake_useragent import UserAgent
print(UserAgent().chrome)


# In[ ]:


page_link = 'https://www.kinopoisk.ru/film/468522/reviews/'
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})


# In[ ]:


url = 'https://www.kinopoisk.ru/film/468522/reviews/' 
r = requests.get(url) # загружаем страницу по ссылке
print(r.status_code)


# In[ ]:


soup = BeautifulSoup(r.text, features="html.parser")
print(soup.prettify())


# # Отряд самоубийц

# # Bad reviews (264) (выгружены)

# In[ ]:


kinopoisk_url_list_bad = []


for page_b in range(1, 28):
    url_page_bad = f'https://www.kinopoisk.ru/film/468522/reviews/ord/date/status/bad/perpage/10/page/{page_b}/'
    kinopoisk_url_list_bad.append(url_page_bad)
print(kinopoisk_url_list_bad)


# In[ ]:


url_bad = kinopoisk_url_list_bad[26]
url_bad


# In[ ]:


url_bad = kinopoisk_url_list_bad[26]

def review_bad_parsing(url_bad):
    page_bad = requests.get(url_bad)
    soup_bad = BeautifulSoup(page_bad.text, features = 'html.parser')
    review_content_bad = soup_bad.find_all('tbody')
    review_bad = [bad.text for bad in review_content_bad]
    final_review_bad = ' '.join(review_bad)
    return final_review_bad
print(review_bad_parsing(url_bad))


# In[ ]:


from time import sleep

all_reviews_bad = [] # список с отрицательными отзывами

for b in kinopoisk_url_list_bad[:16]:
    try:
        rev_bad = review_bad_parsing(b)
        all_reviews_bad.append(rev_bad)
        sleep (10)
    except:
        print(b) #try, except показывает, какая ссылка ломает парсер


# In[ ]:


all_reviews_bad


# In[ ]:


df_bad = pd.DataFrame(all_reviews_bad)
df_bad


# In[ ]:


df_bad.to_excel('Suicide Squad_all_reviews_bad.xlsx')


# In[ ]:


df_bad.to_csv('Suicide Squad_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# In[ ]:


from time import sleep

all_reviews_bad1 = [] # список с отрицательными отзывами

for b1 in kinopoisk_url_list_bad[16:27]:
    try:
        rev_bad1 = review_bad_parsing(b1)
        all_reviews_bad1.append(rev_bad1)
        sleep (5)
    except:
        print(b1) #try, except показывает, какая ссылка ломает парсер


# In[ ]:


all_reviews_bad1


# In[ ]:


df_bad0 = pd.DataFrame(all_reviews_bad1)
df_bad0


# In[ ]:


df_bad.to_excel('Suicide Squad_all_reviews_bad1.xlsx')


# In[ ]:


df_bad.to_csv('Suicide Squad_all_reviews_bad1.txt', sep='\t', index=False) # для дальнейшей работы


# In[ ]:


with open("joined_rev_squad.txt", 'a', encoding='utf-8') as f0:
    for i in df_bad[0]:
        print(i, file = f0)


# # Good reviews (272) (выгружены)

# In[3]:


kinopoisk_url_list_good = []


for page_g in range(1, 29):
    url_page_good = f'https://www.kinopoisk.ru/film/468522/reviews/ord/date/status/good/perpage/10/page/{page_g}/'
    kinopoisk_url_list_good.append(url_page_good)
print(kinopoisk_url_list_good)


# In[4]:


url_good = kinopoisk_url_list_good[0]

def review_good_parsing(url_good):
    page_good = requests.get(url_good)
    soup_good = BeautifulSoup(page_good.text, features = 'html.parser')
    review_content_good = soup_good.find_all('tbody')
    review_good = [good.text for good in review_content_good]
    final_review_good = ' '.join(review_good)
    return final_review_good
print(review_good_parsing(url_good))


# In[5]:


from time import sleep #мой первоначальный код

all_reviews_good = [] # список с положительными отзывами

for g in kinopoisk_url_list_good[0:15]:
    try:
        rev_good = review_good_parsing(g)
        all_reviews_good.append(rev_good)
        sleep (3)
    except:
        print(g) #try, except показывает, какая ссылка ломает парсер


# In[ ]:


all_reviews_good


# In[6]:


df_good = pd.DataFrame(all_reviews_good)
df_good


# In[8]:


df_good.to_excel('Suicide Squad_all_reviews_good.xlsx')


# In[9]:


df_good.to_csv('Suicide Squad_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# In[10]:


from time import sleep #мой первоначальный код

all_reviews_good1 = [] # список с положительными отзывами

for g in kinopoisk_url_list_good[15:]:
    try:
        rev_good = review_good_parsing(g)
        all_reviews_good1.append(rev_good)
        sleep (3)
    except:
        print(g) #try, except показывает, какая ссылка ломает парсер


# In[11]:


df_good1 = pd.DataFrame(all_reviews_good1)
df_good1


# In[12]:


df_good1.to_excel('Suicide Squad_all_reviews_good1.xlsx')


# In[13]:


df_good1.to_csv('Suicide Squad_all_reviews_good1.txt', sep='\t', index=False) # для дальнейшей работы


# # Повелитель стихий 

# # Bad reviews (329) (выгружены)

# In[4]:


page_link1 = 'https://www.kinopoisk.ru/film/417855/reviews/'
response1 = requests.get(page_link1, headers={'User-Agent': UserAgent().chrome})

url1 = 'https://www.kinopoisk.ru/film/417855/reviews/' 
r1 = requests.get(url1) # загружаем страницу по ссылке
print(r1.status_code)

if r1.status_code == 200:
    soup1 = BeautifulSoup(r1.text, features="html.parser")
    print(soup1.prettify())
else:
    print("ERROR")


# In[4]:


kinopoisk_url_list_bad_air = []


for page_b1 in range(1, 34):
    url_page_bad1 = f'https://www.kinopoisk.ru/film/417855/reviews/ord/date/status/bad/perpage/10/page/{page_b1}/'
    kinopoisk_url_list_bad_air.append(url_page_bad1)
print(kinopoisk_url_list_bad_air)


# In[5]:


url_bad1 = kinopoisk_url_list_bad_air[12]

def review_bad_parsing_air(url_bad1):
    page_bad1 = requests.get(url_bad1)
    soup_bad1 = BeautifulSoup(page_bad1.text, features = 'html.parser')
    review_content_bad1 = soup_bad1.find_all('tbody')
    review_bad1 = [bad1.text for bad1 in review_content_bad1]
    final_review_bad1 = ' '.join(review_bad1)
    return final_review_bad1
print(review_bad_parsing_air(url_bad1))


# In[24]:


from time import sleep

all_reviews_bad_air = [] # список с отрицательными отзывами

for b1 in kinopoisk_url_list_bad_air:
    try:
        rev_bad1 = review_bad_parsing_air(b1)
        all_reviews_bad_air.append(rev_bad1)
        sleep (10)
    except:
        print(b1) #try, except показывает, какая ссылка ломает парсер


# In[ ]:


all_reviews_bad_air


# In[25]:


df_bad_air = pd.DataFrame(all_reviews_bad_air)
df_bad_air


# In[ ]:


df_bad_air.to_excel('Last Airbender_all_reviews_bad.xlsx')


# In[26]:


df_bad_air.to_csv('Last Airbender_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (129)

# In[5]:


kinopoisk_url_list_good_air = []


for page_g1 in range(1, 14):
    url_page_good1 = f'https://www.kinopoisk.ru/film/417855/reviews/ord/date/status/good/perpage/10/page/{page_g1}/'
    kinopoisk_url_list_good_air.append(url_page_good1)
print(kinopoisk_url_list_good_air)


# In[6]:


url_good1 = kinopoisk_url_list_good_air[12]

def review_good_parsing_air(url_good1):
    page_good1 = requests.get(url_good1)
    soup_good1 = BeautifulSoup(page_good1.text, features = 'html.parser')
    review_content_good1 = soup_good1.find_all('tbody')
    review_good1 = [good1.text for good1 in review_content_good1]
    final_review_good1 = ' '.join(review_good1)
    return final_review_good1
print(review_good_parsing_air(url_good1))


# In[7]:


from time import sleep

all_reviews_good_air = [] # список с положительные отзывами

for g1 in kinopoisk_url_list_good_air:
    try:
        rev_good1 = review_good_parsing_air(g1)
        all_reviews_good_air.append(rev_good1)
        sleep (3)
    except:
        print(g1) #try, except показывает, какая ссылка ломает парсер


# In[8]:


df_good_air = pd.DataFrame(all_reviews_good_air)
df_good_air


# In[9]:


df_good_air.to_csv('Last Airbender_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# # Фантастические твари: Преступления Грин-де-Вальда

# # Bad reviews (71) (выгружены)

# In[13]:


page_link2 = 'https://www.kinopoisk.ru/film/843479/reviews/'
response2 = requests.get(page_link2, headers={'User-Agent': UserAgent().chrome})
url2 = 'https://www.kinopoisk.ru/film/843479/reviews/' 

r2 = requests.get(url2) # загружаем страницу по ссылке
#print(r2.status_code)

if r2.status_code == 200:
    soup2 = BeautifulSoup(r2.text, features="html.parser")
    print(soup2.prettify())
else:
    print("ERROR")


# In[14]:


kinopoisk_url_list_bad_creature = []


for page_b2 in range(1, 9):
    url_page_bad2 = f'https://www.kinopoisk.ru/film/843479/reviews/ord/date/status/bad/perpage/10/page/{page_b2}/'
    kinopoisk_url_list_bad_creature.append(url_page_bad2)
print(kinopoisk_url_list_bad_creature)


# In[15]:


url_bad2 = kinopoisk_url_list_bad_creature[3]

def review_bad_parsing_creature(url_bad2):
    page_bad2 = requests.get(url_bad2)
    soup_bad2 = BeautifulSoup(page_bad2.text, features = 'html.parser')
    review_content_bad2 = soup_bad2.find_all('tbody')
    review_bad2 = [bad2.text for bad2 in review_content_bad2]
    final_review_bad2 = ' '.join(review_bad2)
    return final_review_bad2
print(review_bad_parsing_creature(url_bad2))


# In[18]:


from time import sleep

all_reviews_bad_creature = [] # список с положительными отзывами

for b2 in kinopoisk_url_list_bad_creature:
    try:
        rev_bad2 = review_bad_parsing_creature(b2)
        all_reviews_bad_creature.append(rev_bad2)
        sleep (10)
    except:
        print(b2) #try, except показывает, какая ссылка ломает парсер


# In[19]:


df_bad_creature = pd.DataFrame(all_reviews_bad_creature)
df_bad_creature


# In[20]:


df_bad_creature.to_csv('Fantastic_Creature_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (75) (выгружены)

# In[14]:


page_link_2 = 'https://www.kinopoisk.ru/film/843479/reviews/'
response_2 = requests.get(page_link_2, headers={'User-Agent': UserAgent().chrome})
url_2 = 'https://www.kinopoisk.ru/film/843479/reviews/' 

r_2 = requests.get(url_2) # загружаем страницу по ссылке
#print(r_2.status_code)

if r_2.status_code == 200:
    soup_2 = BeautifulSoup(r_2.text, features="html.parser")
    print(soup_2.prettify())
else:
    print("ERROR")


# In[15]:


kinopoisk_url_list_good_creature = []


for page_g2 in range(1, 9):
    url_page_good2 = f'https://www.kinopoisk.ru/film/843479/reviews/ord/date/status/good/perpage/10/page/{page_g2}/'
    kinopoisk_url_list_good_creature.append(url_page_good2)
print(kinopoisk_url_list_good_creature)


# In[16]:


url_good2 = kinopoisk_url_list_good_creature[0]

def review_good_parsing_creature(url_good2):
    page_good2 = requests.get(url_good2)
    soup_good2 = BeautifulSoup(page_good2.text, features = 'html.parser')
    review_content_good2 = soup_good2.find_all('tbody')
    review_good2 = [good2.text for good2 in review_content_good2]
    final_review_good2 = ' '.join(review_good2)
    return final_review_good2
print(review_good_parsing_creature(url_good2))


# In[17]:


from time import sleep

all_reviews_good_creature = [] # список с положительными отзывами

for g2 in kinopoisk_url_list_good_creature:
    try:
        rev_good2 = review_good_parsing_creature(g2)
        all_reviews_good_creature.append(rev_good2)
        sleep (3)
    except:
        print(g2) #try, except показывает, какая ссылка ломает парсер


# In[19]:


df_good_creature = pd.DataFrame(all_reviews_good_creature)
df_good_creature


# In[20]:


df_good_creature.to_csv('Fantastic_Creature_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# # Барби

# # Bad reviews (65) (выгружены)

# In[12]:


page_link3 = 'https://www.kinopoisk.ru/film/478052/reviews/'
response3 = requests.get(page_link3, headers={'User-Agent': UserAgent().chrome})
url3 = 'https://www.kinopoisk.ru/film/478052/reviews/' 

r3 = requests.get(url3) # загружаем страницу по ссылке
#print(r3.status_code)

if r3.status_code == 200:
    soup3 = BeautifulSoup(r3.text, features="html.parser")
    print(soup3.prettify())
else:
    print("ERROR")


# In[15]:


kinopoisk_url_list_bad_barbie = []


for page_b3 in range(1, 8):
    url_page_bad3 = f'https://www.kinopoisk.ru/film/478052/reviews/ord/date/status/bad/perpage/10/page/{page_b3}/'
    kinopoisk_url_list_bad_barbie.append(url_page_bad3)
print(kinopoisk_url_list_bad_barbie)


# In[17]:


url_bad3 = kinopoisk_url_list_bad_barbie[3]

def review_bad_parsing_barbie(url_bad3):
    page_bad3 = requests.get(url_bad3)
    soup_bad3 = BeautifulSoup(page_bad3.text, features = 'html.parser')
    review_content_bad3 = soup_bad3.find_all('tbody')
    review_bad3 = [bad3.text for bad3 in review_content_bad3]
    final_review_bad3 = ' '.join(review_bad3)
    return final_review_bad3
print(review_bad_parsing_barbie(url_bad3))


# In[22]:


from time import sleep

all_reviews_bad_barbie = [] # список с отрицательными отзывами

for b3 in kinopoisk_url_list_bad_barbie:
    try:
        rev_bad3 = review_bad_parsing_barbie(b3)
        all_reviews_bad_barbie.append(rev_bad3)
        sleep (10)
    except:
        print(b3) #try, except показывает, какая ссылка ломает парсер


# In[23]:


df_bad_barbie = pd.DataFrame(all_reviews_bad_barbie)
df_bad_barbie


# In[24]:


df_bad_barbie.to_csv('Barbie_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (56) (выгружены)

# In[21]:


page_link_3 = 'https://www.kinopoisk.ru/film/478052/reviews/'
response_3 = requests.get(page_link_3, headers={'User-Agent': UserAgent().chrome})
url_3 = 'https://www.kinopoisk.ru/film/478052/reviews/' 

r_3 = requests.get(url_3) # загружаем страницу по ссылке
#print(r3.status_code)

if r_3.status_code == 200:
    soup_3 = BeautifulSoup(r_3.text, features="html.parser")
    print(soup_3.prettify())
else:
    print("ERROR")


# In[22]:


kinopoisk_url_list_good_barbie = []


for page_g3 in range(1, 7):
    url_page_good3 = f'https://www.kinopoisk.ru/film/478052/reviews/ord/date/status/good/perpage/10/page/{page_g3}/'
    kinopoisk_url_list_good_barbie.append(url_page_good3)
print(kinopoisk_url_list_good_barbie)


# In[23]:


url_good3 = kinopoisk_url_list_good_barbie[3]

def review_good_parsing_barbie(url_good3):
    page_good3 = requests.get(url_good3)
    soup_good3 = BeautifulSoup(page_good3.text, features = 'html.parser')
    review_content_good3 = soup_good3.find_all('tbody')
    review_good3 = [good3.text for good3 in review_content_good3]
    final_review_good3 = ' '.join(review_good3)
    return final_review_good3
print(review_good_parsing_barbie(url_good3))


# In[25]:


from time import sleep

all_reviews_good_barbie = [] # список с положительными отзывами

for g3 in kinopoisk_url_list_good_barbie:
    try:
        rev_good3 = review_good_parsing_barbie(g3)
        all_reviews_good_barbie.append(rev_good3)
        sleep (3)
    except:
        print(g3) #try, except показывает, какая ссылка ломает парсер


# In[26]:


df_good_barbie = pd.DataFrame(all_reviews_good_barbie)
df_good_barbie


# In[27]:


df_good_barbie.to_csv('Barbie_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# # Охотники за привидениями 2016

# # Bad reviews (79) (выгружены)

# In[21]:


page_link4 = 'https://www.kinopoisk.ru/film/425673/reviews/'
response4 = requests.get(page_link4, headers={'User-Agent': UserAgent().chrome})
url4 = 'https://www.kinopoisk.ru/film/425673/reviews/' 

r4 = requests.get(url4) # загружаем страницу по ссылке
#print(r4.status_code)

if r4.status_code == 200:
    soup4 = BeautifulSoup(r4.text, features="html.parser")
    print(soup4.prettify())
else:
    print("ERROR")


# In[22]:


kinopoisk_url_list_bad_ghost = []


for page_b4 in range(1, 9):
    url_page_bad4 = f'https://www.kinopoisk.ru/film/425673/reviews/ord/date/status/bad/perpage/10/page/{page_b4}/'
    kinopoisk_url_list_bad_ghost.append(url_page_bad4)
print(kinopoisk_url_list_bad_ghost)


# In[23]:


url_bad4 = kinopoisk_url_list_bad_ghost[3]

def review_bad_parsing_ghost(url_bad4):
    page_bad4 = requests.get(url_bad4)
    soup_bad4 = BeautifulSoup(page_bad4.text, features = 'html.parser')
    review_content_bad4 = soup_bad4.find_all('tbody')
    review_bad4 = [bad4.text for bad4 in review_content_bad4]
    final_review_bad4 = ' '.join(review_bad4)
    return final_review_bad4
print(review_bad_parsing_ghost(url_bad4))


# In[24]:


from time import sleep

all_reviews_bad_ghost = [] # список с отрицательными отзывами

for b4 in kinopoisk_url_list_bad_ghost:
    try:
        rev_bad4 = review_bad_parsing_ghost(b4)
        all_reviews_bad_ghost.append(rev_bad4)
        sleep (10)
    except:
        print(b4) #try, except показывает, какая ссылка ломает парсер


# In[25]:


df_bad_ghost = pd.DataFrame(all_reviews_bad_ghost)
df_bad_ghost


# In[26]:


df_bad_ghost.to_csv('Ghostbusters_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (69) (выгружены)

# In[28]:


page_link4 = 'https://www.kinopoisk.ru/film/425673/reviews/'
response4 = requests.get(page_link4, headers={'User-Agent': UserAgent().chrome})
url4 = 'https://www.kinopoisk.ru/film/425673/reviews/' 

r4 = requests.get(url4) # загружаем страницу по ссылке
#print(r4.status_code)

if r4.status_code == 200:
    soup4 = BeautifulSoup(r4.text, features="html.parser")
    print(soup4.prettify())
else:
    print("ERROR")


# In[30]:


kinopoisk_url_list_good_ghost = []


for page_g4 in range(1, 8):
    url_page_good4 = f'https://www.kinopoisk.ru/film/425673/reviews/ord/date/status/good/perpage/10/page/{page_g4}/'
    kinopoisk_url_list_good_ghost.append(url_page_good4)
print(kinopoisk_url_list_good_ghost)


# In[31]:


url_good4 = kinopoisk_url_list_good_ghost[0]

def review_good_parsing_ghost(url_good4):
    page_good4 = requests.get(url_good4)
    soup_good4 = BeautifulSoup(page_good4.text, features = 'html.parser')
    review_content_good4 = soup_good4.find_all('tbody')
    review_good4 = [good4.text for good4 in review_content_good4]
    final_review_good4 = ' '.join(review_good4)
    return final_review_good4
print(review_good_parsing_ghost(url_good4))


# In[32]:


from time import sleep

all_reviews_good_ghost = [] # список с положительными отзывами

for g4 in kinopoisk_url_list_good_ghost:
    try:
        rev_good4 = review_good_parsing_ghost(g4)
        all_reviews_good_ghost.append(rev_good4)
        sleep (3)
    except:
        print(g4) #try, except показывает, какая ссылка ломает парсер


# In[33]:


df_good_ghost = pd.DataFrame(all_reviews_good_ghost)
df_good_ghost


# In[34]:


df_good_ghost.to_csv('Ghostbusters_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# # Муви 43

# # Bad reviews (108) (выгружены)

# In[35]:


page_link5 = 'https://www.kinopoisk.ru/film/432725/reviews/'
response5 = requests.get(page_link5, headers={'User-Agent': UserAgent().chrome})
url5 = 'https://www.kinopoisk.ru/film/432725/reviews/' 

r5 = requests.get(url5) # загружаем страницу по ссылке
#print(r5.status_code)

if r5.status_code == 200:
    soup5 = BeautifulSoup(r5.text, features="html.parser")
    print(soup5.prettify())
else:
    print("ERROR")


# In[13]:


kinopoisk_url_list_bad_movie = []


for page_b5 in range(1, 12):
    url_page_bad5 = f'https://www.kinopoisk.ru/film/432725/reviews/ord/date/status/bad/perpage/10/page/{page_b5}/'
    kinopoisk_url_list_bad_movie.append(url_page_bad5)
print(kinopoisk_url_list_bad_movie)


# In[14]:


url_bad5 = kinopoisk_url_list_bad_movie[3]

def review_bad_parsing_movie(url_bad5):
    page_bad5 = requests.get(url_bad5)
    soup_bad5 = BeautifulSoup(page_bad5.text, features = 'html.parser')
    review_content_bad5 = soup_bad5.find_all('tbody')
    review_bad5 = [bad5.text for bad5 in review_content_bad5]
    final_review_bad5 = ' '.join(review_bad5)
    return final_review_bad5
print(review_bad_parsing_movie(url_bad5))


# In[17]:


from time import sleep

all_reviews_bad_movie = [] # список с отрицательными отзывами

for b5 in kinopoisk_url_list_bad_movie:
    try:
        rev_bad5 = review_bad_parsing_movie(b5)
        all_reviews_bad_movie.append(rev_bad5)
        sleep (10)
    except:
        print(b5) #try, except показывает, какая ссылка ломает парсер


# In[18]:


df_bad_movie = pd.DataFrame(all_reviews_bad_movie)
df_bad_movie


# In[19]:


df_bad_movie.to_csv('Movie43_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (116) (выгружены)

# In[36]:


kinopoisk_url_list_good_movie = []


for page_g5 in range(1, 13):
    url_page_good5 = f'https://www.kinopoisk.ru/film/432725/reviews/ord/date/status/good/perpage/10/page/{page_g5}/'
    kinopoisk_url_list_good_movie.append(url_page_good5)
print(kinopoisk_url_list_good_movie)


# In[37]:


url_good5 = kinopoisk_url_list_good_movie[3]

def review_good_parsing_movie(url_good5):
    page_good5 = requests.get(url_good5)
    soup_good5 = BeautifulSoup(page_good5.text, features = 'html.parser')
    review_content_good5 = soup_good5.find_all('tbody')
    review_good5 = [good5.text for good5 in review_content_good5]
    final_review_good5 = ' '.join(review_good5)
    return final_review_good5
print(review_good_parsing_movie(url_good5))


# In[38]:


from time import sleep

all_reviews_good_movie = [] # список с положительными отзывами

for g5 in kinopoisk_url_list_good_movie:
    try:
        rev_good5 = review_good_parsing_movie(g5)
        all_reviews_good_movie.append(rev_good5)
        sleep (5)
    except:
        print(g5) #try, except показывает, какая ссылка ломает парсер


# In[39]:


df_good_movie = pd.DataFrame(all_reviews_good_movie)
df_good_movie


# In[40]:


df_good_movie.to_csv('Movie43_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы


# # 50 оттенков серого

# # Bad reviews (267) (выгружены)

# In[41]:


page_link6 = 'https://www.kinopoisk.ru/film/688832/reviews/'
response6 = requests.get(page_link6, headers={'User-Agent': UserAgent().chrome})
url6 = 'https://www.kinopoisk.ru/film/688832/reviews/' 

r6 = requests.get(url6) # загружаем страницу по ссылке
#print(r6.status_code)

if r6.status_code == 200:
    soup6 = BeautifulSoup(r6.text, features="html.parser")
    print(soup6.prettify())
else:
    print("ERROR")


# In[28]:


kinopoisk_url_list_bad_shades = []


for page_b6 in range(1, 28):
    url_page_bad6 = f'https://www.kinopoisk.ru/film/688832/reviews/ord/date/status/bad/perpage/10/page/{page_b6}/'
    kinopoisk_url_list_bad_shades.append(url_page_bad6)
print(kinopoisk_url_list_bad_shades)


# In[29]:


url_bad6 = kinopoisk_url_list_bad_shades[0]

def review_bad_parsing_shades(url_bad6):
    page_bad6 = requests.get(url_bad6)
    soup_bad6 = BeautifulSoup(page_bad6.text, features = 'html.parser')
    review_content_bad6 = soup_bad6.find_all('tbody')
    review_bad6 = [bad6.text for bad6 in review_content_bad6]
    final_review_bad6 = ' '.join(review_bad6)
    return final_review_bad6
print(review_bad_parsing_shades(url_bad6))


# In[30]:


from time import sleep

all_reviews_bad_shades = [] # список с отрицательными отзывами

for b6 in kinopoisk_url_list_bad_shades:
    try:
        rev_bad6 = review_bad_parsing_shades(b6)
        all_reviews_bad_shades.append(rev_bad6)
        sleep (5)
    except:
        print(b6) #try, except показывает, какая ссылка ломает парсер


# In[31]:


df_bad_shades = pd.DataFrame(all_reviews_bad_shades)
df_bad_shades


# In[32]:


df_bad_shades.to_csv('Shades_all_reviews_bad.txt', sep='\t', index=False) # для дальнейшей работы


# # Good reviews (191) выгружены

# In[42]:


kinopoisk_url_list_good_shades = []


for page_g6 in range(1, 21):
    url_page_good6 = f'https://www.kinopoisk.ru/film/688832/reviews/ord/date/status/good/perpage/10/page/{page_g6}/'
    kinopoisk_url_list_good_shades.append(url_page_good6)
print(kinopoisk_url_list_good_shades)


# In[43]:


url_good6 = kinopoisk_url_list_good_shades[0]

def review_good_parsing_shades(url_good6):
    page_good6 = requests.get(url_good6)
    soup_good6 = BeautifulSoup(page_good6.text, features = 'html.parser')
    review_content_good6 = soup_good6.find_all('tbody')
    review_good6 = [good6.text for good6 in review_content_good6]
    final_review_good6 = ' '.join(review_good6)
    return final_review_good6
print(review_good_parsing_shades(url_good6))


# In[44]:


from time import sleep

all_reviews_good_shades = [] # список с положительными отзывами

for g6 in kinopoisk_url_list_good_shades:
    try:
        rev_good6 = review_good_parsing_shades(g6)
        all_reviews_good_shades.append(rev_good6)
        sleep (5)
    except:
        print(g6) #try, except показывает, какая ссылка ломает парсер


# In[45]:


df_good_shades = pd.DataFrame(all_reviews_good_shades)
df_good_shades


# In[46]:


df_good_shades.to_csv('Shades_all_reviews_good.txt', sep='\t', index=False) # для дальнейшей работы

