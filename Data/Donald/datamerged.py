import os
import csv
import hashlib

def read_file(path):
    encodings = ['utf-8', 'iso-8859-1']  # list of encodings to try
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as file:
                return file.read()
        except Exception as e:
            pass  # try the next encoding
    # if we get here, none of the encodings worked
    print(f"Error reading file: {path}")
    return ""

folder_path = 'C:/Users/holly/OneDrive/Documents/FinalYearProject/Data/Donald/DonaldData'

file_contents = {}
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        content = read_file(file_path)
        hash_value = hashlib.md5(content.encode('utf-8')).hexdigest()
        if hash_value not in file_contents:
            file_contents[hash_value] = content

output_path = 'C:/Users/holly/OneDrive/Documents/FinalYearProject/Data/Donald/DonaldData/TrumpTweet.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_MINIMAL)
    for content in file_contents.values():
        for tweet in content.split('\n'):
            if tweet.strip() != '':
                tweet_id = str(hash(tweet))[:10]
                writer.writerow([f'"{tweet_id} {tweet.strip()}"'])
