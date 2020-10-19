#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Libraries
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Importing data
os.chdir('C:/Users/Public/Dataset')
df = pd.read_csv('Sample_Dataset.csv')
df.head()


# In[4]:


# Quantity of items 0 and 1
cnt = len(df['obj1'])
cnt


# In[5]:


# Record count equal to 0
cnt_obj_0 = len(df[df['obj1']==0])
cnt_obj_0


# In[6]:


# Record count equal to 1
cnt_obj_1 = len(df[df['obj1']==1])
cnt_obj_1


# In[7]:


# How much more is 0 compared to 1
qtd_vezes_maior = '{:.2f}'.format(cnt_obj_0/cnt_obj_1)
print('The quantity of 0 is '+str(qtd_vezes_maior)+' times greater than the quantity of 1')


# In[9]:


# Setting the background for the chart
sns.set_style('darkgrid')

# Building the count graph
ax = sns.countplot(df['obj1'], palette="Set3")

# Percentage of 0 and 1
perc_0 = '{:.2f}%'.format(100*(cnt_obj_0/cnt))
perc_1 = '{:.2f}%'.format(100*(cnt_obj_1/cnt))

# Set the Xlabel
plt.xlabel('Object')

# Inserting the percentages on the chart
plt.text(1,3000,"% of 0: "+perc_0+"\n% of 1: "+perc_1)

# Show the graph
plt.show()


# In[10]:


# Shuffle the data before creating the subsets
df = df.sample(frac=1)

#Defining the size of the range we want from the data [0 and 1]

df_0 = df.loc[df['obj1']==0][:834]
df_01 = df.loc[df['obj1']==1]

# Concatenating the subsets
df2 = pd.concat([df_0,df_01])

# Shuffling the data
new_df = df2.sample(frac=1, random_state = 50)
new_df.head()


# In[11]:


# Checking the new distribution of records equal to 0 and 1
print(new_df['obj1'].value_counts()/len(new_df))


# In[12]:


# Checking the balance on the chart
ax2 = sns.countplot(new_df['obj1'], palette="Set3")

