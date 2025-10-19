def infix_to_postfix():
    print("\n" + "="*60)
    print("INFIX TO POSTFIX CONVERSION")
    print("="*60)
@@ -37,19 +36,16 @@ def infix_to_postfix():


class Node:
    def __init__(self, data):
        self.data = data
        self.next: 'Node | None' = None
        class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
@@ -60,13 +56,11 @@ def append(self, data):
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
            current = current.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
@@ -96,7 +89,6 @@ def display(self):


def singly_linked_list_demo():
    print("\n" + "="*60) 
    def split_evens_odds():
    print("\n" + "="*60)
    print("SPLIT EVENS AND ODDS")
    print("="*60)
@@ -156,7 +147,6 @@ def split_evens_odds():


def main():
    while True:
        print("\n" + "="*60)
        print("Welcome to Array-Based Sequences Project!")
       
      
  
     
      
            
