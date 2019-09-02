import collections
import heapq

class Solution:
    def prisonCells(self, cells, N):
        seen = []
        seen.append(cells)
        for i in range(1, N+1):
            newcells = [0] * len(cells)
            for j in range(1, len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    newcells[j] = 1
            cells = newcells[:]

            if cells in seen:
                ind = seen.index(cells)
                cycle = i - ind
                i = ind + (N - ind) % cycle
                return seen[i]
            else:
                seen.append(cells)
        return cells




if __name__=="__main__":
    solution = Solution()
    print(solution.prisonCells([1,0,0,1,0,0,1,0], 1000000000))
