import numpy as np
import copy


class Solver():
    def __init__(self,array):
        self.array = array
    
    
    def solve(self):
        list = np.where(self.array != 0)
        self.list = [(list[0][i],list[1][i]) for i in range(len(list[0]))]
        self.grid_dict = self.grid_assign()
        self.grid_dict_2 = {0 : {(i,j) : self.array[i][j] for i in range(3) for j in range(3)},1 : {(i,j) : self.array[i][j] for i in range(3) for j in range(3,6)},2 : {(i,j) : self.array[i][j] for i in range(3) for j in range(6,9)},3 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(3)},4 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(3,6)},5 : {(i,j) : self.array[i][j] for i in range(3,6) for j in range(6,9)},6 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(3)},7 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(3,6)},8 : {(i,j) : self.array[i][j] for i in range(6,9) for j in range(6,9)}}
        b = self.check_all()
        if type(b) == str:
            return b
        self.values = {}
        list_2 = np.where(self.array == 0)
        self.list_2 = [(list_2[0][i],list_2[1][i]) for i in range(len(list_2[0]))]
        self.possible_value()
        self.sol()
        return self.array


    def check_all(self):
        for i in self.list:
            a = self.conditions(i)
            if a == True:continue
            else:return a


    def conditions(self,i):
        #FOR ROWS
        for j in range(9):
            if j == i[1]:
                continue
            elif self.array[i[0],i[1]] == self.array[i[0],j]:
                return f'Row {i[0]+1}'

        #FOR COLUMN
        for j in range(9):
            if j == i[0]:
                continue
            elif self.array[i[0],i[1]] == self.array[j,i[1]]:
                return f'Column {i[1]+1}'

        #FOR GRID
        grid = self.grid_dict_2[self.grid_dict[i]]
        for j in grid.keys():
            if j == i:
                continue
            elif grid[j] == self.array[i[0],i[1]]:
                return f'Grid {self.grid_dict[i]+1}'
        return True
        
        
    def grid_assign(self):
        l = np.where(self.array == self.array)
        l = [(l[0][i],l[1][i]) for i in range(len(l[0]))]
        grid = {}
        for i in l:
            if 0 <= i[0] <= 2:
                if 0 <= i[1] <= 2:
                    grid[i] = 0
                elif 3 <= i[1] <= 5:
                    grid[i] = 1
                elif 6 <= i[1] <= 8:
                    grid[i] = 2
            elif 3 <= i[0] <= 5:
                if 0 <= i[1] <= 2:
                    grid[i] = 3
                elif 3 <= i[1] <= 5:
                    grid[i] = 4
                elif 6 <= i[1] <= 8:
                    grid[i] = 5
            elif 6 <= i[0] <= 8:
                if 0 <= i[1] <= 2:
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
            if self.conditions(s) == True:
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
                
 
if __name__ == "__main__":
    print("Enter In Single Line")
    print("Replace Unsolved bits by 0")
    print("Example : 206000049037009000100700006000580900705000804009062000900004001000300490410000208\n")
    data = input("Enter Unsolved Sudoku : ")

    array = np.array([[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]
                     ],dtype=int)

    n = 0
    for i in range(9):
        for j in range(9):
            array[i][j] = int(data[n])
            n += 1

    solved = Solver(array).solve()
    print(f"\nSolved Sudoku:\n {solved}")
    input("\n\nPress Any Key To Exit!")