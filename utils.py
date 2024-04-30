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
    

    def read(self):
        pass
    

    
