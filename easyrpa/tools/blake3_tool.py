import blake3

# pip install blake3

class Blake3Tool:
    def __init__(self, salt=None, key=None, encoding='utf-8'):
        self.salt = salt
        self.key = key
        self.encoding = encoding

    def hash(self, data):
        if self.salt:
            data = self.salt + data
        if self.key:
            data = self.key + data
        return blake3.blake3(data.encode(self.encoding)).hexdigest()

    def hash_bytes(self, data):
        if self.salt:
            data = self.salt + data
        if self.key:
            data = self.key + data
        return blake3.blake3(data).digest()

    def verify(self, data, hash_value):
        return self.hash(data) == hash_value

    def verify_bytes(self, data, hash_value):
        return self.hash_bytes(data) == hash_value

    def update(self, data, hash_value):
        return blake3.blake3(data.encode(self.encoding), hash_value=hash_value).hexdigest()

    def update_bytes(self, data, hash_value):
        return blake3.blake3(data, hash_value=hash_value).digest()

# 示例使用
tool = Blake3Tool(salt='my_salt', key='my_key')
data = 'Hello, World!'
hash_value = tool.hash(data)
print(hash_value)

# tool.verify(data, hash_value)

# tool.update(data, hash_value)