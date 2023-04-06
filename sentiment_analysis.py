from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from config import TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_SUBSCRIPTION_KEY
from twitter_api import get_twitter_api, get_stock_tweets

def analyze_sentiment(text_analytics_client, df, batch_size=10):
    sentiments = []
    for i in range(0, len(df), batch_size):
        batch_df = df.iloc[i:i+batch_size]
        documents = [{"id": str(idx), "text": tweet["text"]} for idx, tweet in batch_df.iterrows()]
        results = text_analytics_client.analyze_sentiment(documents=documents)
        sentiments += [result.sentiment for result in results]

    df["sentiment"] = sentiments
    return df

# Integrating the sentiment_analysis with gui.py to get input from analyze() function and returning the 
# results as a dataframe to the GUI

def get_tweets_with_sentiment(word_search):
    # Authenticate with the Text Analytics service
    print("Authenticating with the Text Analytics service...")
    text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_SUBSCRIPTION_KEY))

    # Authenticate with the Twitter API
    print("Authenticating with the Twitter API...")
    api = get_twitter_api()

    # Get tweets containing a specific stock symbol
    num_tweets = 100
    tweets_df = get_stock_tweets(api, word_search, num_tweets)

    # Analyze the sentiment of the tweets
    print("Analyzing sentiment of tweets...")
    tweets_with_sentiment_df = analyze_sentiment(text_analytics_client, tweets_df)

    # Print the tweets and their sentiment
    print(tweets_with_sentiment_df[["text", "sentiment"]])
    return tweets_with_sentiment_df[["text", "sentiment"]]





# The below written code was to test the app without the GUI, now that it's working, we can integrate it with the GUI
# You can refer to the below code for references

# if __name__ == "__main__":
#     print("Sentiment Analysis")

#     # Authenticate with the Text Analytics service
#     print("Authenticating with the Text Analytics service...")
#     text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_SUBSCRIPTION_KEY))

#     # Authenticate with the Twitter API
#     print("Authenticating with the Twitter API...")
#     api = get_twitter_api()

#     # Get tweets containing a specific stock symbol
#     word_search = "$TSLA"
#     num_tweets = 100
#     tweets_df = get_stock_tweets(api, word_search, num_tweets)

#     # Analyze the sentiment of the tweets
#     print("Analyzing sentiment of tweets...")
#     tweets_with_sentiment_df = analyze_sentiment(text_analytics_client, tweets_df)

#     # Print the tweets and their sentiment
#     print(tweets_with_sentiment_df[["text", "sentiment"]])