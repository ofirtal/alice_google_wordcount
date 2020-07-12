class PrintDictResults:
    def __init__(self, dict_of_sorted_words):
        self.list_of_sorted_words = dict_of_sorted_words

    def print_items(self, counter):
        print(f'{counter + 1}. "{self.list_of_sorted_words[counter][1]}" : {self.list_of_sorted_words[counter][0]}')

    def get_all_words(self):
        for item in self.list_of_sorted_words:
            self.print_items((self.list_of_sorted_words.index(item)))

    def get_top(self, number_of_wanted_items):
        for i in range(0, number_of_wanted_items):
            self.print_items(i)
