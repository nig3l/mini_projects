import tweepy
import time

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)
tweets = ["Monday motivation! 💪", "Tuesday tip: always be learning 📚", "Hump day humor 😂", "Throwback Thursday to when we launched our first product 🚀", "Friday feels! 🎉"]

for tweet in tweets:
    api.update_status(tweet)
    time.sleep(86400)
