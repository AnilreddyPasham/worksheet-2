#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[5]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[6]:


page


# In[7]:


soup=BeautifulSoup(page.content)


# In[10]:


teams = []
for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)
teams


# In[42]:


team = teams[0:10]
team


# In[13]:


banner = soup.find('td',class_="rankings-block__banner--matches")
top = banner.text
top


# In[15]:


topp = soup.find('td',class_="rankings-block__banner--points")
top_point= topp.text
top_point


# In[14]:


matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches.append(i.text)
matches


# In[18]:


match = [top] + matches[0:18:2]
match


# In[19]:


point = [top_point] + matches[1:19:2]
point


# In[37]:


topr = soup.find('td',class_="rankings-block__banner--rating u-text-right")
toprate = topr.text.replace('\n',"").split()[0]
toprate


# In[25]:


rates = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rates.append(i.text)
rates


# In[40]:


rating = [toprate] + rates[0:9]
rating


# In[43]:


print(len(team),len(match),len(point),len(rating))


# In[44]:


ODI_TEAMS= pd.DataFrame({'teams':team,'matches':match,'points':point,'rating':rating})


# In[45]:


ODI_TEAMS


# In[ ]:





# In[ ]:





# ODI Players

# In[46]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[47]:


page


# In[48]:


soup = BeautifulSoup(page.content)


# In[49]:


topp = soup.find('div',class_="rankings-block__banner--name-large")
top_play = topp.text
top_play


# In[58]:


play = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    play.append(i.text.replace('\n',""))
play[0:10]


# In[53]:


players = [top_play] + play[0:9]
players


# In[55]:


topc = soup.find('div',class_="rankings-block__banner--nationality")
topteam = topc.text.replace('\n',"")
topteam


# In[59]:


team = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    team.append(i.text)
team[0:10]


# In[61]:


teams = [topteam] + team[0:9]
teams


# In[63]:


toprate = soup.find('div',class_="rankings-block__banner--rating")
tops=toprate.text
tops


# In[65]:


rate = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    rate.append(i.text)
rate[0:10]


# In[67]:


rating = [tops]+ rate[0:9]
rating


# In[68]:


odiplayers = pd.DataFrame({'players':players,'team':teams,'rating':rating})
odiplayers


# In[ ]:





# In[ ]:





# ODI BOWLERS

# In[69]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[70]:


soup = BeautifulSoup(page.content)


# In[72]:


topplay = soup.find('div',class_="rankings-block__banner--name-large")
topplayer = topplay.text
topplayer


# In[75]:


player = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    player.append(i.text.replace('\n', ""))
player[0:9]


# In[77]:


players = [topplayer]+player[0:9]
players


# In[80]:


topt = soup.find('div',class_="rankings-block__banner--nationality")
topteam = topt.text.replace('\n',"")
topteam


# In[82]:


team = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    team.append(i.text)
team[0:9]


# In[84]:


teams = [topteam]+team[0:9]
teams


# In[85]:


topr= soup.find('div',class_="rankings-block__banner--rating")
toprate = topr.text
toprate


# In[87]:


rating=[]
for i in soup.find_all('td',class_="table-body__cell rating"):
    rating.append(i.text)
rating[0:9]


# In[88]:


ratings = [toprate]+ rating[0:9]


# In[89]:


ratings


# In[91]:


odi_allrounder = pd.DataFrame({'players':players,'team':teams,'rating':ratings})


# In[92]:


odi_allrounder


# In[ ]:




