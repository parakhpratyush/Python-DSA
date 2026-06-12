#VALID ANAGRAM
class Solution(object):
    def isAnagram(s, t):
        return sorted(s) == sorted(t)

print(Solution.isAnagram("anagram","nagaram"))
print(Solution.isAnagram("rat","car"))

#GROUP ANAGRAM
from collections import defaultdict

class Solution(object):
    def groupAnagrams(strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())
    
print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution.groupAnagrams([""]))
print(Solution.groupAnagrams(["a"]))