class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)
        n = len(word)
        if n == 1:
            self.words.add('.')
        for i in range(n):
            self.words.add(word[0:i] + '.' + word[i + 1:])
            for j in range(i + 1, n):
                self.words.add(word[0:i] + '.' + word[i + 1:j] + '.' + word[j+1:])

    def search(self, word: str) -> bool:
        return word in self.words


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # return False
print(wordDictionary.search("bad"))  # return True
print(wordDictionary.search(".ad"))  # return True
print(wordDictionary.search("b.."))  # return True
