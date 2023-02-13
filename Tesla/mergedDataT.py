import os

# specify the directory where the text files are stored
directory = r"C:\Users\holly\OneDrive\Documents\FinalYearProject\Tesla\DataTesla"

# create a list to store the contents of the text files
texts = []

# iterate over the files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        # add the contents of each file to the list
        texts.append(f.read())

# convert the list to a set to remove duplicates
texts = set(texts)

# write the unique contents to a single file
with open(r'C:\Users\holly\OneDrive\Documents\FinalYearProject\Tesla\merged_data.txt', 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text)
