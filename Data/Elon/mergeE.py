import csv

def merge_csv_files(deleteE, merge):
    tweets = set()
    
    with open(deleteE, 'r', encoding='utf-8') as f8:
        reader8 = csv.reader(f8)
        for row in reader8:
            tweets.add(tuple(row))
            
    with open(merge, 'r', encoding='utf-8') as f2:
        reader2 = csv.reader(f2)
        for row in reader2:
            tweets.add(tuple(row))
    
    with open('merged.csv', 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        for tweet in tweets:
            writer.writerow(tweet)

merge_csv_files('deletedE.csv', 'merged.csv')
