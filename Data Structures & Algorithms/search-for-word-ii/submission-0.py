class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            node=trie
            for char in word:
                if char not in node:
                    node[char]={}
                node=node[char]
            node['word']=word
        rows=len(board)
        cols=len(board[0])
        result=set()
        def backtrack(r,c,node):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            char=board[r][c]
            if char=='#':
                return
            if char not in node:
                return 
            node=node[char]
            if "word" in node:
                result.add(node["word"])
            board[r][c]='#'
            backtrack(r + 1, c, node)
            backtrack(r - 1, c, node)
            backtrack(r, c + 1, node)
            backtrack(r, c - 1, node)
            board[r][c]=char
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,trie)
        return list(result)