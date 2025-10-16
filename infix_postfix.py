class InfixPostfixConverter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operators = set(['+', '-', '*', '/', '^', '(', ')'])
        self.right_associative = set(['^'])
    
    def is_operator(self, char):
        return char in self.operators
    
    def get_precedence(self, op):
        return self.precedence.get(op, 0)
    
    def is_right_associative(self, op):
        return op in self.right_associative
    
    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        
        expression = expression.replace(' ', '')
        
        print(f"\nConverting infix expression: {expression}")
        print(f"{'Step':<6} {'Symbol':<8} {'Stack':<20} {'Postfix':<30}")
        print("-" * 64)
        
        step = 1
        for char in expression:
            if char.isalnum():
                postfix.append(char)
                print(f"{step:<6} {char:<8} {str(stack):<20} {' '.join(postfix):<30}")
            
            elif char == '(':
                stack.append(char)
                print(f"{step:<6} {char:<8} {str(stack):<20} {' '.join(postfix):<30}")
            
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack:
                    stack.pop()
                print(f"{step:<6} {char:<8} {str(stack):<20} {' '.join(postfix):<30}")
            
            elif self.is_operator(char):
                if self.is_right_associative(char):
                    while (stack and stack[-1] != '(' and 
                           self.get_precedence(stack[-1]) > self.get_precedence(char)):
                        postfix.append(stack.pop())
                else:
                    while (stack and stack[-1] != '(' and 
                           self.get_precedence(stack[-1]) >= self.get_precedence(char)):
                        postfix.append(stack.pop())
                stack.append(char)
                print(f"{step:<6} {char:<8} {str(stack):<20} {' '.join(postfix):<30}")
            
            step += 1
        
        while stack:
            postfix.append(stack.pop())
        
        print(f"{'Final':<6} {'':<8} {str(stack):<20} {' '.join(postfix):<30}")
        print("-" * 64)
        
        return ''.join(postfix)
    
    def evaluate_postfix(self, expression):
        stack = []
        
        print(f"\nEvaluating postfix expression: {expression}")
        print(f"{'Step':<6} {'Symbol':<8} {'Stack':<30}")
        print("-" * 44)
        
        step = 1
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
                print(f"{step:<6} {char:<8} {str(stack):<30}")
            
            elif char in self.precedence:
                if len(stack) < 2:
                    print("Error: Invalid postfix expression")
                    return None
                
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                result = 0
                if char == '+':
                    result = operand1 + operand2
                elif char == '-':
                    result = operand1 - operand2
                elif char == '*':
                    result = operand1 * operand2
                elif char == '/':
                    if operand2 == 0:
                        print("Error: Division by zero")
                        return None
                    result = operand1 / operand2
                elif char == '^':
                    result = operand1 ** operand2
                
                stack.append(result)
                print(f"{step:<6} {char:<8} {str(stack):<30}")
            
            step += 1
        
        print("-" * 44)
        
        if len(stack) != 1:
            print("Error: Invalid postfix expression")
            return None
        
        return stack[0]


def run_infix_postfix():
    print("\n" + "="*60)
    print("PROJECT 1: INFIX AND POSTFIX EXPRESSIONS")
    print("="*60)
    
    converter = InfixPostfixConverter()
    
    while True:
        print("\n1. Convert Infix to Postfix")
        print("2. Evaluate Postfix Expression")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            infix = input("\nEnter infix expression (e.g., A+B*C or (A+B)*C): ").strip()
            if infix:
                postfix = converter.infix_to_postfix(infix)
                print(f"\nPostfix Expression: {postfix}")
            else:
                print("Invalid input!")
        
        elif choice == '2':
            postfix = input("\nEnter postfix expression (e.g., 53+82-* or use digits): ").strip()
            if postfix:
                result = converter.evaluate_postfix(postfix)
                if result is not None:
                    print(f"\nResult: {result}")
            else:
                print("Invalid input!")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_infix_postfix()
