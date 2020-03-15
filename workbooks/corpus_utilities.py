from os import listdir
from os.path import isfile, join
import csv


def load_articles(directory_path):
    """
    This function takes a corpus directory path and returns a list of articles

    :param directory_path:
    :type directory_path: str
    :return: collection of articles
    :rtype: list
    """

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

    return articles
