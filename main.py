def infix_to_postfix():
    """Convert infix expression to postfix using a stack"""
    print("\n" + "="*60)
    print("INFIX TO POSTFIX CONVERSION")
    print("="*60)
@@ -37,19 +36,16 @@ def infix_to_postfix():


class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next: 'Node | None' = None
        class SinglyLinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
@@ -60,13 +56,11 @@ def append(self, data):
        current.next = new_node

    def prepend(self, data):
        """Add a node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete first occurrence of a node with given data"""
        if not self.head:
            return
            current = current.next

    def display(self):
        """Display the linked list"""
        if not self.head:
            print("List is empty")
            return
@@ -96,7 +89,6 @@ def display(self):


def singly_linked_list_demo():
    """Demonstrate singly linked list operations"""
    print("\n" + "="*60) 
    def split_evens_odds():
    """Split array into evens and odds"""
    print("\n" + "="*60)
    print("SPLIT EVENS AND ODDS")
    print("="*60)
@@ -156,7 +147,6 @@ def split_evens_odds():


def main():
    """Main menu for array-based sequences project"""
    while True:
        print("\n" + "="*60)
        print("Welcome to Array-Based Sequences Project!")
       
      
  
     
      
            
