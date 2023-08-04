class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [None for i in range(array_size)]

    def hash(self, key):
        if isinstance(key, str):
            key_bytes = key.encode()
            hash_code = sum(key_bytes)
            return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = [key, value]

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index] 

        if payload is not None and payload[0] == key:
                return payload[1]
        else:
            return None

       
