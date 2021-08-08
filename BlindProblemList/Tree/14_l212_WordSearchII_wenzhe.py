class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:        
        trie = dict()
        result = set()
        for w in words:
            cur_node = trie
            for i in range(len(w)):
                if w[i] not in cur_node:
                    cur_node[w[i]] = dict()
                cur_node = cur_node[w[i]]
            cur_node['end'] = w
        def backtrack(i, j, trie):
            if 'end' in trie:
                result.add(trie['end'])
            char = board[i][j]
            board[i][j] = 'X'
            if i > 0 and board[i-1][j] in trie:
                backtrack(i-1, j, trie[board[i-1][j]])
            if i < len(board)-1 and board[i+1][j] in trie:
                backtrack(i+1, j, trie[board[i+1][j]])
            if j > 0 and board[i][j-1] in trie:
                backtrack(i, j-1, trie[board[i][j-1]])
            if j < len(board[0])-1 and board[i][j+1] in trie:
                backtrack(i, j+1, trie[board[i][j+1]])
            board[i][j] = char
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtrack(i,j,trie[board[i][j]])
        return list(result)