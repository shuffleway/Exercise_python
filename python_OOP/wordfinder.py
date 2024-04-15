"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True
    ...
    """
    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""
        return random.choice(self.words)
    
if __name__ == "__main__":
    print("Word Finder")
    wf = WordFinder("words.txt")  
    print(f"{len(wf.words)} words read")
    print(wf.random() in wf.words)
    print(wf.random() in wf.words)
    print(wf.random() in wf.words)
    print("***********************************")

    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def __init__(self, filename):
        super().__init__(filename)

    def read_words(self):
        """Read words from file and exclude blank lines/comments."""
        with open(self.filename, 'r') as file:
            self.words = [word.strip() for word in file.readlines() if word.strip() and not word.startswith("#")]


if __name__ == "__main__":
    print("Special Word Finder")
    swf = SpecialWordFinder("complex.txt")
    print(f"{len(swf.words)} words read")
    print(swf.random() in ["pear", "carrot", "kale"])
    print(swf.random() in ["pear", "carrot", "kale"])
    print(swf.random() in ["pear", "carrot", "kale"])
