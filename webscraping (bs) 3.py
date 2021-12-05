#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[4]:


soup = BeautifulSoup(page.content)


# In[5]:


soup


# In[6]:


name= soup.find('td',class_="titleColumn")


# In[7]:


name


# In[9]:


name.text.replace("\n", "",1)[15:-8]


# In[37]:


names = []

for i in soup.find_all('td',class_="titleColumn"):
    names.append(i.text.replace("\n", "",1)[15:-8])


# In[67]:


movie_name = names[0:100]


# In[68]:


movie_name


# In[45]:


rating = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.replace("\n", ""))


# In[65]:


ratings = rating[0:100]


# In[66]:


ratings


# In[51]:


year = []

for i in soup.find_all('span',class_="secondaryInfo"):
    year.append(i.text[1:-1])


# In[63]:


years = year[0:100]


# In[64]:


years


# In[69]:


print(len(movie_name),len(ratings),len(years))


# In[72]:


data= pd.DataFrame({'Name':movie_name,'year':years,'rating':ratings})


# In[73]:


data


# In[ ]:




