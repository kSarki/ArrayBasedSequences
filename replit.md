# Data Structures Project - Three Parts

## Project Overview
This project implements three data structure assignments in a single Python file with a menu-driven interface.

## Project Components

### Part 1: Stack ADT for Infix to Postfix Conversion
- **Implementation**: Custom Stack class with push, pop, peek, is_empty, and size methods
- **Purpose**: Converts infix expressions (e.g., A+B*C) to postfix notation (ABC*+)
- **Key Features**:
  - Proper Stack ADT class (not using Python list directly)
  - Handles operator precedence
  - Supports parentheses

### Part 2: Singly Linked List
- **Implementation**: Node class and SinglyLinkedList class
- **Required Operations**:
  - `append(data)` - Add node at the end
  - `prepend(data)` - Add node at the beginning
  - `delete(data)` - Delete first occurrence of a value
  - `remove_all(data)` - Remove all occurrences of a value
  - `display()` - Show list forward
  - `reverse_display()` - Show list in reverse using Stack ADT
- **Key Feature**: reverse_display uses the Stack ADT from Part 1

### Part 3: Split Evens and Odds
- **Implementation**: EvenOddLinkedList class with node pointer manipulation
- **Purpose**: Split a linked list into two separate lists (even numbers and odd numbers)
- **Key Features**:
  - Uses node pointer manipulation (NOT arrays)
  - Relinks nodes by manipulating .next pointers
  - Does not use list comprehensions or array-based methods
  - Creates two new linked lists from the original

## How to Run
Click the "Run" button or execute `python main.py` in the console.

## Project Structure
- **main.py**: Single file containing all three parts with menu system
- Classes implemented:
  - Stack (for Part 1 and used in Part 2)
  - Node (for linked lists)
  - SinglyLinkedList (for Part 2)
  - EvenOddLinkedList (for Part 3)

## Testing Each Part
1. Select option 1 to test infix to postfix conversion
2. Select option 2 to test linked list operations (includes all required methods)
3. Select option 3 to test splitting evens and odds using node manipulation

## Key Requirements Met
✓ Stack ADT implementation (not just Python list)
✓ Modular, class-based design
✓ All required linked list methods
✓ reverse_display uses Stack
✓ Split evens/odds uses node pointer manipulation (not arrays)
✓ Menu-driven interface
✓ Proper documentation and comments

Last Updated: October 19, 2025
