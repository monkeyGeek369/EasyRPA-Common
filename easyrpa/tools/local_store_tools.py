cache = {}

def add_data(key: str, value):
    cache[key] = value

def update_data(key: str, value):
    if key in cache:
        cache[key] = value
    else:
        add_data(key, value)

def delete_data(key:str):
    if key in cache:
        del cache[key]

def get_data(key:str):
    return cache.get(key)