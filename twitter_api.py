import tweepy
import pandas as pd
from config import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# Function to authenticate and return a Tweepy API object
def get_twitter_api():
    print('Authneticating with Twitter...')
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Function to get tweets containing a specific stock symbol
def get_stock_tweets(api, stock_symbol, num_tweets=100):
    print("Getting tweets containing the stock symbol: " + stock_symbol)
    tweets = tweepy.Cursor(api.search_tweets, q=stock_symbol, lang="en").items(num_tweets)
    tweet_data = [[tweet.id, tweet.text, tweet.created_at] for tweet in tweets]
    df = pd.DataFrame(data=tweet_data, columns=["id", "text", "created_at"])
    return df