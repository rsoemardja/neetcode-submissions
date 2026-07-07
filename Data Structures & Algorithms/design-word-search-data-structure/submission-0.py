# 1. THE NODE BLUEPRINT
class TrieNode:
    def __init__(self):
        self.children = {}  # Maps letter -> TrieNode
        self.is_word = False

class WordDictionary:
    def __init__(self):
        # Create our base entry point
        self.root = TrieNode()

    # 2. ADD WORD PROTOCOL
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode() # Create drawer if missing
            curr = curr.children[char]           # Step inside
        curr.is_word = True                      # Paste the word-end sticker

    # 3. SEARCH PROTOCOL
    def search(self, word: str) -> bool:
        
        # We define a helper inside to handle the recursive backtracking for dots
        def dfs(index: int, node: TrieNode) -> bool:
            curr = node
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # WILDCARD MATCH: Inspect every single available drawer
                    for child in curr.children.values():
                        # If the rest of the word matches down this branch, we win!
                        if dfs(i + 1, child):
                            return True
                    return False # None of the branches worked out
                    
                else:
                    # STANDARD LETTER MATCH
                    if char not in curr.children:
                        return False # Dead end
                    curr = curr.children[char] # Keep moving down the chain
                    
            return curr.is_word

        # Fire off the inspection starting at index 0 and the root node
        return dfs(0, self.root)