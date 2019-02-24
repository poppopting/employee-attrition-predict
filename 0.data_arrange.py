
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('max_info_columns',100)


# In[2]:


hr=pd.read_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr2.csv')
hr=hr.rename(columns={'sales':'position'})


# In[3]:


hr=hr[['left','satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours', 'time_spend_company', 'Work_accident', 
       'promotion_last_5years', 'position', 'salary']]


# In[ ]:


hrhr=pd.get_dummies(hr)


# In[ ]:


hrhr.to_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_report_01.csv',index=False)

