#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import matplotlib.pyplot as plt


# In[2]:


data=pandas.read_csv('baltimore_crimes.csv')
data


# # CLEANING THE DATA

# In[3]:


for crime_time in range(len(data['CrimeTime'])):
    current_crime_time=data['CrimeTime'][crime_time].split(':')
    if len(current_crime_time)==1:
        data['CrimeTime'][crime_time]=current_crime_time[0][0:2]+':'+current_crime_time[0][2:4]+':00'
        


# # 1) FREQUENCY OF CRIME INCIDENTS ACROSS ALL DISTRICTS

# In[4]:


district_crimes={}
for district in data['District']:
    if district not in district_crimes:
        district_crimes[district]=0
    district_crimes[district]+=1
plt.rcParams["figure.figsize"]=[20,8]
plt.bar(*zip(*district_crimes.items()))
plt.show()


# * From the above frequency plot we can conclude that Southeastern district has the most number of incidents where as Northeastern district has the least number of incidents

# # 2) HEATMAP OF THE CRIMES COMMITTED

# In[6]:


import gmaps
API_KEY='AIzaSyCl7c7pr7lFAwQqm5q8H26bAx9E3eDxOGQ'
gmaps.configure(api_key=API_KEY)


# In[7]:


Location=[]
for location in data['Location 1']:
    lt=float(location[1:len(data['Location 1'][0])-1].split(',')[0])
    lg=float(location[1:len(data['Location 1'][0])-1].split(',')[1])
    Location.append((lt,lg))


# In[8]:


data


# In[12]:


fig = gmaps.figure(map_type='HYBRID')
heatmap_layer = gmaps.heatmap_layer(Location,point_radius=3.0)
fig.add_layer(heatmap_layer)
fig


# In[ ]:




