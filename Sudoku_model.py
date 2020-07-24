import numpy as np
import copy

class Sudoku():
    def __init__(self,array=None):
        self.array = array

    def sd(self):
        list = np.where(self.array != 0)
        self.list = [(list[0][i],list[1][i]) for i in range(len(list[0]))]
        self.grid_dict = self.grid_assign()
        self.grid_dict_2 = {0 : {(i,j) : self.array[i][j] for i in range(3) for j in range(3)},1 : {(i,j) : self.array[i][j] for i in range(3) for j in range(3,6)},2 : {(i,j) : self.array[i][j] for i in range(3) for j in range(6,9)},3 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(3)},4 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(3,6)},5 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(6,9)},6 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(3)},7 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(3,6)},8 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(6,9)}}
        self.check_all()
        self.values = {}
        list_2 = np.where(self.array == 0)
        self.list_2 = [(list_2[0][i],list_2[1][i]) for i in range(len(list_2[0]))]
        self.possible_value()
        self.sol()
        return self.array
    def check_all(self):
        for i in self.list:
            if self.conditions(i):
                continue
            else:
                print("Same Elements")
                return
    def conditions(self,i):
        #FOR ROWS
        for j in range(9):
            if j == i[1]:
                continue
            elif self.array[i[0],i[1]] == self.array[i[0],j]:
                return False

        #FOR COLUMN
        for j in range(9):
            if j == i[0]:
                continue
            elif self.array[i[0],i[1]] == self.array[j,i[1]]:
                return False

        #FOR GRID
        grid = self.grid_dict_2[self.grid_dict[i]]
        for j in grid.keys():
            if j == i:
                continue
            elif grid[j] == self.array[i[0],i[1]]:
                return False
        return True
    def grid_assign(self):
        l = np.where(self.array == self.array)
        l = [(l[0][i],l[1][i]) for i in range(len(l[0]))]
        grid = {}
        for i in l:
            if 0 <= i[0] <= 2:
                if 0<= i[1] <= 2:
                    grid[i] = 0
                elif 3 <= i[1] <= 5:
                    grid[i] = 1
                elif 6 <= i[1] <= 8:
                    grid[i] = 2
            elif 3 <= i[0] <= 5:
                if 0<= i[1] <= 2:
                    grid[i] = 3
                elif 3 <= i[1] <= 5:
                    grid[i] = 4
                elif 6 <= i[1] <= 8:
                    grid[i] = 5
            elif 6 <= i[0] <= 8:
                if 0<= i[1] <= 2:
                    grid[i] = 6
                elif 3 <= i[1] <= 5:
                    grid[i] = 7
                elif 6 <= i[1] <= 8:
                    grid[i] = 8
        return grid
    def sol(self):
        if len(self.list_2) == 0:
            return True
        s = copy.deepcopy(self.list_2[0])
        r = s[0]
        c = s[1]

        for j in self.values[s]:
            self.array[r][c] = j
            self.grid_dict_2[self.grid_dict[s]][s] = j
            if self.conditions(s):
                self.list_2.remove(s)
                if self.sol():
                    return True
                self.list_2.insert(0,s)
        self.grid_dict_2[self.grid_dict[s]][s] = 0
        self.array[r][c] = 0
        return False

    def possible_value(self):
        for i in self.list_2:
            self.values[i] = [1,2,3,4,5,6,7,8,9]
            for j in range(1,10):
                self.array[i[0]][i[1]] = j
                if not self.conditions(i):
                    self.values[i].remove(j)
            else:
                self.array[i[0]][i[1]] = 0