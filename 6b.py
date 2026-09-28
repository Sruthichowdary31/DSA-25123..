class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

stack = None

def push():
    global stack
    data = int(input("Enter element: "))
    newnode = Node(data)
    newnode.next = stack
    stack = newnode
    print("Element pushed")

def pop():
    global stack
    if stack is None:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.data)
        stack = stack.next

def peek():
    if stack is None:
        print("Stack is empty")
    else:
        print("Top element:", stack.data)

def display():
    if stack is None:
        print("Stack is empty")
    else:
        temp = stack
        print("Stack:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
