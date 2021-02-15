# Enter your code here. Read input from STDIN. Print output to STDOUT

# Create the Queue Class

class Queue:
    def __init__(self):
        # Create the 2 stacks
        self.stack_1 = []
        self.stack_2 = []
    #Enqueue
    def enqueue(self, x):
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1[-1])
            self.stack_1.pop()
        self.stack_1.append(x)
        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2[-1])
            self.stack_2.pop()
    #Dequeue
    def dequeue(self):
        if len(self.stack_1) == 0:
            return None
        x = self.stack_1[-1]
        self.stack_1.pop()
        return x
    #Front
    def front(self):
        if len(self.stack_1) == 0:
            return None
        x = self.stack_1[-1]
        print(x)

my_q = Queue()
number_of_q = int(input())
for i in range(number_of_q):
    query = list(input().split())
    if query[0] == "1":
        my_q.enqueue(query[1])
    elif query[0] == "2":
        my_q.dequeue()
    else:
        my_q.front()
        pass


