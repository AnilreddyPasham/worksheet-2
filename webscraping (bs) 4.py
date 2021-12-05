#!/usr/bin/env python
# coding: utf-8

# ODI TEAMS

# In[57]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[3]:


page


# In[4]:


soup = BeautifulSoup(page.content)


# In[ ]:


soup


# In[9]:


teams = []

for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)


# In[65]:


team = teams[0:10]


# In[66]:


team


# In[14]:


matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches.append(i.text)


# In[41]:


match =['17'] + matches[0:18:2]


# In[42]:


match


# In[45]:


points =['2054'] + matches[1:18:2]


# In[46]:


points


# In[33]:


rating = []

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)


# In[47]:


ratings = ['121'] + rating[0:9]


# In[48]:


ratings


# In[54]:


print(len(team),len(match),len(points),len(ratings))


# In[55]:


odi_teams = pd.DataFrame({'team':team,'matches':match,'points':points,'rating':ratings})


# In[56]:


odi_teams


# In[ ]:





# In[ ]:





# ODI BATSMEN

# In[58]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[59]:


page


# In[60]:


soup = BeautifulSoup(page.content)


# In[61]:


soup


# In[76]:


tops = soup.find('div',class_="rankings-block__banner--name")


# In[90]:


top = tops.text


# In[91]:


top


# In[92]:


batsmen = []

for i in soup.find_all('td',class_="table-body__cell name"):
    batsmen.append(i.text.replace('\n', ""))


# In[93]:


top_batsmen = [top] + batsmen[0:9]


# In[94]:


top_batsmen


# In[95]:


team = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    team.append(i.text)


# In[106]:


team[0:9]


# In[99]:


first = soup.find('div',class_="rankings-block__banner--nationality")


# In[107]:


top = first.text.replace('\n', "").split()[0]


# In[108]:


teams = [top]+team[0:9]


# In[109]:


teams


# In[110]:


topper = soup.find('div',class_="rankings-block__banner--rating")


# In[111]:


top_rate= topper.text


# In[112]:


rating=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)


# In[114]:


ratings = [top_rate] + rating[0:9]


# In[115]:


ratings


# In[116]:


ODI_BATSMEN = pd.DataFrame({'batsmen':top_batsmen,'team':teams,'rating':ratings})


# In[117]:


ODI_BATSMEN


# In[ ]:





# In[ ]:





# ODI BOWLERS

# In[120]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[121]:


page


# In[122]:


soup = BeautifulSoup(page.content)


# In[123]:


bowl = soup.find('div',class_="rankings-block__banner--name-large")
bowler = bowl.text
bowler


# In[127]:


bowlers = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowlers.append(i.text.replace('\n', ""))
    
topbowl = bowlers[0:9]
topbowl


# In[131]:


top_bowlers=[bowler] + topbowl
top_bowlers


# In[134]:


team = soup.find('div',class_="rankings-block__banner--nationality")
topteam = team.text.replace('\n',"")
topteam


# In[135]:


teams
for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)
teams


# In[136]:


top_team= [topteam] + teams[0:9]
top_team


# In[137]:


top = soup.find('div',class_="rankings-block__banner--rating")
tops= top.text
tops


# In[138]:


rate = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    rate.append(i.text)
rate


# In[140]:


rating = [tops]+rate[0:9]
rating


# In[141]:


odi_bowler = pd.DataFrame({'bowlers':top_bowlers,'team':top_team,'rating':rating})
odi_bowler


# In[ ]:




