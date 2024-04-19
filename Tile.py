class Tile(Matrix64):
    def __init__(self, purchaser_id, database):
        self.purchaser_id = purchaser_id
        self.db = database