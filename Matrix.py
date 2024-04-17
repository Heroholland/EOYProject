class Matrix64:
    def __init__(self):
        self.m = [[]]

    def set_item(self, row, col, val):
        self.m[row][col] = val

    def get_item(self, row, col):
        return self.m[row][col]
    
    def remove_item(self, row, col):
        del self.m[row][col]
