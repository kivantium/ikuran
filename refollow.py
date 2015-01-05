#!/usr/bin/python
#-*- coding: utf-8 -*-

from tweepy import *

def get_oauth():
    consumer_key = lines[0]
    consumer_secret = lines[1]
    access_key = lines[2]
    access_secret = lines[3]
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

#Authorization
f = open('/home/kivantium/ikuran/config.txt','r')
data = f.read()
f.close()
lines = data.split('\n')

auth = get_oauth()
api = API(auth)
followers_id = api.followers_ids('ikuran01')
friends_id = api.friends_ids('ikuran01')
for follower in followers_id:
    if follower not in friends_id:
        api.create_friendship(follower)
