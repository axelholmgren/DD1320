class DictHash:
    def __init__(self):
        self.table = {}

    def store(self, nyckel, data):
        self.table[hash(nyckel)] = data

    def search(self, nyckel):
        try:
            return self.table[hash(nyckel)]
        except KeyError:
            return "finns inte"

    def __contains__(self, nyckel):
        try:
            self.table[hash(nyckel)]
            return True
        except KeyError:
            return False
