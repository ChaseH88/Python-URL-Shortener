class Store:
    def __init__(self):
        self.key_value_store = {}

    def add(self, key, value):
        if key not in self.key_value_store and len(key) > 0:
            self.key_value_store[key] = value

    def getKey(self, key):
        return self.key_value_store.get(key, None)
    
    def getValue(self, value):
        for k, v in self.key_value_store.items():
            if v == value:
                return k
        return None
    
    def getStore(self):
        return self.key_value_store
    
    def delete(self, key):
        if key in self.key_value_store:
            del self.key_value_store[key]

store = Store()
