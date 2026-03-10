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
                    sparse_index[k] = offset

                f.write(line)

                offset += len(line)

        return filename, sparse_index