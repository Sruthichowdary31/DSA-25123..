tree = [None] * 10

def insert(value):
    for i in range(len(tree)):
        if tree[i] is None:
            tree[i] = value
            return
    print("Tree is full")

def display():
    print("Binary Tree using Array:")
    for i in range(len(tree)):
        if tree[i] is not None:
            print(tree[i], end=" ")
    print()

insert(10)
insert(20)
insert(30)
insert(40)
insert(50)

display()
