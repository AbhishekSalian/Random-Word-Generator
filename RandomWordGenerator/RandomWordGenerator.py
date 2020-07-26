"""Random Word Generator main file
"""
import string
import random
import re


class RandomWord:
    def __init__(self, max_word_size=10,
                 constant_word_size=True,
                 include_digits=False,
                 special_chars=r"@_!#$%^&*()<>?/\|}{~:`",
                 include_special_chars=False):

        """Method for initializing the Random Word Generator

        Args:

            max_word_size (int, optional): Represents maximum length of
                                           randomly generated word.
                                           Defaults to 10.

            constant_word_size (bool, optional): Represents word length of
                                                 randomly generated word.
                                                 Defaults to True.

            include_digits (bool, optional): Represents whether or not to
                                            include digits in generated words.
                                            Defaults to False.

            special_chars (regex, optional): Represents a regex string of all
                                             specials character you want to
                                             include in generated words.
                                             Default"@_!#$%^&*()<>?/\\|}{~:`".

            include_special_chars (bool, optional): Represents inclusion of
                                                    special characters in
                                                    generated words.
                                                    Defaults to False.

        """

        self.alphabet_string = ""
        self.max_word_size = max_word_size
        self.constant_word_size = constant_word_size

        for l, u in zip(string.ascii_lowercase, string.ascii_uppercase):
            self.alphabet_string += l + u

        if include_digits is True:
            self.alphabet_string += '0123456789'

        if include_special_chars is True:
            spec_char_set = set(re.sub('[A-Za-z0-9]', '', special_chars))
            special_chars = ''.join(spec_char_set)
            self.alphabet_string += special_chars

        if self.max_word_size < 1:
            raise Exception("ERROR!!! max_word_size argument must be >=1")

    # Generate method
    def generate(self):
        """Method for generating a single random word

        Returns:
            str: The random word generated

        """
        random_word = ""

        if self.max_word_size < 1:
            return None

        if self.constant_word_size is True:
            for _ in range(self.max_word_size):
                index = random.randint(0, len(self.alphabet_string)-1)
                random_word += self.alphabet_string[index]
        else:
            n = random.randint(1, self.max_word_size)
            for _ in range(n):
                index = random.randint(0, len(self.alphabet_string)-1)
                random_word += self.alphabet_string[index]

        return random_word

    # Generate list of random words method
    def getList(self, num_of_words=5):
        """Method that with help us to generate a list of random word
           at one shot

        Args:
            num_of_words (int, optional): The no. of random word you want
                                                in a list. Defaults to 5.

        Returns:
            list: A list of randomly generated words

        """
        random_word_list = []

        if num_of_words < 1:
            return None

        for _ in range(num_of_words):
            random_word_list.append(self.generate())

        return random_word_list
