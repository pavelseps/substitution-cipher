import numpy as np
import random
import operator

ALPHABET = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
SKIP = np.array([" ", ".", ",", ":",  ";", "(", ")", "[", "]", "?", "!", "\"", "'", "\\", "/"])


class Cipher:
    def __init__(self):
        self.dictionary = None
        self.original = ""
        self.cipher = ""

    def set_dictionary(self, dict):
        self.dictionary = dict

    def set_original_text(self, text):
        self.original = text

    def set_cipher_text(self, text):
        self.cipher = text

    def get_original_text(self):
        return self.original

    def get_cipher_text(self):
        return self.cipher

    def encode(self):
        print("Cipher encode: Start")
        # Set data to work
        alph = ALPHABET[:]
        alph_dict = self._get_alphabet_dict()

        self.cipher = ""


        for i in range(len(self.original)):
            char = self.original[i].upper()

            # Skip unneeded chars
            if not np.isin(char, SKIP):
                # Set new char is is empty
                if alph_dict[char] is None:

                    # Out of chars in alphabet
                    if len(alph) < 1:
                        raise Exception('Alphabet for encoding is empty')

                    random.shuffle(alph)
                    alph_dict[char], alph = alph[-1], alph[:-1]

                char_new = alph_dict[char]



                self.cipher += char_new
            else:
                self.cipher += char

        print("Cipher encode: Done")

    def decode(self):
        print("Cipher decode: Start")
        # Set data to work
        appearance_dict = self._get_alphabet_dict_funct(lambda : self._get_alphabet_dict(0))
        cipher = (self.cipher + '.')[:-1]

        # Remove unwanted chars except space
        for i in range(len(SKIP)):
            if SKIP[i] != " ":
                cipher = cipher.replace(SKIP[i], "")

        cipher_array = cipher.split()

        # Process each word
        for i in range(len(cipher_array)):
            word = cipher_array[i]
            try:
                pattern = self.dictionary.word_to_pattern(word)
                candidates = self.dictionary.find_pattern(pattern)

                # Set number of appearance
                for word_char_i in range(len(word)):
                    for candidate_word_i in range(len(candidates)):
                        candidate_word = candidates[candidate_word_i]
                        appearance_dict[word[word_char_i]][candidate_word[word_char_i]] += 1
            except:
                print("Can not find in dictionary:", word)

        translate_dict = self._get_alphabet_dict()

        # Create char to char dictionary (key cipher, val original)
        for char in translate_dict:
            max_item = max(appearance_dict[char].items(), key=operator.itemgetter(1))

            if max_item[1] > 0:
                translate_dict[char] = max_item[0]
                total = sum(appearance_dict[char].values())
                print(char + " is " + translate_dict[char] + ": " + str(((max_item[1] / total) * 100)) + "%")

        # Write original
        self.original = ""
        for char_c in self.cipher:
            if not np.isin(char_c, SKIP) and translate_dict[char_c] is not None:
                self.original += translate_dict[char_c]
            else:
                self.original += char_c

        print("Cipher encode: Done")


    def _get_alphabet_dict(self, default = None):
        alph_dict = dict()

        for i in range(len(ALPHABET)):
            alph_dict[ALPHABET[i]] = default
        return alph_dict

    def _get_alphabet_dict_funct(self, funct):
        alph_dict = dict()

        for i in range(len(ALPHABET)):
            alph_dict[ALPHABET[i]] = funct()
        return alph_dict