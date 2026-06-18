class TrieNode:
    def __init__(self):
        # children = dictionary mapping character → TrieNode
        # Har node ke paas 26 possible children ho sakte hain (a-z)
        # Dictionary isliye kyunki sparse hoga — har node pe saare letters nahi honge
        self.children = {}
        
        # is_end = True matlab is node pe koi word khatam hota hai
        # Sirf True/False — "apple" insert karte waqt 'e' node pe is_end=True
        self.is_end = False


class Trie:
    def __init__(self):
        # Root node — empty character, poore trie ka starting point
        self.root = TrieNode()
    
    def insert(self, word):
        # Root se shuru karo
        node = self.root
        
        # Har character ke liye
        for char in word:
            # Agar ye character is node ke children mein nahi hai
            # Naya TrieNode banao
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Us child node pe move karo
            node = node.children[char]
        
        # Word ke last character pe is_end = True
        # Matlab yahan ek complete word khatam hota hai
        node.is_end = True
    
    def search(self, word):
        # Root se shuru karo
        node = self.root
        
        for char in word:
            # Agar character nahi mila — word exist nahi karta
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Saare characters mile — lekin is_end check karo
        # "app" search karo jab sirf "apple" insert hua ho
        # Saare characters milenge lekin is_end = False
        return node.is_end
    
    def startsWith(self, prefix):
        # Prefix search — is_end check nahi karna
        # Sirf itna chahiye ki prefix exist kare as a path
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Prefix mili — True return karo
        # is_end check nahi — prefix complete word nahi hona chahiye
        return True


# Test
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apply")

print(trie.search("apple"))     # True
print(trie.search("app"))       # True
print(trie.search("ap"))        # False — "ap" insert nahi kiya
print(trie.startsWith("app"))   # True — "app" prefix exist karta hai
print(trie.startsWith("apl"))   # False
