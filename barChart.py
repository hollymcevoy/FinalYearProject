import pandas as pd
import matplotlib.pyplot as plt

# Define the file names and their corresponding labels
files = {
    'sentiment_analysis_results_Musk.csv': 'Elon Deleted',
    'sentiment_analysis_results_MuskTweet.csv': 'Elon tweets',
    'sentiment_analysis_results_Biden.csv': 'Biden Deleted',
    'sentiment_analysis_results_BidenTweet.csv': 'Biden Tweets',
    'sentiment_analysis_results_Trump.csv': 'Trump Deleted',
    'sentiment_analysis_results_TrumpTweet.csv': 'Trump Tweets',
    'sentiment_analysis_results_Tesla.csv': 'Tesla Deleted',
    'sentiment_analysis_results_TeslaTweet.csv': 'Tesla Tweets',
    'sentiment_analysis_results_SpaceX.csv': 'SpaceX Deleted',
    'sentiment_analysis_results_SpaceXTweet.csv': 'SpaceX Tweets'
}

# Define a color palette for related columns
colors = {
    'Elon Deleted': '#1f77b4',
    'Elon tweets': '#1f77b4',
    'Biden Deleted': '#ff7f0e',
    'Biden Tweets': '#ff7f0e',
    'Trump Deleted': '#2ca02c',
    'Trump Tweets': '#2ca02c',
    'Tesla Deleted': '#d62728',
    'Tesla Tweets': '#d62728',
    'SpaceX Deleted': '#9467bd',
    'SpaceX Tweets': '#9467bd'
}

# Create a list to store the negative sentiment percentages
negative_sentiments = []

# Loop through the files and calculate the negative sentiment percentage for each file
for file_name, label in files.items():
    df = pd.read_csv(file_name, header=None, names=['id', 'text', 'positive', 'negative', 'score', 'sentiment'])
    negative_sentiment = (df['sentiment'] == 'negative').sum() / len(df) * 100
    negative_sentiments.append(negative_sentiment)

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(range(len(files)), negative_sentiments, tick_label=list(files.values()), color=[colors[label] for label in files.values()])

# Set the chart title and labels
ax.set_title('Comparison of negative Sentiment in Deleted vs Non-Deleted Tweets')
ax.set_xlabel('Files')
ax.set_ylabel('% positvie Sentiment')

# Define the key
key_labels = ['Elon', 'Biden', 'Trump', 'Tesla', 'SpaceX']
key_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
key_patches = [plt.Rectangle((0,0),1,1,fc=color) for color in key_colors]

# Add the key to the chart
plt.legend(key_patches, key_labels, loc='center left', bbox_to_anchor=(1, 0.5))

# Show the chart
plt.show()