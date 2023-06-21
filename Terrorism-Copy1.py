#!/usr/bin/env python
# coding: utf-8

# In[194]:


# Import all the essential libraries for our task
import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[195]:


#Loading the DataSet
df=pd.read_csv(R"C:\Users\bhoop\OneDrive\Documents\Desktop\globalterrorismdb_0718dist.csv",encoding=('ISO-8859-1'))


# In[196]:


df


# In[197]:


df.head()


# In[198]:


df.describe()


# In[199]:


df.dtypes


# In[200]:


df.shape


# In[201]:


df.info()


# In[202]:


df.columns


# In[203]:


for i in df.columns:
 print(i,end=" ,")


# In[204]:


df.isnull().sum()


# In[205]:


df=df[["iyear","imonth","iday","country_txt","region_txt","provstate","city","latitude","longitude","location","summary","attacktype1_txt","gname","motive","weaptype1_txt","nkill","nwound","addnotes"]]


# In[206]:


df.head()


# In[207]:


df.rename(columns={"iyear":"Year","imonth":"Month","iday":"dy","country_txt":"Country","region_txt":"Region","provstate":"Province/State","city":"City","latitude":"Latitude","longitude":"Longitude","location":"Location","summary":"Summary","targtypel_txt":"Target Type","gname":"Group Name","motive":"Motive","weaptypel_txt":"Weapon Type","nkill":"Killed","nwound":"Wounded","addnotes":"Add Notes"},inplace=True)


# In[208]:


df.head()


# In[213]:


df.isnull().sum()


# In[212]:


df.fillna(0)


# In[247]:


k=pd.DataFrame(df["Year"].value_counts().sort_index().reset_index())
k


# In[258]:


attacks=k.rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")


# In[259]:


attacks


# In[317]:


attacks.plot(kind="bar",color="red",figsize=(15,6),fontsize=13)
plt.title("Timeline of Attacks",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Attacks",fontsize=15)
plt.show()


# In[285]:


df["Causuality"]=df["Killed"]+df["Wounded"]


# In[307]:


cs=pd.DataFrame(df[["Year","Causuality"]]).set_index("Year").fillna(0).astype(int).groupby("Year").sum()
cs


# In[318]:


cs.plot(kind="bar",color="green",figsize=(15,6),fontsize=13)
plt.title("Year wise Casualties",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Casualties",fontsize=15)
plt.show()


# In[337]:


ki=pd.DataFrame(df[["Year","Killed"]]).fillna(0).astype(int).set_index("Year").groupby("Year").sum()
ki
ki.plot(kind="bar",color="blue",figsize=(15,6),fontsize=13)
plt.title("Year wise Killed",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Killed",fontsize=15)
plt.show()


# In[336]:


wo=pd.DataFrame(df[["Year","Wounded"]]).fillna(0).astype(int).set_index("Year").groupby("Year").sum()
wo
wo.plot(kind="bar",color="blue",figsize=(15,6),fontsize=13)
plt.title("Year wise Wounded Persons",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Wounded Persons",fontsize=15)
plt.show()


# In[343]:


reg=pd.crosstab(df.Year,df.Region)
reg


# In[346]:


reg.plot(kind="area",figsize=(15,6),fontsize=13)
plt.title("Year wise Wounded Persons",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Wounded Persons",fontsize=15)
plt.show()


# In[ ]:




