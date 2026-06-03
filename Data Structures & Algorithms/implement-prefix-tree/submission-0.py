
class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.d = PrefixNode()
        

    def insert(self, word: str) -> None:
        cur = self.d
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
        
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.d
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end


    def startsWith(self, prefix: str) -> bool:
        cur = self.d
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        