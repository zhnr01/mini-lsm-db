import hashlib

class BloomFilter:

    def __init__(self, size=10000):

        self.size = size
        self.bits = [0] * size

    def _hash(self, key):

        h = hashlib.md5(key.encode()).hexdigest()
        return int(h, 16) % self.size

    def add(self, key):

        index = self._hash(key)
        self.bits[index] = 1

    def might_contain(self, key):

        index = self._hash(key)
        return self.bits[index] == 1