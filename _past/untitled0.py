# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:05:56 2020

@author: tommy
"""
import pandas as pd
import re

#import the CSV file that contains the chatlog
data = pd.read_csv('Messages__Gianni__.csv')

#replace column name and fill sender name
data['Sender'] = data['Sender Name'].fillna('Thomas')

#drop irrelevant columns and rows that are NULL, set index to date
data = data.drop(columns=['Type','Sender Name'])
data = data.set_index('Message Date')
data= data.dropna()

#subject one data set
gianni = data.loc[data.Sender=='Gianni']
gianni = gianni.drop(columns=['Sender'])

#subject two data set
thomas = data.loc[data.Sender=='Thomas']
thomas = thomas.drop(columns=['Sender'])

#word to search in the chat log
word = 'sex'

#results for how many times word was found in the chat log
gword = gianni['Text'].str.contains(word, flags=re.IGNORECASE).value_counts()
tword = thomas['Text'].str.contains(word, flags=re.IGNORECASE).value_counts()
g_times_said= gword[1]
t_times_said= tword[1]

#output to display to user
output = ("GIANNI has said " + str.upper(word) + ' in ' + str(g_times_said) + " text messages" + 
    '\n' +  "THOMAS has said " + str.upper(word) + ' in ' + str(t_times_said) + " text messages")
print(output)
