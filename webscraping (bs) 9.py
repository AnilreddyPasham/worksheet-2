#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


page = requests.get('https://en.tutiempo.net/delhi.html?data=last-24-hours')


# In[4]:


page


# In[4]:


soup = BeautifulSoup(page.content)


# In[26]:


time=pd.timedelta_range(21, periods=48, freq="0H30T")


# In[28]:


time


# In[33]:


hour = []

for i in soup.find_all('th',class_="thHora"):
    hour.append(i.text)


# In[34]:


hour


# In[ ]:


temp = []

for i in soup.

