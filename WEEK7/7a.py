queue = []

def enqueue():
    item = int(input("Enter element: "))
    queue.append(item)
    print("Element inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))

def peek():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

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
