#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[32]:


import pandas as pd


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')


# In[3]:


page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[5]:


tags = soup.find('h3',class_="lister-item-header")


# In[6]:


tags


# In[7]:


tags.text


# In[8]:


tags.text.replace("\n", "",1).split()


# In[9]:


year1 = tags.text.split()[-1][1:-1]


# In[10]:


year1


# In[75]:


main_tags1 = []

for i in soup.find_all('h3',class_="lister-item-header"):
    main_tags1.append(i.text.replace("\n", "",1).split()[1:-1])


# In[76]:


main_tags1


# In[13]:


year1 = []

for i in soup.find_all('h3',class_="lister-item-header"):
    year1.append(i.text.split()[-1][1:-1])


# In[14]:


year1


# In[28]:


rating1 = []

for i in soup.find_all('div',class_="ratings-bar"):
    rating1.append(i.text.replace("\n", "")[0:3])


# In[29]:


rating1


# In[31]:


print(len(main_tags1),len(year1),len(rating1))


# In[34]:


df = pd.DataFrame({'name':main_tags1,'year':year1,'rating':rating1})


# In[35]:


df


# In[ ]:





# In[36]:


page2 = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')


# In[37]:


page2


# In[38]:


soup2 = BeautifulSoup(page2.content)


# In[39]:


soup2


# In[40]:


tags2 = soup2.find('h3',class_="lister-item-header")


# In[41]:


tags2.text.replace("\n", "")


# In[53]:


main_tags2=[]

for i in soup2.find_all('h3',class_="lister-item-header"):
    main_tags2.append(i.text.replace("\n", "",1).split()[1:-1])


# In[54]:


main_tags2


# In[55]:


mainlist = main_tags1 + main_tags2


# In[56]:


print(mainlist)


# In[57]:


year2 = []

for i in soup2.find_all('h3',class_="lister-item-header"):
    year2.append(i.text.split()[-1][1:-1])


# In[58]:


year2


# In[59]:


rating2 = []

for i in soup2.find_all('div',class_="ratings-bar"):
    rating2.append(i.text.replace("\n", "")[0:3])


# In[60]:


rating2


# In[61]:


year = year1 + year2

year


# In[62]:


rating = rating1 + rating2


# In[63]:


data= pd.DataFrame({'Name':mainlist,'year':year,'rating':rating})


# In[64]:


data


# In[ ]:




