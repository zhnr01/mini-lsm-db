import os

class SSTable:

    def __init__(self, directory="storage"):
        os.makedirs(directory, exist_ok=True)
        self.dir = directory

    def write(self, data):
        filename = f"{self.dir}/sst_{len(os.listdir(self.dir))}.db"
        sparse_index = {}

        with open(filename, "w") as f:
            offset = 0
            for i, (k, v) in enumerate(data):
                line = f"{k}:{v}\n"
                if i % 10 == 0:
                    sparse_index[k] = offset  # store byte offset for every 10th key
                f.write(line)
                offset += len(line)

        return filename, sparse_index

    def search(self, key, filename, sparse_index):
        # Step 1: Find closest key in sparse index
        keys = sorted(sparse_index.keys())
        start_offset = 0
        for k in keys:
            if k > key:
                break
            start_offset = sparse_index[k]

        # Step 2: Open file and seek to approximate location
        with open(filename, "r") as f:
            f.seek(start_offset)
            for line in f:
                k, v = line.strip().split(":", 1)
                if k == key:
                    return v
                elif k > key:
                    return None  # key not found
        return None