class Helper:

    def findInString(self, string, letter):
        return [i for i, ltr in enumerate(string, 1) if ltr == letter]