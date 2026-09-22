# Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        self.head = None

        if n <= 0:
            print("List created as empty.")
            return

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

        print("Circular linked list created successfully.")

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print("Node inserted at beginning.")
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print("Node inserted at end.")
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

        print("Node inserted at end.")

    # 4. Insert at specific index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter value: "))

        if index < 0:
            print("Invalid index.")
            return

        # Insert at beginning
        if index == 0:
            new_node = Node(data)

            # Empty list
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                print("Node inserted successfully.")
                return

            # Find last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

            print("Node inserted successfully.")
            return

        # If list is empty, other indexes are invalid
        if self.head is None:
            print("Index out of range.")
            return

        temp = self.head

        # Move to node before required index
        for _ in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range.")
                return

        # If index is beyond the end
        if temp.next == self.head and index > 0:
            # index == current number of nodes means insert at end
            new_node = Node(data)
            new_node.next = self.head
            temp.next = new_node

            print("Node inserted successfully.")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted successfully.")

    # 5. Delete by value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty.")
            return

        # If first node contains the value
        if self.head.data == value:
            self.delete_first()
            return

        prev = self.head
        current = self.head.next

        while current != self.head:
            if current.data == value:
                prev.next = current.next
                print("Node deleted successfully.")
                return

            prev = current
            current = current.next

        print("Value not found.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("First node deleted successfully.")
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

        print("First node deleted successfully.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("Last node deleted successfully.")
            return

        prev = self.head
        current = self.head.next

        while current.next != self.head:
            prev = current
            current = current.next

        prev.next = self.head

        print("Last node deleted successfully.")

    # 8. Count number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Circular Linked List:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main Program
linked_list = CircularLinkedList()

while True:
    print("\n========== CIRCULAR LINKED LIST ==========")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")
    print("===========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.create()

    elif choice == 2:
        linked_list.insert_beginning()

    elif choice == 3:
        linked_list.insert_end()

    elif choice == 4:
        linked_list.insert_at_index()

    elif choice == 5:
        linked_list.delete_by_value()

    elif choice == 6:
        linked_list.delete_first()

    elif choice == 7:
        linked_list.delete_last()

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.display()

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
