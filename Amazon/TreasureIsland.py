import collections
import heapq

class Solution:
    def treasureIsland(self, grid):
        q = [(0, 0, 0)]
        visited = set()
        visited.add((0, 0))
        while q:
            i, j, dist = q.pop(0)
            if i == len(grid)-1 and j == 0:
                return dist

            elif grid[i][j] == 'O':
                for r, c in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    newr, newc = i+r, j+c
                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]):
                        if grid[newr][newc] != "D" and (newr, newc) not in visited:
                            q.append((newr, newc, dist+1))
                            visited.add((newr, newc))


if __name__=="__main__":
    solution = Solution()
    print(solution.treasureIsland([['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]))
