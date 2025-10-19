"""
Data Structures Project - Three Parts
Author: Student
Date: October 19, 2025

This project demonstrates three data structure implementations:
1. Stack ADT for Infix to Postfix Conversion
2. Singly Linked List with required operations
3. Split Evens and Odds using node pointer manipulation
"""


# ============================================================================
# PART 1: STACK ADT (for Infix to Postfix Conversion)
# ============================================================================

class Stack:
    """Stack ADT implementation using a list as underlying storage"""
    
    def __init__(self):
        """Initialize an empty stack"""
        self._items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self._items)
    
    def __str__(self):
        """String representation of the stack"""
        return str(self._items)


def infix_to_postfix(expression):
    """
    Convert an infix expression to postfix notation using Stack ADT
    
    Args:
        expression: String containing infix expression
    
    Returns:
        String containing postfix expression
    """
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Create a stack for operators
    operator_stack = Stack()
    postfix = []
    
    # Process each character in the expression
    for char in expression:
        # If operand (letter or digit), add to output
        if char.isalnum():
            postfix.append(char)
        
        # If left parenthesis, push to stack
        elif char == '(':
            operator_stack.push(char)
        
        # If right parenthesis, pop until matching left parenthesis
        elif char == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                postfix.append(operator_stack.pop())
            if not operator_stack.is_empty():
                operator_stack.pop()  # Remove the '('
        
        # If operator
        elif char in precedence:
            # Pop operators with higher or equal precedence
            while (not operator_stack.is_empty() and 
                   operator_stack.peek() != '(' and
                   operator_stack.peek() in precedence and
                   precedence[operator_stack.peek()] >= precedence[char]):
                postfix.append(operator_stack.pop())
            operator_stack.push(char)
    
    # Pop any remaining operators
    while not operator_stack.is_empty():
        postfix.append(operator_stack.pop())
    
    return ''.join(postfix)


def infix_to_postfix_demo():
    """Interactive demo for infix to postfix conversion"""
    print("\n" + "="*60)
    print("PART 1: INFIX TO POSTFIX CONVERSION (Using Stack ADT)")
    print("="*60)
    
    expression = input("\nEnter an infix expression (e.g., A+B*C or (A+B)*C): ").strip()
    
    # Remove spaces from expression
    expression = expression.replace(" ", "")
    
    result = infix_to_postfix(expression)
    
    print(f"\nInfix Expression:   {expression}")
    print(f"Postfix Expression: {result}")
    print()


# ============================================================================
# PART 2: SINGLY LINKED LIST
# ============================================================================

class Node:
    """Node class for singly linked list"""
    
    def __init__(self, data):
        """Initialize a node with data"""
        self.data = data
        self.next: 'Node | None' = None


