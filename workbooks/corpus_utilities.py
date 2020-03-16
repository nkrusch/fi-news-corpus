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


def longest_base_word(word_list):
    """Given a list of words, this function finds the longest common sequence from
    the beginning that is common between each words in the list"""

    unique_words = list(set(word_list))

    # if list contains exactly 1 words, return that
    if len(unique_words) == 1:
        return unique_words[0]

    max_len, res = -1, ['']

    # find longest word
    for ele in word_list:
        if len(ele) > max_len:
            max_len = len(ele)

    # loop substrings
    for idx in range(1, max_len):
        tmp = list(set([t[0:idx] for t in word_list]))
        if len(tmp) > 1:
            break
        res = tmp
    return res[0]
