import matplotlib.pyplot as plt
import time


class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions=[]
        self.stack=[[]] 
        self.generated_states = 0
        self.checked_states = 0

    def solve_dfs(self):
        while len(self.stack) != 0: 
            node = self.stack.pop()
            self.checked_states += 1
            #print(node)
            if self.conflict(node) == False:
                if len(node) == self.size:
                    self.solutions.append(node)
                    #print(f'Found solution: {node}')
                for col in range(self.size):
                    queen = (len(node), col)
                    queens = node.copy()
                    queens.append(queen)
                    self.stack.append(queens)
                    self.generated_states += 1
        return self.solutions


    def conflict(self, queens):
        blockedRows = [False]*self.size
        blockedColumns = [False]*self.size
        blockedDiagonals1 = [False]*(self.size*2-1)
        blockedDiagonals2 = [False]*(self.size*2-1)

        for i in range(0,len(queens)):
            x,y = queens[i]
            diag1 = x + y
            diag2 = (self.size - x-1) + y
            #print(queens)
            if(blockedRows[y] or blockedColumns[x] or blockedDiagonals1[diag1] or blockedDiagonals2[diag2]):
                return True
            blockedRows[y] = True
            blockedColumns[x] = True
            blockedDiagonals1[diag1] = True
            blockedDiagonals2[diag2] = True
        return False


def createPlot(title,osX,osY):
    plt.plot(osX,osY)
    plt.xlabel("N-Queens(N)")
    plt.ylabel("time(s)")
    plt.title(title)
    plt.grid()
    plt.show()

tab=[]
generated_states_tab = []
checked_states_tab = []


for size in range(4,10):
    n_queens = NQueens(size)
    start=time.time()
    dfs_solutions = n_queens.solve_dfs()
    end=time.time()
    finalTime=end-start
    Time = finalTime
    tab.append(Time)
    generated_states_tab.append(n_queens.generated_states)
    checked_states_tab.append(n_queens.checked_states)
    print(f'Dla rozmiaru {size}x{size}:')
    print(f'Liczba wygenerowanych stanow: {n_queens.generated_states}')
    print(f'liczba sprawdzonych stanow: {n_queens.checked_states}')
    print(f'Czas kompilacji: {round(Time,2)}s\n')



createPlot("wykres czasu do liczby N-queens", range(4,10), tab)
  