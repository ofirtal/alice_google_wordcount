#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


class WordCounter:
    def __init__(self, filename):
        self.word_count_dict = {}
        self.file_name = filename

    def count_from_file(self):
        with open(self.file_name, "r") as data_txt:
            for line in data_txt:
                list_of_line_words = line.lower().split()
                self.line_words_into_dict(list_of_line_words)

    def line_words_into_dict(self, words_list):
        for word in words_list:
            if word in self.word_count_dict:
                self.word_count_dict[word] += 1
            else:
                self.word_count_dict[word] = 1

    def get_dict(self):
        self.count_from_file()
        return self.sort_dict()

    def number_of_items(self):
        return

    def sort_dict(self):
        sorted_dict = sorted([(value, key) for (key, value) in self.word_count_dict.items()], reverse=True)
        return sorted_dict
