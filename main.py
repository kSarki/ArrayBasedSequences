import infix_postfix
import linked_list
import split_evens_odds


def print_main_menu():
    print("\n" + "="*60)
    print("ARRAY-BASED SEQUENCES - THREE PROJECTS")
    print("="*60)
    print("\n1. Infix and Postfix Expressions")
    print("2. Singly Linked List")
    print("3. Split Evens-Odds")
    print("4. Exit")


def main():
    print("\nWelcome to Array-Based Sequences Project!")
    
    while True:
        print_main_menu()
        
        choice = input("\nSelect a project (1-4): ").strip()
        
        if choice == '1':
            infix_postfix.run_infix_postfix()
        
        elif choice == '2':
            linked_list.run_linked_list()
        
        elif choice == '3':
            split_evens_odds.run_split_evens_odds()
        
        elif choice == '4':
            print("\nThank you for using Array-Based Sequences Project!")
            print("Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1-4.")


if __name__ == "__main__":
    main()
