#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


tags = soup.find('span',class_="mw-headline")


# In[8]:


tags


# In[9]:


tag = []
for i in soup.find_all('span',class_="mw-headline"):
    tag.append(i.text)


# In[10]:


tag


# In[ ]:




