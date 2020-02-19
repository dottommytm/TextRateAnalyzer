# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:47:49 2020

@author: tommy
"""

import pandas as pd
import re
from matplotlib import pyplot as plt

#import the CSV file that contains the chatlog
file = 'Messages__Gianni__.csv'
data = pd.read_csv(file)

#subject names
sub1name= 'Gianni'
sub2name= 'Thomas'

#word to search in the chat log
word = 'sleep'

#replace column name and fill sender name
data['Sender'] = data['Sender Name'].fillna(sub2name)

#drop irrelevant columns and rows that are NULL, set index to date

data['Date']= pd.to_datetime(data['Message Date']) 
data.index= data['Date']
data = data[['Text', 'Sender']].dropna()
#subject one data set
sub1 = data.loc[data.Sender==sub1name].drop(columns=['Sender'])

#subject two data set
sub2 = data.loc[data.Sender==sub2name].drop(columns=['Sender'])

#results for how many times word was found in the chat log
sub1result = sub1['Text'].str.contains(word, flags=re.IGNORECASE)
sub2result = sub2['Text'].str.contains(word, flags=re.IGNORECASE)

#group by month
sub1result = sub1result.resample('M').sum()
sub2result = sub2result.resample('M').sum()
sub1result.index = sub1result.index.month_name().str.slice(stop=3)
sub2result.index = sub2result.index.month_name().str.slice(stop=3)

#graph
plt.style.use('Solarize_Light2')
plt.plot(sub1result, label=sub1name, color='black')
plt.plot(sub2result, label=sub2name, color='blue')
plt.title('Times we have said ' + (str.upper(word)) + ' throughout the months')
plt.xlabel('Month')
plt.ylabel('Number of times')
plt.legend()
plt.savefig('resultimg2.png', dpi = 300)