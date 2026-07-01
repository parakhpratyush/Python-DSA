from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
    
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
    
        while queue:
            word, length = queue.popleft()
        
            if word == endWord:
                return length
        
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
        return 0
    
#----Testing----
solver=Solution()

print(solver.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(solver.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))