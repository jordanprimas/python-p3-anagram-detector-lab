# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        sorted_list = []
        for anagram in possible_anagrams:
            if sorted(anagram) == sorted(self.word):
                sorted_list.append(anagram)
        return sorted_list






