import matplotlib.pyplot as plt
import numpy as np
from utils import Grid

class MRV:
    def select(self, grid: Grid):
        '''
        MRV 
        '''
        cells = grid.get_cells()
        min_idx = (-1, -1) # coord
        min_count = 10e9


        for i in range(grid.get_width()):
            for j in range(grid.get_width()):
                if cells[i][j] < min_count:
                    min_idx = (i, j)
                    min_count = cells[i][j]
        
        return min_idx



class Backtracking:
    '''
    Backtracking search for CSP
    '''
    def search(self, grid, ):
        '''
        Backtrack search implementation
        '''
        pass


class AC3:
    '''
    AC3 enforcement
    '''
    def remove_domain_row(self):
        '''
        Remove domain value from row 
        '''
        pass


    def remove_domain_col(self):
        '''
        Remove domain value from col
        '''
        pass


    def remove_domain_ss(self):
        '''
        Remove domain value from subsection
        '''
        pass

    def enforce_init(self):
        '''
        Enforce arc consistency for initial grid (since empty cells are given full domain)
        '''
        pass

    def enforce(self):
        '''
        Enforce arc consistency for other grids
        '''
        pass

    