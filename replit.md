# Array-Based Sequences - Three Projects

## Overview
This Python project contains three distinct implementations of array-based sequence algorithms:
1. **Infix and Postfix Expressions** - Expression conversion and evaluation
2. **Singly Linked List** - Complete linked list data structure implementation
3. **Split Evens-Odds** - Array partitioning algorithms

## Project Structure
```
.
├── main.py                 # Main menu system to run each project
├── infix_postfix.py       # Project 1: Infix/Postfix converter and evaluator
├── linked_list.py         # Project 2: Singly linked list implementation
├── split_evens_odds.py    # Project 3: Even/odd splitting algorithms
└── replit.md             # This file
```

## Features

### Project 1: Infix and Postfix Expressions
- Convert infix expressions to postfix notation using stack-based algorithm
- Evaluate postfix expressions with step-by-step visualization
- Support for operators: +, -, *, /, ^ (power)
- Handles operator precedence and parentheses
- Shows stack state at each step

### Project 2: Singly Linked List
- Insert operations: beginning, end, at position
- Delete operations: from beginning, from end, by value
- Search for values with position tracking
- Display entire list
- Get list length
- Complete error handling for edge cases

### Project 3: Split Evens-Odds
- Three different algorithms:
  1. Split into separate arrays (evens and odds)
  2. In-place split using two-pointer approach
  3. Partition array in single pass
- Step-by-step visualization of each algorithm
- Performance comparison of different approaches

## Usage
Run the main program:
```bash
python main.py
```

The main menu allows you to select which project to run. Each project has its own submenu with various operations.

## Recent Changes
- **October 16, 2025**: Initial project creation
  - Implemented all three array-based sequence projects
  - Added comprehensive error handling
  - Created interactive menu systems
  - Added step-by-step algorithm visualizations

## Technical Details
- **Language**: Python 3.11
- **Dependencies**: None (uses only Python standard library)
- **Architecture**: Modular design with separate files for each project
- **Data Structures**: Arrays, stacks, linked lists

## Algorithm Complexity

### Infix to Postfix Conversion
- Time Complexity: O(n) where n is the length of expression
- Space Complexity: O(n) for the stack

### Linked List Operations
- Insert/Delete at beginning: O(1)
- Insert/Delete at end: O(n)
- Search: O(n)

### Split Evens-Odds
- Separate arrays: O(n) time, O(n) space
- In-place split: O(n) time, O(1) space
- Partition: O(n) time, O(1) space
