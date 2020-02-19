# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:05:56 2020

@author: tommy
"""
import pandas as pd
import re

#import the CSV file that contains the chatlog
file = 'Messages__Gianni__.csv'
data = pd.read_csv(file)

#subject names
sub1name= 'Gianni'
sub2name= 'Thomas'

#word to search in the chat log
word = 'lotion'

#replace column name and fill sender name
data['Sender'] = data['Sender Name'].fillna(sub2name)

#drop irrelevant columns and rows that are NULL, set index to date
data = data.drop(columns=['Type','Sender Name']).dropna()
data = data.set_index('Message Date')

#subject one data set
sub1 = data.loc[data.Sender==sub1name].drop(columns=['Sender'])

#subject two data set
sub2 = data.loc[data.Sender==sub2name].drop(columns=['Sender'])

#results for how many times word was found in the chat log
sub1result = sub1['Text'].str.contains(word, flags=re.IGNORECASE).value_counts()
sub2result = sub2['Text'].str.contains(word, flags=re.IGNORECASE).value_counts()

#change results series to single numeric value
sub1result= sub1result[1]
sub2result= sub2result[1]

#output to display to user
output = (str.upper(sub1name) + " has said " + str.upper(word) + ' in ' + str(sub1result) + " text messages" + 
   '\n' +  str.upper(sub2name) + " has said " + str.upper(word) + ' in ' + str(sub2result) + " text messages")
print(output)
