class MemTable:

    def __init__(self, max_size=100):

        self.table = {}
        self.max_size = max_size

    def put(self, key, value):

        self.table[key] = value

    def get(self, key):

        return self.table.get(key)

    def delete(self, key):

        self.table[key] = "__TOMBSTONE__"

    def is_full(self):

        return len(self.table) >= self.max_size

    def flush(self):

        items = sorted(self.table.items())
        self.table.clear()
        return items