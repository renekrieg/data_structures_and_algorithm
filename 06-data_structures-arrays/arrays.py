class Array():
    def __init__(self):
        self.length = 0
        self.data = []
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f'{self.data}'
    
    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data.append(item)
        self.length+=1
    
    def pop(self):
        self.length-=1
        return self.data.pop()
    
    def delete(self,index):
        self.length-=1
        self.data.remove(self.get(index))
        return self.data
    
newArray = Array()
newArray.push(5)
newArray.push(3)
newArray.push(52)
newArray.push(7)
print(f'Array: {newArray}')
print(f'Length: {len(newArray)}')

newArray.pop()
print(f'Array: {newArray}')
print(f'Length: {len(newArray)}')

newArray.delete(0)
print(f'Array: {newArray}')
print(f'Length: {len(newArray)}')