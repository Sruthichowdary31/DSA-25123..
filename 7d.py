class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

rear = None

def enqueue():
    global rear

    data = int(input("Enter element: "))
    newnode = Node(data)

    if rear is None:
        rear = newnode
        rear.next = rear
    else:
        newnode.next = rear.next
        rear.next = newnode
        rear = newnode

    print("Element inserted")

def dequeue():
    global rear

    if rear is None:
        print("Queue Underflow")
    else:
        front = rear.next

        if rear == front:
            rear = None
        else:
            rear.next = front.next

        print("Deleted element:", front.data)

def peek():
    if rear is None:
        print("Queue is empty")
    else:
        print("Front element:", rear.next.data)

def display():
    if rear is None:
        print("Queue is empty")
    else:
        front = rear.next
        temp = front

        print("Queue:", end=" ")

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == front:
                break

        print()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
