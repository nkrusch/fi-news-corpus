from os import listdir
from os.path import isfile, join
import csv

# path to corpus directory; change this value as necessary
directory_path = '../corpus'

# read all files
all_files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]

# create a list to hold data
articles = []

# iterate over each csv file
for f in all_files:

    rows = 0

    # open the file for reading
    with open(join(directory_path, f)) as csvfile:

        # read file contents
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:

            # skip header row
            if rows > 0:
                articles.append(row)

            rows += 1

# print some stats
print('num files: ' + str(len(all_files)))
print('articles: ' + str(len(articles)))

# sort articles by date
# article publish date is first property - we can use default sort here
articles.sort()

# display information about the oldest article in the dataset
print('=' * 40)
print('Julkaistu: ' + articles[0][0])
print('Otsikko: ' + articles[0][1])
print('Kuvaus: ' + articles[0][2])
print('Kuva: ' + articles[0][3])

# display information about the newest article in the dataset
print('=' * 40)
print('Julkaistu: ' + articles[-1][0])
print('Otsikko: ' + articles[-1][1])
print('Kuvaus: ' + articles[-1][2])
print('Kuva: ' + articles[-1][3])
print('=' * 40)
