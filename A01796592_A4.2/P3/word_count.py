""" Word Count 
CLA-T-1201 - A01796592 - Assignment 4.2 - Problem 2
This script identify all distintic words and the frequency of them 
"""

import sys
import time

class WordCount:
    """ Word Count class 
    This class has the method to count the frequency of words in a text file
    """
    def __init__(self, arg_word_count):
        """ Constructor of the class 
        It initializes the array of words and an empty dictionary to store the word count
        """
        self.array_words = arg_word_count
        self.word_count = {}
        self.total_words = 0

    def count_words(self):
        """ Count the frequency of words in the array of words
        It iterates through the array of words and counts the frequency of each word
        """
        for w in self.array_words:
            word_lower = w.lower()
            if word_lower in self.word_count:
                self.word_count[word_lower] += 1
                self.total_words += 1
            else:
                self.word_count[word_lower] = 1
                self.total_words += 1

    def save_to_file(self, output_filename):
        """ Save the word count to a file 
        It writes the word and its frequency to the specified output file
        """
        with open(output_filename, 'w', encoding='utf-8') as f:
            for word_write, count in self.word_count.items():
                f.write(f"{word_write}: \t{count}\n")
                print(f"{word_write}: \t{count}")
            f.write(f"Total words: {self.total_words}\n")
            print(f"Total words: {self.total_words}\n")

if __name__ == "__main__":
    start_time = time.time()
    filenames = sys.argv[1:]
    with open("WordCountResults.txt", 'w', encoding='utf-8') as output_file:
        output_file.write("FILE\t\tWORD\tCOUNT\n")
        print("FILE\t\tWORD\tCOUNT")
        for fname in filenames:
            words = []
            with open(fname, 'r', encoding='utf-8') as file:
                tokens = (
                file.read()
                .replace(",", " ")
                .replace("\n", " ")
                .replace(";", " ")
                .split()
            )
            for word in tokens:
                if word.isalpha():
                    words.append(word.lower())
                else:
                    print(f"Warning: '{word}' in {fname} skipped")
            counter = WordCount(words)
            counter.count_words()
            for i, word in enumerate(words):
                output_file.write(f"{fname}\t{word}\t{counter.word_count[word]}\n")
                print(f"{fname}\t{word}\t{counter.word_count[word]}")
            output_file.write(f"{fname}\tTotal words\t{counter.total_words}\n")
            print(f"{fname}\tTotal words\t{counter.total_words}\n")
            output_file.write("\n")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
