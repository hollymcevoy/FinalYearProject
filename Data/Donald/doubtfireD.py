import csv
import codecs

def compare_text_files(file1, file2):
    with codecs.open(file1, "r", encoding='utf-8', errors='ignore') as f1, \
         codecs.open(file2, "r", encoding='utf-8', errors='ignore') as f2:
         lines1 = set(line[:30] for line in f1)
         lines2 = set(line[:30] for line in f2)

    deleted_tweets = lines1 - lines2
    deleted_lines = []
    with codecs.open(file1, "r", encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line[:30] in deleted_tweets:
                deleted_lines.append(line)

    return deleted_lines

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for tweet in data:
            writer.writerow([tweet])

deleted_tweets = compare_text_files("donald1.txt", "donaldNew10.txt")
save_to_csv(deleted_tweets, "deletedD.csv")
