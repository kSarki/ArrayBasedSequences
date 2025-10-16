def infix_to_postfix():
    print("\n" + "="*60)
    print("INFIX TO POSTFIX CONVERSION")
    print("="*60)
    
    expression = input("Enter an infix expression (e.g., A+B*C): ").strip()
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()
        elif char in precedence:
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and 
                   precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    result = ''.join(postfix)
    print(f"\nInfix Expression:  {expression}")
    print(f"Postfix Expression: {result}")
    print()


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
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


def singly_linked_list_demo():
    print("\n" + "="*60)
    print("SINGLY LINKED LIST OPERATIONS")
    print("="*60)
    
    sll = SinglyLinkedList()
    
    while True:
        print("\n1. Append (add at end)")
        print("2. Prepend (add at beginning)")
        print("3. Delete")
        print("4. Display")
        print("5. Return to main menu")
        
        choice = input("\nSelect operation (1-5): ").strip()
        
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
            print(f"Deleted '{data}' from the list")
        elif choice == '4':
            print("\nCurrent List:")
            sll.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def split_evens_odds():
    print("\n" + "="*60)
    print("SPLIT EVENS AND ODDS")
    print("="*60)
    
    try:
        numbers_input = input("\nEnter numbers separated by spaces: ").strip()
        numbers = [int(x) for x in numbers_input.split()]
        
        evens = [num for num in numbers if num % 2 == 0]
        odds = [num for num in numbers if num % 2 != 0]
        
        print(f"\nOriginal Array: {numbers}")
        print(f"Even Numbers:   {evens}")
        print(f"Odd Numbers:    {odds}")
        print()
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")


def main():
    while True:
        print("\n" + "="*60)
        print("Welcome to Array-Based Sequences Project!")
        print("\n" + "="*60)
        print("ARRAY-BASED SEQUENCES - THREE PROJECTS")
        print("="*60)
        print()
        print("1. Infix and Postfix Expressions")
        print("2. Singly Linked List")
        print("3. Split Evens-Odds")
        print("4. Exit")
        print()
        
        choice = input("Select a project (1-4): ").strip()
        
        if choice == '1':
            infix_to_postfix()
        elif choice == '2':
            singly_linked_list_demo()
        elif choice == '3':
            split_evens_odds()
        elif choice == '4':
            print("\nThank you for using the Array-Based Sequences Project!")
            print("Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
