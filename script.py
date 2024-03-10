# Given a list of words and a matrix with characters, find in how many ways can we form the given list of words using the characters from the matrix. you can move left and down in the matrix from a starting point and see if a word can be formed using that sequence. You can only switch your direction once in the sequence.
#
# eg:
# matrix =
# [w, o, a , k]
# [r , r, a, m]
# [e, d, e, r]
#
# String[] words = {"word","order","worder"} ; ans = 2
# "Worder" is not part of the ans because you'd need to change the direction twice in the sequence.
#
#

class Solution:
    def findWords(self, board, words):
        WORD_KEY = '$'
        trie = {}
        m, n = len(board), len(board[0])
        res = []

        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[WORD_KEY] = word


        def backtrack(i, j, trie, path):
            letter = board[i][j]

            parent = trie[letter]
            if not parent:
                trie.pop(letter)

            word = parent.pop(WORD_KEY, False)
            if word:
                res.append((word, path))

            board[i][j] = '#'

            for ox, oy, in [(0, 1), (1, 0)]:
                nr, nc = i + ox, j + oy

                if min(nr, nc) < 0 or nr >= m or nc >= n:
                    continue

                if board[nr][nc] not in parent:
                    continue

                backtrack(nr, nc, parent, path + [(nr, nc)])

            board[i][j] = letter


        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie, [(i, j)])


        def isDirectionChanged(previ_dire, curr_dire):
            if previ_dire == None:
                return False
            return previ_dire != curr_dire


        def findDirection(x1, y1, x2, y2):
            if x2 - x1 == 0:
                return 'x'
            if y2 - y1 == 0:
                return 'y'

        ans = 0
        for word, path in res:
            previ_dire = None
            count = 0
            for i in range(len(path) - 1):
                dire = findDirection(path[i][0], path[i][1], path[i+1][0], path[i+1][1])
                if isDirectionChanged(previ_dire, dire):
                    count += 1
                    previ_dire = dire
                    if count >= 2:
                        break
                else:
                    previ_dire = dire
                    continue
            if count == 1:
                ans += 1
        return ans



board = [["w", "o", "a" , "k"],
["r" , "r", "a", "m"],
["e", "d", "e", "r"]]
words = ["word", 'order', 'worder']
solution = Solution()
print(solution.findWords(board, words))