class Stack:
    def __init__(self):
        self.stack = []

    def sizeStack(self):
        return len(self.stack)
	
		
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack):
            val=self.stack[-1]
            del self.stack[-1]
            return val
        else:
            print("Stack is Empty")
    
    def peek(self):
        if len(self.stack):
            return self.stack[-1]
	
    def display(self):
        s=""
        i=len(self.stack)
        for i in range(i-1,-1,-1):
            s=s+str(self.stack[i])
        print(s)

stack = Stack()
stack1=Stack()

k=int(input("Enter a number: "))
while(k):
    dig=k%10
    stack.push(dig)
    k=k//10

while stack.sizeStack():
    a=stack.pop()
    stack1.push(a)

stack1.display()





