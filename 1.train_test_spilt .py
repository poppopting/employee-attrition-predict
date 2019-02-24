
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from imblearn import under_sampling, over_sampling
from imblearn.over_sampling import SMOTE
from itertools import combinations


# In[2]:


hr=pd.read_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_report_01.csv')
hr=hr[['left','satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours', 'time_spend_company', 'Work_accident', 
       'promotion_last_5years','position_IT', 'position_RandD',
       'position_accounting', 'position_hr', 'position_management',
       'position_marketing', 'position_product_mng', 'position_sales',
       'position_support','salary_low','salary_medium']]
hr0=hr[hr['left']==0]
hr0=hr0.reset_index(drop=True)
hr1=hr[hr['left']==1]
hr1=hr1.reset_index(drop=True)


# In[3]:


x_train_0,x_test_0,y_train_0,y_test_0=train_test_split(hr0.iloc[:,1:],hr0.iloc[:,0],test_size=0.3)
x_train_1,x_test_1,y_train_1,y_test_1=train_test_split(hr1.iloc[:,1:],hr1.iloc[:,0],test_size=0.3)
x_train=pd.concat([x_train_0,x_train_1],axis=0)
x_test=pd.concat([x_test_0,x_test_1],axis=0)
y_train=pd.concat([y_train_0,y_train_1],axis=0)
y_test=pd.concat([y_test_0,y_test_1],axis=0)


# In[4]:


over_samples=SMOTE(random_state=107354012)   
over_samples_X,over_samples_y=over_samples.fit_sample(x_train, y_train)  


# In[5]:


smote_train_x=pd.DataFrame(over_samples_X,columns=['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'position_IT', 'position_RandD',
       'position_accounting', 'position_hr', 'position_management',
       'position_marketing', 'position_product_mng', 'position_sales',
       'position_support', 'salary_low', 'salary_medium'])


# In[6]:


interact=['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'position_IT', 'position_RandD',
       'position_accounting', 'position_hr', 'position_management',
       'position_marketing', 'position_product_mng', 'position_sales',
       'position_support', 'salary_low', 'salary_medium']


# In[7]:


for i in list(combinations(interact, 2)):
    smote_train_x['%s'%i[0]+'*%s'%i[1]]=smote_train_x[i[0]]*smote_train_x[i[1]]


# In[8]:


for i in list(combinations(interact, 2)):
    x_test['%s'%i[0]+'*%s'%i[1]]=x_test[i[0]]*x_test[i[1]]


# In[9]:


add_power=['satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours', 'time_spend_company']
for term in add_power:
    smote_train_x['%s'%term+'^2']=smote_train_x[term]**2
    smote_train_x['%s'%term+'^3']=smote_train_x[term]**3


# In[10]:


for term in add_power:
    x_test['%s'%term+'^2']=x_test[term]**2
    x_test['%s'%term+'^3']=x_test[term]**3


# In[11]:


over_samples_y=pd.DataFrame(over_samples_y,columns=['left'])
y_test=pd.DataFrame(y_test,columns=['left'])


# In[12]:


training=pd.concat([over_samples_y,smote_train_x],axis=1)
testing=pd.concat([y_test,x_test],axis=1)
training.to_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_training.csv',index=False)
testing.to_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_testing.csv',index=False)

