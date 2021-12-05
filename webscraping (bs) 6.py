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


page = 1
headings = []
while page != 18:
    url = f"https://coreyms.com/page/{page}"
    request = requests.get(url)
    soup=BeautifulSoup(request.content)
    for i in soup.find_all('header',class_="entry-header"):
        headings.append(i.text.replace('\n','').split()[:-9])
    page = page + 1


# In[3]:


headings


# In[4]:


page = 1
date = []
while page != 18:
    url = f"https://coreyms.com/page/{page}"
    request = requests.get(url)
    soup=BeautifulSoup(request.content)
    for i in soup.find_all('time',class_="entry-time"):
        date.append(i.text)
    page = page + 1


# In[5]:


date


# In[6]:


page = 1
content = []
while page != 18:
    url = f"https://coreyms.com/page/{page}"
    request = requests.get(url)
    soup=BeautifulSoup(request.content)
    for i in soup.find_all('div',class_="entry-content"):
        content.append(i.text.replace('\n',''))
    page = page + 1


# In[7]:


content


# In[3]:


page = 1
link = []
while page != 18:
    url = f"https://coreyms.com/page/{page}"
    request = requests.get(url)
    soup=BeautifulSoup(request.content)
    for i in soup.find_all('a',class_="ytp-title-text"):
        link.append(mp4['src'])
    page = page + 1


# In[4]:


link


# In[23]:


r  = requests.get("https://coreyms.com/")

soup = BeautifulSoup(r.read(), 'lxml')

links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))


# In[ ]:





# In[16]:


print(len(headings),len(date),len(content))


# In[17]:


data = pd.DataFrame({'Heads':headings,'date':date,'content':content})
data


# In[ ]:




