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
for tweet in api.search(q='リフォロー', count=100):
    friendship = api.show_friendship(source_screen_name='ikuran01',target_screen_name=tweet.user.screen_name)
    if friendship[0].following == False:
        if tweet.user.friends_count > tweet.user.followers_count*4/5:
            api.create_friendship(tweet.user.screen_name)
            break
