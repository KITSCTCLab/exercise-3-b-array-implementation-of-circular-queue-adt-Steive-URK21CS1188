class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.size = size
        self.queue = [None]*size
        self.rear = -1
        self.front = -1
    def enqueue(self, value: int) -> bool:
        # Write code here
        if not self.is_full():
            if self.front==-1:
                self.front=0
                self.rear=0
            else:
                if self.rear==self.size-1:
                    self.rear=0
                else:
                    self.rear+=1
            self.queue[self.rear]=value
    def dequeue(self) -> bool:
        # Write code here
        if not self.is_empty():
            r=self.queue[0]
            del self.queue[0]
            self.front+=1
            return r
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                if self.front==self.size-1:
                    self.front=0
                else:
                    self.front=(self.front+1)%self.size
        
    def get_front(self) -> int:
        # Write code here
        return self.front
    def get_rear(self):
        # Write code here
        return self.rear
    def is_empty(self):
        # Write code here
        if self.front==-1:
            return 1
        else:
            return 0
    def is_full(self):
        # Write code here
        if (self.rear==(self.size-1) and self.front==0) or (self.front==self.rear+1):
            return 1
        else:
            return 0

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
