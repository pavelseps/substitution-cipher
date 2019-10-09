class Cipher:
    def __init__(self):
        self.dictionary = None
        self.encoded_text = ""
        self.decoded_text = ""

    def encode(self):
        self.encoded_text = "Enocding"

    def decode(self):
        self.decoded_text = "Decoding"

    def set_dictionary(self, dict):
        self.dictionary = dict

    def set_encoded_text(self, text):
        self.encoded_text = text

    def set_decoded_text(self, text):
        self.decoded_text = text

    def get_encoded_text(self):
        return self.encoded_text

    def get_decoded_text(self):
        return self.decoded_text
