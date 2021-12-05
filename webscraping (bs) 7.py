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


page = requests.get('https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=RK1,BHK1,BHK2,BHK3,BHK4,BHK4PLUS&searchParam=W3sibGF0IjoxMi44N%20DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8%20iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0&propType=AP,IH,GC,SB')


# In[3]:


page


# In[4]:


soup = BeautifulSoup(page.content)


# In[5]:


headings = soup.find('h2',class_="heading-6 font-semi-bold nb__25Cl7")


# In[6]:


headings.text


# In[7]:


heading = []
for i in soup.find_all('h2',class_="heading-6 font-semi-bold nb__25Cl7"):
    heading.append(i.text)


# In[8]:


heading


# In[9]:


location = []
for i in soup.find_all('div',class_="nb__1EwQz"):
    location.append(i.text)
    
location


# In[10]:


emi = []

for i in soup.find_all('div',class_="nb__3q08s"):
    location.append(i.text)
emi


# In[12]:


emi = soup.find('div',class_="font-semi-bold heading-6")


# In[13]:


emi


# In[ ]:




