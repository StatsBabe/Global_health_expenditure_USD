# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:27:25 2020

@author: Owner# Tanya Reeves

Further to a large study I undertook in 2019 regarding Income Inequality (Gini Index) and Life Expectancy,
this study is an exploration of global Health Expenditure (USD) per capita, and its relation to the "Health Development Index" (United Nations)

Many thanks to the many Githubers, Kagglers and Youtubers who have provided me with so much guidance and inspiration.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("health_systems.csv")

data.info()
"""
Country_Region                          187 non-null object
Province_State                          14 non-null object
World_Bank_Name                         210 non-null object
Health_exp_pct_GDP_2016                 186 non-null float64
Health_exp_public_pct_2016              186 non-null float64
Health_exp_out_of_pocket_pct_2016       186 non-null float64
Health_exp_per_capita_USD_2016          186 non-null float64
per_capita_exp_PPP_2016                 186 non-null float64
External_health_exp_pct_2016            167 non-null float64
Physicians_per_1000_2009-18             189 non-null float64
Nurse_midwife_per_1000_2009-18          189 non-null float64
Specialist_surgical_per_1000_2008-18    175 non-null float64
Completeness_of_birth_reg_2009-18       163 non-null float64
Completeness_of_death_reg_2008-16       107 non-null float64
dtypes: float64(11), object(3)
memory usage: 23.1+ KB
"""

data.isnull().sum()
"""
df.isnull().sum()
Out[7]: 
Country_Region                           23
Province_State                          196
World_Bank_Name                           0
Health_exp_pct_GDP_2016                  24
Health_exp_public_pct_2016               24
Health_exp_out_of_pocket_pct_2016        24
Health_exp_per_capita_USD_2016           24
per_capita_exp_PPP_2016                  24
External_health_exp_pct_2016             43
Physicians_per_1000_2009-18              21
Nurse_midwife_per_1000_2009-18           21
Specialist_surgical_per_1000_2008-18     35
Completeness_of_birth_reg_2009-18        47
Completeness_of_death_reg_2008-16       103
dtype: int64
"""
data.Health_exp_per_capita_USD_2016.describe()
"""
count     186.000000
mean     1037.004839
std      1712.592621
min        16.400000
25%        85.700000
50%       322.600000
75%      1059.800000
max      9869.700000
Name: Health_exp_per_capita_USD_2016, dtype: float64
"""
data['health_development_level']=["high" if i>1037 else "low" for i in data.Health_exp_per_capita_USD_2016]
print(data['health_development_level'].value_counts(dropna=False))

"""
low     161
high     49
Name: health_development_level, dtype: int64
"""

data.boxplot(column='Health_exp_per_capita_USD',by='health_development_level',figsize=(9,15))

data['category']=["best" if i>8000 else "good" if 4000<i<8000 else "average" if 2000<i<4000 else "bad" if 1000<i<2000 else "worst" for i in data.Health_exp_per_capita_USD_2016]
print(data['category'].value_counts(dropna=False))

"""
worst      160
bad         22
good        15
average     11
best         2
Name: category, dtype: int64
"""
filtr = data.Health_exp_per_capita_USD_2016 > 8000
f_data = data[filtr]
print(f_data)

"""
    Country_Region Province_State  ... health_development_level  category
181    Switzerland            NaN  ...                     high      best
199             US            NaN  ...                     high      best
"""

#Tidy Data(melting)
data_new = (data[(data['Health_exp_per_capita_USD_2016']>4000)])
melted = pd.melt(frame = data_new, id_vars = 'Country_Region',value_vars = ['Health_exp_pct_GDP_2016','Health_exp_per_capita_USD_2016'])
print(melted)
"""
   Country_Region                        variable   value
0       Australia         Health_exp_pct_GDP_2016     9.3
1         Austria         Health_exp_pct_GDP_2016    10.4
2         Belgium         Health_exp_pct_GDP_2016    10.0
3          Canada         Health_exp_pct_GDP_2016    10.5
4         Denmark         Health_exp_pct_GDP_2016    10.4
5         Finland         Health_exp_pct_GDP_2016     9.5
6          France         Health_exp_pct_GDP_2016    11.5
7         Germany         Health_exp_pct_GDP_2016    11.1
8         Iceland         Health_exp_pct_GDP_2016     8.3
9         Ireland         Health_exp_pct_GDP_2016     7.4
10          Japan         Health_exp_pct_GDP_2016    10.9
11     Luxembourg         Health_exp_pct_GDP_2016     6.2
12    Netherlands         Health_exp_pct_GDP_2016    10.4
13         Norway         Health_exp_pct_GDP_2016    10.5
14         Sweden         Health_exp_pct_GDP_2016    10.9
15    Switzerland         Health_exp_pct_GDP_2016    12.2
16             US         Health_exp_pct_GDP_2016    17.1
17      Australia  Health_exp_per_capita_USD_2016  5002.4
18        Austria  Health_exp_per_capita_USD_2016  4688.3
19        Belgium  Health_exp_per_capita_USD_2016  4149.4
20         Canada  Health_exp_per_capita_USD_2016  4458.2
21        Denmark  Health_exp_per_capita_USD_2016  5565.6
22        Finland  Health_exp_per_capita_USD_2016  4117.3
23         France  Health_exp_per_capita_USD_2016  4263.4
24        Germany  Health_exp_per_capita_USD_2016  4714.3
25        Iceland  Health_exp_per_capita_USD_2016  5063.6
26        Ireland  Health_exp_per_capita_USD_2016  4758.6
27          Japan  Health_exp_per_capita_USD_2016  4233.0
28     Luxembourg  Health_exp_per_capita_USD_2016  6271.4
29    Netherlands  Health_exp_per_capita_USD_2016  4742.0
30         Norway  Health_exp_per_capita_USD_2016  7477.9
31         Sweden  Health_exp_per_capita_USD_2016  5710.6
32    Switzerland  Health_exp_per_capita_USD_2016  9836.0
33             US  Health_exp_per_capita_USD_2016  9869.7
"""

#pivoting data(reverse of melted)

print(melted.pivot(index='Country_Region',columns='variable',values='value'))

"""
Country_Region                                                         
Australia                           9.3                          5002.4
Austria                            10.4                          4688.3
Belgium                            10.0                          4149.4
Canada                             10.5                          4458.2
Denmark                            10.4                          5565.6
Finland                             9.5                          4117.3
France                             11.5                          4263.4
Germany                            11.1                          4714.3
Iceland                             8.3                          5063.6
Ireland                             7.4                          4758.6
Japan                              10.9                          4233.0
Luxembourg                          6.2                          6271.4
Netherlands                        10.4                          4742.0
Norway                             10.5                          7477.9
Sweden                             10.9                          5710.6
Switzerland                        12.2                          9836.0
US                                 17.1                          9869.7
"""

#seeing which countries rated as best, medium and worst
data1 = (data[(data['Health_exp_per_capita_USD_2016']>6000)])
data2 = (data[(data['Health_exp_pct_GDP_2016']<3)])
#vertical concatenate
conc_data_row = pd.concat([data1,data2],axis=0,ignore_index=True)
conc_data_row
"""
      Country_Region Province_State  ... health_development_level  category
0         Luxembourg            NaN  ...                     high      good
1             Norway            NaN  ...                     high      good
2        Switzerland            NaN  ...                     high      best
3                 US            NaN  ...                     high      best
4             Angola            NaN  ...                      low     worst
5         Bangladesh            NaN  ...                      low     worst
6             Brunei            NaN  ...                      low     worst
7               Laos            NaN  ...                      low     worst
8             Monaco            NaN  ...                     high   average
9           Pakistan            NaN  ...                      low     worst
10  Papua New Guinea            NaN  ...                      low     worst

[11 rows x 16 columns]
"""
#horizontal concatenate
data1 = (data[(data['Health_exp_per_capita_USD_2016']>6000)])
data2 = (data[(data['Health_exp_pct_GDP_2016']<3)])
conc_data_col = pd.concat([data1,data2],axis=1)
conc_data_col
"""
    Country_Region Province_State  ... health_development_level  category
4              NaN            NaN  ...                      low     worst
13             NaN            NaN  ...                      low     worst
24             NaN            NaN  ...                      low     worst
103            NaN            NaN  ...                      low     worst
111     Luxembourg            NaN  ...                      NaN       NaN
124            NaN            NaN  ...                     high   average
140         Norway            NaN  ...                      NaN       NaN
142            NaN            NaN  ...                      low     worst
145            NaN            NaN  ...                      low     worst
181    Switzerland            NaN  ...                      NaN       NaN
199             US            NaN  ...                      NaN       NaN
"""

#Data Types
data.dtypes
"""
Country_Region                           object
Province_State                           object
World_Bank_Name                          object
Health_exp_pct_GDP_2016                 float64
Health_exp_public_pct_2016              float64
Health_exp_out_of_pocket_pct_2016       float64
Health_exp_per_capita_USD_2016          float64
per_capita_exp_PPP_2016                 float64
External_health_exp_pct_2016            float64
Physicians_per_1000_2009-18             float64
Nurse_midwife_per_1000_2009-18          float64
Specialist_surgical_per_1000_2008-18    float64
Completeness_of_birth_reg_2009-18       float64
Completeness_of_death_reg_2008-16       float64
health_development_level                 object
category                                 object
"""
data['Province_State'].value_counts(dropna=False)
"""
NaN                 196
Guam                  1
Hong Kong             1
Sint Maarten          1
Channel Islands       1
Macau                 1
New Caledonia         1
Cayman Islands        1
St Martin             1
French Polynesia      1
Puerto Rico           1
Virgin Islands        1
Isle of Man           1
Faroe Islands         1
Greenland             1
Name: Province_State, dtype: int64
"""

