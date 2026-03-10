import json
import os

class WAL:

    def __init__(self, path="wal.log"):
        self.path = path

    def append(self, key, value):

        record = {"k": key, "v": value}

        with open(self.path, "a") as f:
            f.write(json.dumps(record) + "\n")

    def recover(self):

        data = {}

        if not os.path.exists(self.path):
            return data

        with open(self.path) as f:
            for line in f:
                record = json.loads(line)
                data[record["k"]] = record["v"]

        return data