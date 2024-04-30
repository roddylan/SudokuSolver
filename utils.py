import numpy as np

class Grid:
    '''
    Grid object.
    Representation for sudoku grid
    '''

    def __init__(self, cells=[], domain='123456789', w=9):
        '''
        cells: w * w sized array with sudoku entries
        domain: possible values
        width: sudoku board width
        '''
        self.cells = cells
        self.domain = domain
        self.width = w
        self.n_sect = int(np.sqrt(self.width))
        self.w_sec = self.width // self.n_sect


    def copy(self):
        '''
        Return copy of Grid object
        '''
        temp = Grid()
        temp.cells = [row.copy() for row in self.cells]
        return temp
    

    def get_cells(self):
        '''
        Getter for cell attribute
        '''
        return self.cells
    
    def get_width(self):
        '''
        Getter for width attribute
        '''
        return self.width
    
    def get_dom(self):
        '''
        Getter for domain attribute
        '''
        return self.domain
    

    def read(self, sudoku: str):
        '''
        Read sudoku string and build cells.
        '.' represents empty cell

        Each resulting cell contains initial possible values
        '''
        i = 0
        row = []
        for c in sudoku:
            if c == '.':
                row.append(self.domain)
            else:
                row.append(c)
            
            i += 1
            if i % self.width:
                self.cells.append(row)
                row = []
    
    def print(self):
        '''
        Print board representation
        '''

        # n_sect = int(np.sqrt(self.width))
        n_border = self.n_sect + 1

        for _ in range(self.width + n_border):
            print("-", end=" ")
        print()

        for i in range(self.width):
            # row
            print("|", end=" ")
            
            for j in range(self.width):
                # col
                if len(self.cells[i][j]) == 1:
                    print(self.cells[i][j], end=" ")
                elif len(self.cells[i][j]) > 1:
                    print(".", end=" ")
                else:
                    print(";", end=" ")
                
                if (j+1) % self.n_sect == 0:
                    print("|", end=" ")
            print()

            if (i+1) % self.n_sect == 0:
                for _ in range(self.width + n_border):
                    print("-", end=" ")
                print()

        print()

    def print_possible(self):
        for row in self.cells:
            print(row)



    def is_val_consistent(self, val, row, col):
        '''
        True if value is arc consistent
        '''

        # row constraint
        for i in range(self.width):
            if i == col: continue
            if self.cells[row][i] == val:
                return False
        
        # column constraint
        for i in range(self.width):
            if i == row: continue
            if self.cells[i][col] == val:
                return False
            

        # subsection constraint
        # w_sec = self.width // self.n_sect
        w_sec = self.w_sec

        row_init = (row // self.n_sect) * w_sec
        col_init = (col // self.n_sect) * w_sec

        
        for i in range(row_init, row_init + w_sec):
            for j in range(col_init, col_init + w_sec):
                if i == row and j == col: continue
                if self.cells[i][j] == val:
                    return False
        
        return True


    def is_solved(self):
        '''
        Return True if solved; False otherwise
        '''
        for i in range(self.width):
            for j in range(self.width):
                if len(self.cells[i][j]) > 1 or not self.is_val_consistent(self.cells[i][j], i, j):
                    return False
                
        return True

class SudokuGenerator:
    '''
    Sudoku generator
    '''
    def __init__(self, domain='123456789', w=9):
        self.d = domain
        self.w = w


    def generate(self):
        pass
    
