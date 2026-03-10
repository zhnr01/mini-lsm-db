from wal import WAL
from memtable import MemTable
from sstable import SSTable

class MiniLSM:

    def __init__(self):

        self.wal = WAL()
        self.memtable = MemTable()
        self.sstable = SSTable()

        self.sstables = []
        self.indexes = []

    def put(self, key, value):

        self.wal.append(key, value)
        self.memtable.put(key, value)

        if self.memtable.is_full():
            self.flush()

    def get(self, key):

        value = self.memtable.get(key)

        if value:
            return value

        for i in reversed(range(len(self.sstables))):

            file = self.sstables[i]
            index = self.indexes[i]

            result = search_sstable(file, index, key)

            if result:
                return result

        return None

    def flush(self):

        data = self.memtable.flush()

        file, index = self.sstable.write(data)

        self.sstables.append(file)
        self.indexes.append(index)


def search_sstable(file, sparse_index, key):

    keys = sorted(sparse_index.keys())

    start_key = None

    for k in keys:
        if k <= key:
            start_key = k
        else:
            break

    if start_key is None:
        return None

    offset = sparse_index[start_key]

    with open(file) as f:

        f.seek(offset)

        for line in f:

            k, v = line.strip().split(":")

            if k == key:
                return v

            if k > key:
                return None