#drop non-values
data11 =data
data11['Province_State'].dropna(inplace=True)
assert data11['Province_State'].notnull().all()

#Building Data Frames from Scratch
 # data frames from dictionary
    
country = data.World_Bank_Name
Health_exp = data.Health_exp_per_capita_USD_2016
list_label = ["country","Health_exp"]
list_col =[country, Health_exp]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df

#add new column
df['region'] = data.Country_Region

#Broadcasting
df['income'] = 0
df

df.info()
"""
Data columns (total 4 columns):
country       210 non-null object
Health_exp    186 non-null float64
region        187 non-null object
income        210 non-null int64
dtypes: float64(1), int64(1), object(2)
memory usage: 6.7+ KB
"""
#Visual Exploratory Data Analysis

   #PLOT
data1 = data.loc[:,['Health_exp_pct_GDP_2016','Health_exp_out_of_pocket_pct_2016','Health_exp_per_capita_USD_2016']]
data1.plot(figsize=(15,15))

#SUBPLOTS
data1.plot(subplots=True, figsize=(15,15))
plt.show()

f,ax = plt.subplots(figsize=(18,18))
sns.heatmap(data.corr(),annot=True,linewidth=.5,fmt='.1f',ax=ax)
plt.show()

data.plot(kind='scatter',x="Health_exp_per_capita_USD_2016", y="per_capita_exp_PPP_2016",figsize=(10,10))

#hist
data1.plot(kind='hist',y='Health_exp_per_capita_USD_2016',bins=50,range=(0,250),figsize=(10,10))

#histogram subplot with non cumulative and cumulative
fig,axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind='hist',y='Health_exp_per_capita_USD_2016',bins=50,range=(0,250),ax=axes[0])
data1.plot(kind='hist',y='Health_exp_per_capita_USD_2016',bins=50,range=(0,250),ax=axes[1],cumulative=True)
plt.savefig('graph.png')
plt

data.describe()
"""
       Health_exp_pct_GDP_2016  ...  Completeness_of_death_reg_2008-16
count               186.000000  ...                         107.000000
mean                  6.715054  ...                          89.309346
std                   2.976537  ...                          18.071157
min                   1.700000  ...                           4.000000
25%                   4.500000  ...                          85.500000
50%                   6.200000  ...                          99.000000
75%                   8.375000  ...                         100.000000
max                  23.300000  ...                         100.000000
"""
#Indexing Pandas Time Series
data2=data.head()
date_list=['1996-01-10','1996-02-10','1996-03-10','1996-04-11','1996-05-12']
datetime_object=pd.to_datetime(date_list)
data2['date']=datetime_object
data2=data2.set_index('date')
data2

#Select according to date index
print(data2.loc['1996-03-10'])
"""
Country_Region                          Algeria
Province_State                              NaN
World_Bank_Name                         Algeria
Health_exp_pct_GDP_2016                     6.6
Health_exp_public_pct_2016                 67.7
Health_exp_out_of_pocket_pct_2016          30.9
Health_exp_per_capita_USD_2016            260.4
per_capita_exp_PPP_2016                   998.2
External_health_exp_pct_2016                  0
Physicians_per_1000_2009-18                 1.8
Nurse_midwife_per_1000_2009-18              2.2
Specialist_surgical_per_1000_2008-18       12.1
Completeness_of_birth_reg_2009-18           100
Completeness_of_death_reg_2008-16           NaN
health_development_level                    low
category                                  worst
Name: 1996-03-10 00:00:00, dtype: object
"""

print(data2.loc['1996-03-10':'1996-05-12'])
"""
           Country_Region Province_State  ... health_development_level  category
date                                      ...                                   
1996-03-10        Algeria            NaN  ...                      low     worst
1996-04-11        Andorra            NaN  ...                     high   average
1996-05-12         Angola            NaN  ...                      low     worst
"""
#calculate mean according to years
data2.resample('A').mean()

#calculate mean according to months
data2.resample('M').mean()

# As you see, some values are NaN, to interpolate as linear method
data2.resample('M').first().interpolate('linear')
"""
           Country_Region  Province_State  ... health_development_level  category
date                                       ...                                   
1996-01-31    Afghanistan             NaN  ...                      low     worst
1996-02-29        Albania             NaN  ...                      low     worst
1996-03-31        Algeria             NaN  ...                      low     worst
1996-04-30        Andorra             NaN  ...                     high   average
1996-05-31         Angola             NaN  ...                      low     worst
"""

#and interpolate, do not change real mean
data2.resample('M').mean().interpolate('linear')
"""
Out[44]: 
            Health_exp_pct_GDP_2016  ...  Completeness_of_death_reg_2008-16
date                                 ...                                   
1996-01-31                     10.2  ...                                NaN
1996-02-29                      6.7  ...                               53.0
1996-03-31                      6.6  ...                               66.5
1996-04-30                     10.4  ...                               80.0
1996-05-31                      2.9  ...                               80.0
"""

