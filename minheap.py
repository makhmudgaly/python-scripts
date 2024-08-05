class MinHeap:
    def __init__(self) -> None:
        self.length = 0
        self.data = []
    
    def insert(self, value):
        self.data[self.length] = value
        self.__heapifyUp(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            return None
        
        out = self.data[0]
        self.length -= 1

        if self.length == 0:
            self.data = []
            return out
        
        
        self.data[0] = self.data[self.length]
        self.__heapifyDown(0)
        return out

    def __parent(self, idx):
        return (idx-1) // 2
    
    def __leftChild(self, idx):
        return (2*idx) + 1
    
    def __rightChild(self, idx):
        return (2*idx) + 2
    
    def __heapifyUp(self,idx):
        if idx == 0:
            return
        
        parent = self.__parent(idx)
        parent_value = self.data[parent]
        current_value = self.data[idx]

        if parent_value > current_value:
            self.data[idx] = parent_value
            self.data[parent] = current_value
            self.__heapifyUp(parent)

    def __heapifyDown(self, idx):
        if idx >= self.length:
            return
        
        left_idx = self.__leftChild(idx)
        right_idx = self.__rightChild(idx)
        left_val = self.data[left_idx]
        right_val = self.data[right_idx]
        curr_val = self.data[idx]

        if left_val > right_val and curr_val > right_val:
            self.data[right_idx] = curr_val
            self.data[idx] = right_val
            self.__heapifyDown(right_idx)
        elif right_val > left_val and curr_val > left_val:
            self.data[left_idx] = curr_val
            self.data[idx] = left_val
            self.__heapifyDown(left_val)

        if left_idx >= self.length:
            return