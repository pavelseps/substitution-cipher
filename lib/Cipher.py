import numpy as np
import random

ALPHABET = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
SKIP = np.array([" ", ".", ",", "(", ")", "[", "]"])


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
        # Set data to work
        alph = ALPHABET[:]
        alph_dict = dict()

        for i in range(len(alph)):
            alph_dict[alph[i]] = None


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


    def decode(self):
        pass

