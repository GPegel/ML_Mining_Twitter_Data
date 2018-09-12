import json
import tweepy
from env import *

from tweepy import OAuthHandler

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

# What if we want to have a list of all our followers? There you go:
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# And how about a list of all our tweets? Simple:
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

def process_or_store(tweet):
    print(json.dumps(tweet))
