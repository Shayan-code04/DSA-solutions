# ==========================================
# Linked List Implementation from Scratch
# File: linked_list.py
# ==========================================


# -----------------------------
# Node Class
# -----------------------------
class Node:
    def __init__(self, data):
        # Store the actual value
        self.data = data

        # Pointer to the next node
        # Initially it points to nothing
        self.next = None


# -----------------------------
# Linked List Class
# -----------------------------
class LinkedList:
    def __init__(self):
        # Head points to the first node
        # Empty list => head is None
        self.head = None

    # -------------------------
    # Add node at the end
    # -------------------------
    def append(self, data):

        # Create a new node
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Start from the first node
        current = self.head

        # Move until the last node
        while current.next:
            current = current.next

        # Connect last node to new node
        current.next = new_node

    # -------------------------
    # Add node at the beginning
    # -------------------------
    def prepend(self, data):

        # Create a new node
        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # Update head
        self.head = new_node

    # -------------------------
    # Delete first occurrence
    # -------------------------
    def delete(self, value):

        # Empty list
        if self.head is None:
            return

        # If head contains the value
        if self.head.data == value:
            self.head = self.head.next
            return

        # Start from head
        current = self.head

        # Search for the node before the target
        while current.next:

            if current.next.data == value:

                # Skip the node to delete
                current.next = current.next.next
                return

            current = current.next

    # -------------------------
    # Print the linked list
    # -------------------------
    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # -------------------------
    # Count number of nodes
    # -------------------------
    def length(self):

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# ==========================================
# Testing
# ==========================================

ll = LinkedList()

print("Append 10")
ll.append(10)
ll.display()

print("\nAppend 20")
ll.append(20)
ll.display()

print("\nAppend 30")
ll.append(30)
ll.display()

print("\nPrepend 5")
ll.prepend(5)
ll.display()

print("\nDelete 20")
ll.delete(20)
ll.display()

print("\nLength of Linked List")
print(ll.length())