import matplotlib.pyplot as plt
import time


class Heuristic:
    def calcualte(self, node):
        raise Exception("NotImplemented")


class H1(Heuristic):
    def calcualte(self, queens, size):
        value = 0
        for i in range(len(queens)):
            x, y = queens[i]
            w_row = 0
            if i < size/2:
                w_row = size - y + 1
            else:
                w_row = y
            value += w_row
        value *= (size - len(queens))
        return value


class H2(Heuristic):
    def calcualte(self, queens, size):
        value = 0
        board = []
        for i in range(size):
            board.append([False]*size)

        for i in range(len(queens)):
            x, y = queens[i]


class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = []
        self.stack = [([], 0)]  # tablica stanów a stany to tablice

    def solve_dfs(self):
        while len(self.stack) != 0:  # pobieram pustą tablice,
            node = self.stack.pop()
            if self.conflict(node[0]) == False:
                if len(node[0]) == self.size:
                    return node[0]
                for col in range(self.size):
                    queen = (len(node[0]), col)
                    queens = node[0].copy()
                    queens.append(queen)
                    self.appendInOrder(queens)
        return None

    def appendInOrder(self, queens):
        heuristic = H1()
        value = heuristic.calcualte(queens, self.size)
        i = 0
        while i < len(self.stack) and self.stack[i][1] < value:
            i = i + 1
        self.stack.insert(i, (queens, value))

    def conflict(self, queens):
        blockedRows = [False]*self.size
        blockedColumns = [False]*self.size
        blockedDiagonals1 = [False]*(self.size*2-1)
        blockedDiagonals2 = [False]*(self.size*2-1)

        for i in range(0, len(queens)):
            x, y = queens[i]
            diag1 = x + y
            diag2 = (self.size - x-1) + y
            if(blockedRows[y] or blockedColumns[x] or blockedDiagonals1[diag1] or blockedDiagonals2[diag2]):
                return True
            blockedRows[y] = True
            blockedColumns[x] = True
            blockedDiagonals1[diag1] = True
            blockedDiagonals2[diag2] = True
        return False


for size in range(1, 9):
    n_queens = NQueens(size)
    start = time.time()
    dfs_solution = n_queens.solve_dfs()
    end = time.time()
    finalTime = end-start

    print(f"Size: {size}")
    if dfs_solution == None:
        print("No solutions")
    else:
        print(
            f'Solution: ')
        for i in range(len(dfs_solution)):
            print(dfs_solution[i])
