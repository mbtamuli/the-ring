class UniqueChars(object):

    def has_unique_chars(self, string):
        chars = []

        if string == None:
            return False
        letters = list(string)

        for letter in letters:
            if letter not in chars:
                chars.append(letter)
            elif letter in chars:
                return False

        return True
