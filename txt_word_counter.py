from print_dict_results import PrintDictResults
from wordcount import WordCounter
import argparse


class MainWordCounter:
    """ WordCounter takes a txt file and counts the app"""
    def __init__(self, filename, results_to_return):
        self.results = results_to_return
        self.sorted_dict_of_words = WordCounter(filename).get_dict()
        self.number_of_words_in_dict = len(self.sorted_dict_of_words)
        self.items_wanted()

    def items_wanted(self):
        """ checks the results wanted and verify that it dose not exceed the items existing in dict  """
        if self.results == 9999:
            PrintDictResults(self.sorted_dict_of_words).get_all_words()
        elif self.results > self.number_of_words_in_dict:
            PrintDictResults(self.sorted_dict_of_words).get_top(self.number_of_words_in_dict)
        else:
            PrintDictResults(self.sorted_dict_of_words).get_top(self.results)
        print('****')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('file_name', help='Enter file name url', type=str)
    parser.add_argument('--results', type=int, default=9999, help='Optional! default is all results. To get top results enter a a number: top 5 -> enter 5')

    args = parser.parse_args()

    MainWordCounter(args.file_name, args.results)
