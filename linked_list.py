class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning")
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            print(f"Inserted {data} at the end (first node)")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        print(f"Inserted {data} at the end")
    
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position! Position must be >= 1")
            return
        
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {position}")
            return
        
        current = self.head
        count = 1
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print(f"Position {position} is out of range!")
            return
        
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}")
    
    def delete_from_beginning(self):
        if self.is_empty():
            print("List is empty! Cannot delete.")
            return
        
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning")
    
    def delete_from_end(self):
        if self.is_empty():
            print("List is empty! Cannot delete.")
            return
        
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted {deleted_data} from the end")
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        print(f"Deleted {deleted_data} from the end")
    
    def delete_by_value(self, value):
        if self.is_empty():
            print("List is empty! Cannot delete.")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value} from the list")
            return
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                print(f"Deleted {value} from the list")
                return
            current = current.next
        
        print(f"Value {value} not found in the list")
    
    def search(self, value):
        if self.is_empty():
            print("List is empty!")
            return False
        
        current = self.head
        position = 1
        
        while current:
            if current.data == value:
                print(f"Value {value} found at position {position}")
                return True
            current = current.next
            position += 1
        
        print(f"Value {value} not found in the list")
        return False
    
    def display(self):
        if self.is_empty():
            print("List is empty!")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Linked List: " + " -> ".join(elements) + " -> None")
    
    def get_length(self):
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count


def run_linked_list():
    print("\n" + "="*60)
    print("PROJECT 2: SINGLY LINKED LIST")
    print("="*60)
    
    linked_list = SinglyLinkedList()
    
    while True:
        print("\n1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete from Beginning")
        print("5. Delete from End")
        print("6. Delete by Value")
        print("7. Search for Value")
        print("8. Display List")
        print("9. Get Length")
        print("10. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-10): ").strip()
        
        if choice == '1':
            try:
                data = int(input("Enter value to insert: "))
                linked_list.insert_at_beginning(data)
                linked_list.display()
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '2':
            try:
                data = int(input("Enter value to insert: "))
                linked_list.insert_at_end(data)
                linked_list.display()
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '3':
            try:
                data = int(input("Enter value to insert: "))
                position = int(input("Enter position: "))
                linked_list.insert_at_position(data, position)
                linked_list.display()
            except ValueError:
                print("Invalid input! Please enter numbers.")
        
        elif choice == '4':
            linked_list.delete_from_beginning()
            linked_list.display()
        
        elif choice == '5':
            linked_list.delete_from_end()
            linked_list.display()
        
        elif choice == '6':
            try:
                value = int(input("Enter value to delete: "))
                linked_list.delete_by_value(value)
                linked_list.display()
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '7':
            try:
                value = int(input("Enter value to search: "))
                linked_list.search(value)
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '8':
            linked_list.display()
        
        elif choice == '9':
            length = linked_list.get_length()
            print(f"Length of the list: {length}")
        
        elif choice == '10':
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-10.")


if __name__ == "__main__":
    run_linked_list()
