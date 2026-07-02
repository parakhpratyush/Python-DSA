class WordDictionary(object):

    def __init__(self):
        # Trie node structure — dictionary of children + is_end flag
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        # Word end mark karo
        node['#'] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            
            char = word[i]
            
            if char == '.':
                # Wildcard — saare possible children try karo
                for child in node:
                    if child != '#' and dfs(node[child], i + 1):
                        return True
                return False
            else:
                if char not in node:
                    return False
                return dfs(node[char], i + 1)
        
        return dfs(self.root, 0)

#----Testing----
solver = WordDictionary()
solver.addWord("bad")
solver.addWord("dad")
solver.addWord("mad")
print(solver.search("pad"))   # False
print(solver.search("bad"))   # True
print(solver.search(".ad"))   # True
print(solver.search("b.."))   # True