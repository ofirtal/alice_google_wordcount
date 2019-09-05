#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys


# read the file and return a sorted dict of words and values
def alice_helper(filename):
    counts = dict()
    with open(filename, "r") as data_txt:
      for line in data_txt:
        raw_line = str(line).lower()
        line_of_words = raw_line.split()
        for word in line_of_words:
          if word in counts:
            counts[word] += 1
          else:
            counts[word] = 1

      sorted_dict = sorted([(value, key) for (key, value) in counts.items()], reverse=True)
      return sorted_dict


# print the sorted dictionary
def print_words(filename):
    print(alice_helper(filename))


# print top 20 words that appeared in text. for more words replace the 20 in range different number
def print_top(filename):
    sorted_dict = alice_helper(filename)
    for i in range(20):
      print(i, " :", sorted_dict[i])


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  choice = 0
  first = True
  while not (choice == 1 or choice == 2):
    if not first:
      print("Invalid Choice: "+choice+"\n")
    first = False
    choice = int(input("What whould you like to do?\n1 count\n2 topcount\nEnter your chioce:\n"))
    filename = input("Please insert the file path:\n")
  do_choice(choice, filename)

def do_choice(choice, filename):
  option = choice
  if option == 1:
    print_words(filename)
  elif option == 2:
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
