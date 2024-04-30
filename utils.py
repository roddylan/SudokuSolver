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
    
    


class SudokuGenerator:
    '''
    Sudoku generator
    '''
    def __init__(self, domain='123456789', w=9):
        self.d = domain
        self.w = w


    def generate(self):
        pass
    
