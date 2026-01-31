class Trie:

    def __init__(self):
        self.prefixes = set()
        self.words = set()

    # def insert(self, word: str) -> None:
    #     self.words.add(word)
    #     for i in range(len(word)):
    #         self.prefixes.add(word[0:i + 1])

    def insert(self, word):
        self.words.add(word)
        prefix = ""
        for c in word:
            prefix += c
            self.prefixes.add(prefix)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True
trie.insert("banana")
print(trie.search("ban"))     # return False
print(trie.startsWith("ban")) # return True
trie.insert("ban")
print(trie.search("ban"))     # return True
