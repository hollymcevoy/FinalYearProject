import pandas as pd
import re
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os


import matplotlib.pyplot as plt


def process_tweet(tweet, keywords_file):
    # Convert to lower case
    tweet = tweet.lower()

    # Remove URLs
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)

    # Remove user @ references and '#' from hashtags
    tweet = re.sub(r'\@\w+|\#', '', tweet)

    # Remove punctuation
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers
    tweet = re.sub(r'\d+', '', tweet)

    # Remove extra white space
    tweet = tweet.strip()
    tweet = re.sub('\s+', ' ', tweet)

    # Remove words in keywords_file
    with open(keywords_file, 'r') as f:
        keywords = f.read().splitlines()
    tweet = ' '.join(word for word in tweet.split() if word not in keywords)

    # Check for positive and negative emojis
    positive_emojis = [':)', ':D', ':]', ';)', ':*', ':p', ':P', '😊', '😃', '🤗', '😍', 
                       '😘', '😇', '🤩', '🥳', '🙌', '👍', '💖', '💯', '🔥', '😁', '😆',
                        '😂', '🤣', '😜', '😎', '🎉', '❤️', '👏', '👌', '✨', '🌟', '🌈',
                          '🍕', '🍔', '🍟', '🍩', '🍭', '🎂', '🎈', '🎁', '🎊', '👑', '💐', 
                          '🌹', '🌺', '🌸', '🌷', '🌻', '🌼', '🐶', '🐱', '🦊', '🐻', '🐨',
                          '🐯', '🐰', '🦁', '🦄', '🐴', '🐮', '🐷', '🐒', '🐥', '🐟', '🦀']

    negative_emojis = [':(', ':/', ':\\', ':|', ':O', ':S', ':@', '😔', '😞', '😒', '😠',
                       '😡', '😩', '😓', '😖', '😠', '🤬', '🙄', '💔', '👎', '😢', '😭', '😕',
                       '🤢', '🤕', '💀', '👻', '😱', '😨', '👿', '💩', '👺', '👹', '🤮', '🥴',
                         '🥺', '😿', '🔪', '💣', '🚫', '🐍', '🕷️', '🦂', '🐀', '🦠', '🌪️', '🔥']



    positive_emoji_count = 0
    negative_emoji_count = 0
    for c in tweet:
        if c in positive_emojis:
            positive_emoji_count += 1
        elif c in negative_emojis:
            negative_emoji_count += 1

    return tweet, positive_emoji_count, negative_emoji_count


def calculate_sentiment_score(tweet, analyzer):
    # Calculate sentiment score using VADER
    score = analyzer.polarity_scores(tweet)['compound']

    return score


def sentiment_analysis(data_file, keywords_file):
    # Load data
    df = pd.read_csv(data_file)

    # Get filename without extension
    filename = data_file.split(".")[0]

    # Initialize VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Process tweets
    df['Text'], df['Positive Emojis'], df['Negative Emojis'] = zip(
        *df.iloc[:, 0].apply(lambda x: process_tweet(x, keywords_file)))

    # Calculate sentiment score for each tweet
    df['Sentiment Score'] = df['Text'].apply(lambda tweet: calculate_sentiment_score(tweet, analyzer))

    # Add sentiment score for emojis
    df['Sentiment Score'] += df['Positive Emojis'] - df['Negative Emojis']

    # Categorize tweets as positive, negative, or neutral
    df['Sentiment'] = df['Sentiment Score'].apply(lambda score: 'positive' if score > 0 else (
        'negative' if score < 0 else 'neutral'))

    # Output results
    output_file = f'sentiment_analysis_results_{filename}.csv'
    df.to_csv(output_file, index=False)
    print(f'Sentiment analysis complete. Results saved to {output_file}')

    # Generate pie chart for sentiment distribution
    sentiment_counts = df['Sentiment'].value_counts()
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
    plt.title(f'Sentiment Distribution for {filename}')
    plt.show()

# Analyze sentiment for each file
files = ['Trump.csv', 'Musk.csv', 'Biden.csv', 'Tesla.csv', 'SpaceX.csv']
for file in files:
    sentiment_analysis(file, 'keywords.csv')