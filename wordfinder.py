"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:


    def __init__(self, file_path):
      """Initialize WordFinder with a path to a file containing words"""
      self.file_path = file_path
      self.words = self.read_words_from_file()

    def read_words_from_file(self):
     """Read words from the file and return a list of words"""
     with open(words.txt, 'r') as file:
         words = [line.strip() for line in file]
     return words

    def random(self):
       """Return a random word from the list of words"""
       return random.choice(self.words)
    
    def num_words_read(self):
       """Return the number of words read from the file"""
       return len(self.words)
    
    # wf = WordFinder("C:\Users\admin\Documents\python-oo-practice\words.txt")


    