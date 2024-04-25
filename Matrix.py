class Matrix64:
    def __init__(self, rows, cols):
        self.m = [[None]*cols]*rows

    def set_item(self, row, col, val):
        self.m[row][col] = val

    def get_item(self, row, col):
        return self.m[row][col]
    
    def remove_item(self, row, col):
        del self.m[row][col]
    
    def get_raw(self):
        return self.m
