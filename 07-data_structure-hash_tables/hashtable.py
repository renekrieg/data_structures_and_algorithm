class Hashtable():
    def __init__(self, size):
        self.data = [None] * size
    
    def __hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    
    def set(self, key, value):
        address = self.__hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self.__hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            print(current_bucket)
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        else:
            return []
    
    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                keys_array.append(self.data[i][0][0])
           #keys_array.append(self.data[0][i][0])
        return keys_array
    
    
    def create_hash(self, key):
        return self.__hash(key)
        
a = Hashtable(50)
a.set('apples', 100)
a.set('bananas', 10)
#print(a.get('bananas'))
print(a.keys())