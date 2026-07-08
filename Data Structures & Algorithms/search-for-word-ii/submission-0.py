class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Instead of a boolean, we store the actual word string here for easy retrieval

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. BUILD THE TARGET MANIFEST (Trie)
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w # Store the word at the final leaf node
            
        rows, cols = len(board), len(board[0])
        result = []
        
        # 2. THE TACTICAL PATROL SWEEP (DFS + Backtracking)
        def backtrack(r: int, c: int, node: TrieNode):
            char = board[r][c]
            
            # If the current character isn't a valid next step in our Trie, abort immediately
            if char not in node.children:
                return
                
            next_node = node.children[char]
            
            # Target located! Add it to our recovery list
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None # Clear it so we don't accidentally log duplicates
                
            # Temporary tape: Mark this room as visited by changing its character
            board[r][c] = "#"
            
            # Step in all 4 directions (Up, Down, Left, Right)
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in directions:
                if 0 <= nr < rows and 0 <= nc < cols:
                    backtrack(nr, nc, next_node)
                    
            # Peel off the tape: Restore the original room character on our way out
            board[r][c] = char

        # 3. DISPATCH TEAM: Start a sweep from every single coordinate in the grid
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)
                
        return result