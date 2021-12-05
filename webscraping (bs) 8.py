#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[3]:


page


# In[4]:


soup = BeautifulSoup(page.content)


# In[18]:


name = []

for i in soup.find_all('div',class_="restnt-info cursor"):
    name.append(i.text.split(',')[0])
name


# In[19]:


location = []
for i in soup.find_all('div',class_="restnt-info cursor"):
    location.append(i.text.split(',')[1:])
location


# In[21]:


cuisine = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
cuisine


# In[22]:


rating = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[24]:


image = []
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
image


# In[25]:


data = pd.DataFrame({'name':name,'cuisine':cuisine,'location':location,'rating':rating,'image':image})


# In[26]:


data


# In[ ]:




