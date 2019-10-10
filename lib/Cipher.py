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
        appearance_dict = self._get_alphabet_dict(np.array([]))
        intersect_dict = self._get_alphabet_dict(np.array([]))
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
                        appearance_dict[word[word_char_i]] = np.append(appearance_dict[word[word_char_i]],
                                                                       candidate_word[word_char_i])

                # Intersect candidates
                intersect_dict = self.intersect_dicts(intersect_dict, appearance_dict)
                appearance_dict = self._get_alphabet_dict(np.array([]))

            except:
                print("Can not find in dictionary:", word)

        intersect_dict = self.remove_solved_letters(intersect_dict)

        # Print dict stats
        self.print_stats(intersect_dict)

        # Write original
        self.original = ""
        for char_c in self.cipher:
            if not np.isin(char_c, SKIP) and len(intersect_dict[char_c]) > 0:
                self.original += intersect_dict[char_c][0]
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

    def intersect_dicts(self, intersect_dict, appearance_dict):
        result = self._get_alphabet_dict(np.array([]))

        for char in result:
            if len(appearance_dict[char]) > 0:
                if len(intersect_dict[char]) < 1:
                    result[char] = np.unique(appearance_dict[char])
                else:
                    result[char] = np.intersect1d(intersect_dict[char], np.unique(appearance_dict[char]))
            else:
                result[char] = np.unique(intersect_dict[char])

        return result

    def print_stats(self, intersect_dict):
        missing = np.array([])
        unclear = dict()
        correct = dict()

        for char in intersect_dict:
            if len(intersect_dict[char]) < 1:
                missing = np.append(missing, char)
            elif len(intersect_dict[char]) == 1:
                correct[char] = intersect_dict[char][0]
            elif len(intersect_dict[char]) > 1:
                unclear[char] = intersect_dict[char]
        print("CORRECT: "+ str(int((len(correct) / len(intersect_dict)) * 100)) +"%", correct)
        print("UNCLEAR: "+ str(int((len(unclear) / len(intersect_dict)) * 100)) +"%", unclear)
        print("MISSING: "+ str(int((len(missing) / len(intersect_dict)) * 100)) +"%", missing)

    def remove_solved_letters(self, intersect_dict):
        # then removeSolvedLettersFromMapping and try guess last char
        alph = ALPHABET[:]

        # remove all ready found
        to_remove_index = np.array([])
        for i in range(len(alph)):
            char = alph[i]
            if(len(intersect_dict[char]) == 1):
                to_remove_index = np.append(to_remove_index, np.where(alph == intersect_dict[char][0]))

        alph = np.delete(alph, np.unique(to_remove_index))

        # check dict and remove allready found chars
        is_changed = False
        for char in intersect_dict:
            if(len(intersect_dict[char]) > 1):
                intersect_dict[char] = np.intersect1d(alph, intersect_dict[char])

                if len(intersect_dict[char]) == 1:
                    is_changed = True

        if is_changed:
            return self.remove_solved_letters(intersect_dict)
        else:
            return intersect_dict
