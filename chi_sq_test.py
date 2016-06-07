# chi square test of indepdence  
# week2 assignment for Data Analysis Tools

"""
Created on Tue Jun 07 14:47:04 2016

@author: taehee jeong
"""


# import libraries
import pandas as pd
import numpy as np
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

#%% Load data
path='C:/Bigdata/Data Analysis and Interpretation/Dataset/GapMinder/'
data = pd.read_csv(path+'gapminder.csv', low_memory=False)

print data.columns

data1=data.copy()

#setting variables you will be working with to numeric
data1['urbanrate'] = pd.to_numeric(data1['urbanrate'], errors='coerce')
data1['suicideper100th'] = pd.to_numeric(data1['suicideper100th'], errors='coerce')



#%% Model Interpretation for Chi-Square Tests:
# more than 2 Categorical explanatory variable vs more than 2 Categorical response variable

# quartile split (use qcut function & ask for 4 groups - gives quartile split)
print '2008 urban population (% of total) : 4 categories - quartiles'
data1['urban_group']=pd.qcut(data1.urbanrate, 4, labels=["1=0%tile","2=25%tile","3=50%tile","4=75%tile"])

print '2005 Suicide, age adjusted, per 100 000  : 4 categories - quartiles'
data1['suicide_group']=pd.qcut(data1.suicideper100th, 4, labels=["1=0%tile","2=25%tile","3=50%tile","4=75%tile"])


# contingency table of observed counts
ct1=pd.crosstab(data1['urban_group'], data1['suicide_group'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)


# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)

#%% Model Interpretation for post hoc Chi-Square Test results:
features=['suicide_group','urban_group']
data2=data1[features]

data1.suicideper100th.describe()
recode_sui = {"1=0%tile":5,"2=25%tile":8,"3=50%tile":12,"4=75%tile":36}
data2['suicide_group']= data2['suicide_group'].map(recode_sui)

data1.urbanrate.describe()
recode_urb = {"1=0%tile":37,"2=25%tile":58,"3=50%tile":74,"4=75%tile":100}
data2['urban_group']= data2['urban_group'].map(recode_urb)

# set explanatory variable types 
data2['urban_group'] = data2['urban_group'].astype('category')
# new code for setting variables to numeric:
data2['suicide_group'] = pd.to_numeric(data2['suicide_group'], errors='coerce')

# graph percent with suicide dependence within each urban rate group 
seaborn.factorplot(x='urban_group', y='suicide_group', data=data2, kind="bar", ci=None)
plt.xlabel('2008 urban rate (%) ')
plt.ylabel('2005 Suicide per 100,000')

#%% post hoc test
#set 1
recode1 = {37:37,58:58}
data2['COMP1v2']= data2['urban_group'].map(recode1)

# contingency table of observed counts
ct1=pd.crosstab(data2['suicide_group'], data2['COMP1v2'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)


#set 2
recode2 = {37:37,74:74}
data2['COMP1v3']= data2['urban_group'].map(recode2)

# contingency table of observed counts
ct2=pd.crosstab(data2['suicide_group'], data2['COMP1v3'])
print (ct2)

# column percentages
colsum=ct2.sum(axis=0)
colpct=ct2/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)


#set 3
recode3 = {37:37,100:100}
data2['COMP1v4']= data2['urban_group'].map(recode3)

# contingency table of observed counts
ct3=pd.crosstab(data2['suicide_group'], data2['COMP1v4'])
print (ct3)

# column percentages
colsum=ct3.sum(axis=0)
colpct=ct3/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs3= scipy.stats.chi2_contingency(ct3)
print (cs3)

#set 4
recode4 = {58:58,74:74}
data2['COMP2v3']= data2['urban_group'].map(recode4)

# contingency table of observed counts
ct4=pd.crosstab(data2['suicide_group'], data2['COMP2v3'])
print (ct4)

# column percentages
colsum=ct4.sum(axis=0)
colpct=ct4/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs4= scipy.stats.chi2_contingency(ct4)
print (cs4)


#set 5
recode5 = {58:58,100:100}
data2['COMP2v4']= data2['urban_group'].map(recode5)

# contingency table of observed counts
ct5=pd.crosstab(data2['suicide_group'], data2['COMP2v4'])
print (ct5)

# column percentages
colsum=ct5.sum(axis=0)
colpct=ct5/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs5= scipy.stats.chi2_contingency(ct5)
print (cs5)

#set 6
recode6 = {74:74,100:100}
data2['COMP3v4']= data2['urban_group'].map(recode6)

# contingency table of observed counts
ct6=pd.crosstab(data2['suicide_group'], data2['COMP3v4'])
print (ct6)

# column percentages
colsum=ct6.sum(axis=0)
colpct=ct6/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs6= scipy.stats.chi2_contingency(ct6)
print (cs6)
