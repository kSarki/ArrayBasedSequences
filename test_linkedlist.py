from main import Stack, SinglyLinkedList, Node, SplitEvensOdds


postfix = [
    "5 3 +", "8 2 - 3 +", "5 3 8 * +", "6 2 / 3 +", "5 8 + 3 -",
    "5 3 + 8 *", "8 2 3 * + 6 -", "5 3 8 * + 2 /", "8 2 + 3 6 * -", "5 3 + 8 2 / -"
]

def evaluate_postfix(expr):
    stack = Stack()
    tokens = expr.split()
    for t in tokens:
        if t.isdigit():
            stack.push(int(t))
        else:
            b = stack.pop()
            a = stack.pop()
            if t == '+': stack.push(a + b)
            elif t == '-': stack.push(a - b)
            elif t == '*': stack.push(a * b)
            elif t == '/': stack.push(a / b)
    return stack.pop()

print("----- Postfix Evaluator -----")
for expr in postfix:
    print(f"[{expr}] = {evaluate_postfix(expr)}")


infix = [
    "A + B", "A + B * C", "( A + B ) * C", "A * B + C / D",
    "( A + B ) * ( C - D )", "A + B * C - D / E", "A * ( B + C ) / D",
    "( A + B * C ) / ( D - E )", "A +  ( B - C ) * D", "( A + B * ( C - D ) ) / E"
]

def infix_to_postfix(expr):
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = Stack()
    postfix = []
    tokens = expr.replace("(","( ").replace(")"," )").split()
    for c in tokens:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stack.push(c)
        elif c == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != '(' and precedence.get(stack.peek(),0) >= precedence[c]:
                postfix.append(stack.pop())
            stack.push(c)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return ' '.join(postfix)

print("\n----- Infix to Postfix Converter -----")
for expr in infix:
    print(f"[{expr}] = {infix_to_postfix(expr)}")

print("\n----- Linked List Tests -----")
sll = SinglyLinkedList()
print("Appending: 1, 2, 3")
sll.append(1)
sll.append(2)
sll.append(3)
print("Display:", end=" ")
sll.display()

print("Prepending: 0")
sll.prepend(0)
print("Display:", end=" ")
sll.display()

print("Reverse Display:", end=" ")
sll.reverse_display()

print("Deleting: 2")
sll.delete(2)
print("Display:", end=" ")
sll.display()

print("Appending duplicates: 1, 1, 1")
sll.append(1)
sll.append(1)
sll.append(1)
print("Display:", end=" ")
sll.display()

print("Remove all 1s")
sll.remove_all(1)
print("Display:", end=" ")
sll.display()

print("\n----- Split Evens/Odds Test -----")
seo = SplitEvensOdds()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Input: {nums}")
for n in nums:
    seo.append(n)
even, odd = seo.split()
print("Even numbers:", end=" ")
even.display()
print("Odd numbers:", end=" ")
odd.display()

print("\n----- All tests completed! -----")