class SinglyLinkedList:
    """Singly Linked List implementation with required operations"""
    
    def __init__(self):
        """Initialize an empty linked list"""
        self.head = None
    
    def append(self, data):
        """Add a node with data at the end of the list"""
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end and add new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add a node with data at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete the first occurrence of a node with the given data"""
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        
        # If head node contains the data
        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted first occurrence of '{data}'")
            return
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print(f"Deleted first occurrence of '{data}'")
                return
            current = current.next
        
        print(f"'{data}' not found in the list")
    
    def remove_all(self, data):
        """Remove all occurrences of nodes with the given data"""
        if not self.head:
            print("List is empty. Nothing to remove.")
            return
        
        count = 0
        
        # Remove all occurrences from the head
        while self.head and self.head.data == data:
            self.head = self.head.next
            count += 1
        
        # Remove all occurrences from the rest of the list
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                count += 1
            else:
                current = current.next
        
        if count > 0:
            print(f"Removed {count} occurrence(s) of '{data}'")
        else:
            print(f"'{data}' not found in the list")
    
    def reverse_display(self):
        """Display the list in reverse order using a Stack"""
        if not self.head:
            print("List is empty")
            return
        
        # Use Stack ADT to reverse the display
        stack = Stack()
        
        # Push all elements onto the stack
        current = self.head
        while current:
            stack.push(current.data)
            current = current.next
        
        # Pop all elements to display in reverse
        elements = []
        while not stack.is_empty():
            elements.append(str(stack.pop()))
        
        print("Reverse: " + " -> ".join(elements))
    
    def display(self):
        """Display the list from head to tail"""
        if not self.head:
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Forward: " + " -> ".join(elements))


def singly_linked_list_demo():
    """Interactive demo for singly linked list operations"""
    print("\n" + "="*60)
    print("PART 2: SINGLY LINKED LIST OPERATIONS")
    print("="*60)
    
    sll = SinglyLinkedList()
    
    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Append (add at end)")
        print("2. Prepend (add at beginning)")
        print("3. Delete (first occurrence)")
        print("4. Remove All (all occurrences)")
        print("5. Display (forward)")
        print("6. Reverse Display (using stack)")
        print("7. Return to main menu")
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '1':
            data = input("Enter data to append: ").strip()
            sll.append(data)
            print(f"Appended '{data}' to the list")
        
        elif choice == '2':
            data = input("Enter data to prepend: ").strip()
            sll.prepend(data)
            print(f"Prepended '{data}' to the list")
        
        elif choice == '3':
            data = input("Enter data to delete: ").strip()
            sll.delete(data)
        
        elif choice == '4':
            data = input("Enter data to remove all occurrences: ").strip()
            sll.remove_all(data)
        
        elif choice == '5':
            sll.display()
        
        elif choice == '6':
            sll.reverse_display()
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please select 1-7.")


# ============================================================================
# PART 3: SPLIT EVENS AND ODDS (Using Node Pointer Manipulation)
# ============================================================================

class EvenOddLinkedList:
    """Special linked list for splitting evens and odds"""
    
    def __init__(self):
        """Initialize an empty linked list"""
        self.head = None
    
    def append(self, data):
        """Add a node with data at the end of the list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def split_evens_odds(self):
        """
        Split the list into two lists (evens and odds) using node pointer manipulation.
        This method does NOT use arrays - it manipulates node pointers directly.
        
        Returns:
            Tuple of (even_list, odd_list)
        """
        if not self.head:
            return EvenOddLinkedList(), EvenOddLinkedList()
        
        # Create two new empty lists
        even_list = EvenOddLinkedList()
        odd_list = EvenOddLinkedList()
        
        # Pointers to track the last node in each new list
        even_tail: Node | None = None
        odd_tail: Node | None = None
        
        # Traverse the original list
        current = self.head
        while current:
            # Save the next pointer before we modify current.next
            next_node = current.next
            
            # Disconnect the current node
            current.next = None
            
            # Determine if the value is even or odd and add to appropriate list
            if current.data % 2 == 0:
                # Even number - add to even list
                if not even_list.head:
                    even_list.head = current
                    even_tail = current
                else:
                    if even_tail:
                        even_tail.next = current
                    even_tail = current
            else:
                # Odd number - add to odd list
                if not odd_list.head:
                    odd_list.head = current
                    odd_tail = current
                else:
                    if odd_tail:
                        odd_tail.next = current
                    odd_tail = current
            
            # Move to the next node in the original list
            current = next_node
        
        return even_list, odd_list
    
    def display(self):
        """Display the list"""
        if not self.head:
            print("[]")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("[" + ", ".join(elements) + "]")


def split_evens_odds_demo():
    """Interactive demo for splitting evens and odds"""
    print("\n" + "="*60)
    print("PART 3: SPLIT EVENS AND ODDS (Node Pointer Manipulation)")
    print("="*60)
    print("This implementation uses node pointer manipulation,")
    print("NOT arrays or list comprehensions.")
    print("="*60)
    
    try:
        numbers_input = input("\nEnter integers separated by spaces: ").strip()
        numbers = [int(x) for x in numbers_input.split()]
        
        # Create a linked list with the numbers
        original_list = EvenOddLinkedList()
        for num in numbers:
            original_list.append(num)
        
        print("\nOriginal Linked List:")
        original_list.display()
        
        # Split into evens and odds using node pointer manipulation
        even_list, odd_list = original_list.split_evens_odds()
        
        print("\nEven Numbers Linked List:")
        even_list.display()
        
        print("\nOdd Numbers Linked List:")
        odd_list.display()
        print()
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
        print()


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main menu for the three-part data structures project"""
    while True:
        print("\n" + "="*60)
        print("DATA STRUCTURES PROJECT - THREE PARTS")
        print("="*60)
        print()
        print("1. Stack ADT - Infix to Postfix Conversion")
        print("2. Singly Linked List Operations")
        print("3. Split Evens and Odds (Node Pointer Manipulation)")
        print("4. Exit")
        print()
        
        choice = input("Select a project (1-4): ").strip()
        
        if choice == '1':
            infix_to_postfix_demo()
        elif choice == '2':
            singly_linked_list_demo()
        elif choice == '3':
            split_evens_odds_demo()
        elif choice == '4':
            print("\nThank you for using the Data Structures Project!")
            print("Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
