#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:10:27 2018

@author: PuneeT
"""

import tweepy
import json
from tweepy import OAuthHandler

consumer_key = 'Kl0H6t4hi2WiFJ8XuRUMkwRIW'
consumer_secret = 'sqaVgCNa8ItjtuRoncuRURzclLs4gSa23hMH7XX92t1wAluhIu'
access_token = '118168394-1u8GOdXBXEbTZCzCIrFyj670hB2yv5KohOlaur0N'
access_secret = 'mk9foZ2Pkthwi7dlN8N9STfudfkUpOEHfJQlj63ILSd3O'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

# The API variable is now our entry point for most of the operations 
# we can perform with Twitter
api = tweepy.API(auth)

# The function process_or_Store is a placeholder for our custom implementation
# In the simplest form, we can print out the JSON, one Tweet per line
def process_or_store(tweet):
    print(json.dumps(tweet))
    
## For example we can read our own timeline (our Twitter homepage) with below
#for status in tweepy.Cursor(api.home_timeline).items(1):
#    process_or_store(status._json)
    
## For list of all followers, we can have
#for friend in tweepy.Cursor(api.friends).items():
#    process_or_store(friend._json)

json.loads(request.POST.get('mytweets,'{}'))    
# For a list of all our tweets, we can collect tweets in below way
for tweet in tweepy.Cursor(api.user_timeline).items():
    mytweets.json = process_or_store(tweet._json)
  
with open('mytweets.json','r') as f:
    line = f.readline() #read only the first line / tweet
    tweet = json.loads(line) # load it as a Python Dict
    print(json.dumps(tweet,indent=4))
