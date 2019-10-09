import numpy as np


class Dictionary:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None
        self.pattern_tree = dict()

    def load(self):
        file = open(self.file_name, "r")
        self.data = file.readlines()
        file.close()
        self.data = [x.strip() for x in self.data]

    def find_pattern(self, pattern_arr):
        return self._find_pattern_in_tree(self.pattern_tree, pattern_arr)

    def _find_pattern_in_tree(self, ref, pattern_array):
        number, pattern_array = int(pattern_array[0]), pattern_array[1:]

        if ref.get(number, None) is None:
            raise Exception('Patter not found')

        if len(pattern_array) < 1:  # Set word to end
            if ref[number].get("result", None) is None:
                raise Exception('Patter not found')
            return ref[number]["result"]
        else:
            return self._find_pattern_in_tree(ref[number], pattern_array)

    def word_to_pattern(self, word):
        word = word.upper()
        result = np.array([])
        patt_it = 0
        char_dict = dict()

        for i in range(len(word)):
            char = word[i]
            pattern = char_dict.get(char, None)

            # Set new number to pattern
            if pattern is None:
                pattern = char_dict[char] = int(patt_it)
                patt_it += 1

            result = np.append(result, pattern)

        return result


    def process_dict_pattern(self):
        print("Dict tree: Start")
        self.pattern_tree = dict()
        for i in range(len(self.data)):
            word = self.data[i]
            pattern = self.word_to_pattern(word)
            self._set_to_patter_tree(self.pattern_tree, pattern, word)
        print("Dict tree: Done")

    def _set_to_patter_tree(self, ref, pattern_array, word):
        number, pattern_array = int(pattern_array[0]), pattern_array[1:]

        # Generate new node if needed
        if ref.get(number, None) is None:
            ref[number] = dict()

        if len(pattern_array) < 1: # Set word to end

            # Generate array on end if needed
            if ref[number].get("result", None) is None:
                ref[number]["result"] = np.array([])

            ref[number]["result"] = np.append(ref[number]["result"], word)
        else:
            self._set_to_patter_tree(ref[number], pattern_array, word)
