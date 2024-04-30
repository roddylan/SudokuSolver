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
                if len(cells[i][j]) < min_count and len(cells[i][j]) > 1:
                    min_idx = (i, j)
                    min_count = len(cells[i][j])
        
        return min_idx



class Backtracking:
    '''
    Backtracking search for CSP
    '''
    def search(self, grid: Grid, mrv: MRV):
        '''
        Backtrack search implementation
        '''
        if grid.is_solved():
            return grid
        
        i, j = mrv.select(grid)

        for dom in grid.get_cells()[i][j]:
            if grid.is_val_consistent(dom, i, j):
                copy = grid.copy()
                copy.get_cells()[i][j] = dom

            
                if (not AC3().enforce(copy, {(i, j)})): continue

                res = self.search(copy, mrv)
                if res is not False: return res
        
        return False

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

    def enforce_init(self, grid: Grid):
        '''
        Enforce arc consistency for initial grid (since empty cells are given full domain)
        '''
        
        # initialize set
        Q = set()
        w = grid.get_width()
        cells = grid.get_cells()

        for i in range(w):
            for j in range(w):
                if len(cells[i][j]) == 1:
                    Q.add((i,j))

        return self.enforce(grid=grid, Q=Q)

    def enforce(self, grid: Grid, Q: set):
        '''
        Enforce arc consistency
        '''
        while len(Q) != 0:
            row, col = Q.pop()

            row_assigned, row_fail = self.remove_domain_row(grid, row, col)
            col_assigned, col_fail = self.remove_domain_col(grid, row, col)
            ss_assigned, ss_fail = self.remove_domain_ss(grid, row, col)

            if row_fail or col_fail or ss_fail: 
                return False
            
            # Q |= row_assigned | col_assigned | ss_assigned
            Q = Q.union(row_assigned)
            Q = Q.union(col_assigned)
            Q = Q.union(ss_assigned)

        return True

            

    