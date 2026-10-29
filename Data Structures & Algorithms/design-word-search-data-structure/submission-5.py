class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.end = True
    
    def subsearch(self, cur, word):
        for i, w in enumerate(word):
            if w == '.':
                for l in cur.children:
                    if self.subsearch(cur.children[l], word[i + 1:]):
                        return True

                return False
            else:
                if w not in cur.children:
                    return False
                cur = cur.children[w]
        
        return cur.end


    def search(self, word: str) -> bool:
        cur = self.trie
        return self.subsearch(cur, word)
        
