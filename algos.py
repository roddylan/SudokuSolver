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
    def remove_domain_row(self, grid: Grid, row, col):
        '''
        Remove domain values of (row, col) from row 

        Returns:
            Assigned variable indexes
            True if row element already fully assigned (ie. cur. val already assigned in row); False otherwise
        '''
        assigned = []
        cells = grid.get_cells()
        for i in range(grid.get_width()):
            if i == col: continue
            # remove domain
            new_domain = cells[row][i].replace(cells[row][col], '')

            if len(new_domain) == 0:
                return None, True
            
            if len(new_domain) == 1 and len(cells[row][i]) > 1:
                assigned.append((row, i)) # add index of cell with the current value in its domain

            cells[row][i] = new_domain
        
        return assigned, False


            


    def remove_domain_col(self, grid: Grid, row, col):
        '''
        Remove domain values of (row, col) from column

        Returns:
            Assigned variable indexes
            True if column element already fully assigned (ie. cur. val already assigned in column); False otherwise
        '''
        assigned = []
        cells = grid.get_cells()
        for i in range(grid.get_width()):
            if i == row: continue
            # remove domain
            new_domain = cells[i][col].replace(cells[row][col], '')

            if len(new_domain) == 0:
                return None, True
            
            if len(new_domain) == 1 and len(cells[i][col]) > 1:
                assigned.append((i, col)) # add index of cell with the current value in its domain

            cells[i][col] = new_domain
        
        return assigned, False


    def remove_domain_ss(self, grid: Grid, row, col):
        '''
        Remove domain values of (row, col) from subsection

        Returns:
            Assigned variable indexes
            True if column element already fully assigned (ie. cur. val already assigned in subsection); False otherwise
        '''
        assigned = []
        cells = grid.get_cells()

        row_init = (row // grid.n_sect) * grid.w_sec
        col_init = (col // grid.n_sect) * grid.w_sec

        for i in range(row_init, row_init + grid.w_sec):
            for j in range(col_init, col_init + grid.w_sec):
                if i == row and j == col: continue

                new_domain = cells[i][j].replace(cells[row][col], '')

                if len(new_domain) == 0:
                    return None, True
                
                if len(new_domain) == 1 and len(cells[i][j]) > 1:
                    assigned.append((i, j))

                cells[i][j] = new_domain
        
        return assigned, False

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

    