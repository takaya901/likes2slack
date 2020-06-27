import tweepy
import json
import requests
import os
from datetime import datetime, date, timedelta

def create_twitter_url(id_str, screen_name):
    return "https://twitter.com/"+screen_name+"/status/"+str(id_str)

def post():
    auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

    api = tweepy.API(auth)
    me = api.me().screen_name

    slackURL = "https://slack.com/api/"
    params = {'token': os.environ["SLACK_TOKEN"], 'channel': '#test_', 'text': '', 'as_user': 'true'}

    words = ['github:', 'arxiv:', 'pdf:']
    ids = ['slam_hub', 'arxiv_cscv', 'shiropen2', 'ak92501', 'HCI_Comics']

    for status in api.favorites(count=30):
        if any((q in status.text) for q in words) or any((id in status.user.screen_name) for id in ids):
            date_str = str(status.created_at)
            created_at = datetime.fromisoformat(date_str)

            yesterday = datetime.now() - timedelta(days=1)
            if created_at >= yesterday:
                params['text'] = create_twitter_url(status.id, status.user.screen_name)
                r = requests.post(slackURL + "chat.postMessage", params=params)

if __name__ == "__main__":
    post()