import tweepy
import json
import requests

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
me = api.me().screen_name

slackURL = "https://slack.com/api/"
params = {'token': token, 'channel': '#test_', 'text': '', 'as_user': 'true'}

def create_twitter_url(id_str, screen_name):
    return "https://twitter.com/"+screen_name+"/status/"+str(id_str)

words = ['github:', 'arxiv:', 'pdf:']
ids = ['slam_hub', 'arxiv_cscv', 'shiropen2', 'ak92501']

for status in api.favorites(count=30):
    if any((q in status.text) for q in words) or any((id in status.user.screen_name) for id in ids):
        print(status.text)
        print(status.user.name)
        print(status.user.screen_name)
        params['text'] = create_twitter_url(status.id, status.user.screen_name)
        r = requests.post(slackURL + "chat.postMessage", params=params)