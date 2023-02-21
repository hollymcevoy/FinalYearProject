from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re

def sentiment_analysis(mergedD, keyword_file):
    # Read the CSV file containing tweets
    df = pd.read_csv(mergedD, header=None, names=['Text'])

    # Read the CSV file containing keywords to ignore
    keywords = pd.read_csv(keyword_file, header=None, names=['Keyword'])
    ignore_list = keywords['Keyword'].tolist()

    # Create a list of negation words
    negation_list = ["not", "n't", "no"]

    # Create a function to clean and process the tweets
    def process_tweet(tweet):
        # Convert the tweet to lowercase
        tweet = tweet.lower()

        # Replace contractions with their full form
        tweet = re.sub(r"won\'t", "will not", tweet)
        tweet = re.sub(r"can\'t", "can not", tweet)

        # Split the tweet into words
        words = tweet.split()

        # Initialize a flag to check for negation
        negation_flag = False

        # Remove keywords from the ignore list
        processed_tweet = []
        for word in words:
            if word in ignore_list:
                continue
            if word in negation_list:
                negation_flag = True
            else:
                if negation_flag:
                    word = "not_" + word
                    negation_flag = False
                processed_tweet.append(word)

        # Join the processed words back into a tweet
        processed_tweet = " ".join(processed_tweet)

        return processed_tweet

    # Apply the process_tweet function to the 'Text' column of the DataFrame
    df['Text'] = df['Text'].apply(process_tweet)

    # Create a function to classify each tweet as positive, negative, or neutral
    def classify_tweet(tweet):
        # Use TextBlob to classify the tweet
        sentiment = TextBlob(tweet).sentiment.polarity

        # Check for negation
        negation = re.findall(r"not_\w+", tweet)
        if negation:
            sentiment = -sentiment

        # Classify the tweet as positive, negative, or neutral based on the sentiment score
        if sentiment > 0:
            return 'Positive'
        elif sentiment < 0:
            return 'Negative'
        else:
            return 'Neutral'

    # Apply the classify_tweet function to the 'Text' column of the DataFrame
    df['Sentiment'] = df['Text'].apply(classify_tweet)

    # Count the number of tweets for each sentiment
    sentiment_counts = df['Sentiment'].value_counts()

    # Plot the sentiment counts as a pie chart
    plt.pie(sentiment_counts, labels=sentiment_counts.index, startangle=90,
            autopct='%1.1f%%', shadow=True)
    plt.axis('equal')
    plt.show()

# Call the sentiment_analysis function, passing the name of the CSV file and keyword file as arguments
sentiment_analysis('mergedD.csv', 'keywords.csv')
