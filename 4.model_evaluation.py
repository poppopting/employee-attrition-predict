
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np 
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


training_lasso=pd.read_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_training_lasso.csv')
testing_lasso=pd.read_csv(r'C:\Users\Guan-Ting Chen\Desktop\NCCU course2018\applied regrssion\final report\hr_testing_lasso.csv')


# In[ ]:


training_lasso=training_lasso.drop(columns=['number_project*position_accounting'])
testing_lasso=testing_lasso.drop(columns=['number_project*position_accounting'])


# In[ ]:


model=LogisticRegression()
model.fit(training_lasso.iloc[:,1:],training_lasso.iloc[:,0])
train_score=model.score(training_lasso.iloc[:,1:],training_lasso.iloc[:,0])
test_score=model.score(testing_lasso.iloc[:,1:],testing_lasso.iloc[:,0])
print('train=',train_score,'test=',test_score)


# In[ ]:


pd.DataFrame(confusion_matrix(testing_lasso.iloc[:,0],model.predict(testing_lasso.iloc[:,1:])))


# In[ ]:


from sklearn.metrics import classification_report
classification_report(testing_lasso.iloc[:,0],model.predict(testing_lasso.iloc[:,1:]))


# In[ ]:


from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(testing_lasso.iloc[:,0],model.predict(testing_lasso.iloc[:,1:]))
fpr, tpr, thresholds = roc_curve(testing_lasso.iloc[:,0],model.predict_proba(testing_lasso.iloc[:,1:])[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('1–Specifity',fontsize=20)
plt.ylabel('sensitivity',fontsize=20)
plt.title('ROC curve',fontsize=20)
plt.legend(loc="lower right",fontsize=14)
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'major', labelsize = 20)
ax.tick_params(axis = 'y', which = 'major', labelsize = 20)
plt.show()


# In[ ]:


logreg_y_pred = model.predict(testing_lasso.iloc[:,1:])
logreg_cm =confusion_matrix(logreg_y_pred,testing_lasso.iloc[:,0],[1,0])
sns.heatmap(logreg_cm,annot=True, fmt='.0f',xticklabels = ["Left(1)", "Stayed(0)"] , yticklabels = ["Left(1)", "Stayed(0)"],annot_kws={"size": 20})
plt.ylabel('Predicted class',fontsize=20)
plt.xlabel('True class',fontsize=20)
plt.title('Logistic Regression',fontsize=20)
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'major', labelsize = 20)
ax.tick_params(axis = 'y', which = 'major', labelsize = 20)

