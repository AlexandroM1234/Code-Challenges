"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
# TrieNode class stores all of letters of the word in the children hashtable
# Also marks the end of a word at a specific letter
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    # Trie tree starts with a root node that at max is going to store a - z for the start of every possible word
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # the current node always starts at the root
        cur = self.root
        # then go through every character in the word
        for c in word:
            # if its not in the hashtable create the key as the letter and the value as a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # otherwise current while change to be the hashtable at the specific character
            cur = cur.children[c]
        # after all the letters in the loop are done mare the end of the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # traverse the Trie tree
        cur = self.root
        
        for c in word:
            # if at any point we cant find a letter return false
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # if we hit the last letter of the word check if it is the end of a word and return it
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        # same as search except we don't have to check if its the end of a word
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)