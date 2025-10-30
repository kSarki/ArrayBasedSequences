class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n
    def prepend(self,data):
        n = Node(data)
        n.next = self.head
        self.head = n
    def delete(self,data):
        if not self.head: return
        if self.head.data==data:
            self.head=self.head.next
            return
        cur=self.head
        while cur.next:
            if cur.next.data==data:
                cur.next=cur.next.next
                return
            cur=cur.next
    def remove_all(self,data):
        while self.head and self.head.data==data:
            self.head=self.head.next
        cur=self.head
        while cur and cur.next:
            if cur.next.data==data:
                cur.next=cur.next.next
            else:
                cur=cur.next
    def display(self):
        cur=self.head
        parts = ["Head"]
        if not cur:
            parts.append("")
        while cur:
            parts.append(str(cur.data))
            cur=cur.next
        parts.append("None")
        print(" -> ".join(parts))
    def reverse_display(self):
        stack=Stack()
        cur=self.head
        while cur:
            stack.push(cur.data)
            cur=cur.next
        out=[]
        while not stack.is_empty():
            out.append(str(stack.pop()))
        print(" -> ".join(out) if out else "Empty")


class SplitEvensOdds:
    def __init__(self):
        self.head=None
    def append(self,data):
        n=Node(data)
        if not self.head:
            self.head=n
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=n
    def split(self):
        even=SplitEvensOdds()
        odd=SplitEvensOdds()
        cur=self.head
        even_tail=None
        odd_tail=None
        while cur:
            nxt=cur.next
            cur.next=None
            if cur.data%2==0:
                if not even.head:
                    even.head=cur
                    even_tail=cur
                else:
                    even_tail.next=cur
                    even_tail=cur
            else:
                if not odd.head:
                    odd.head=cur
                    odd_tail=cur
                else:
                    odd_tail.next=cur
                    odd_tail=cur
            cur=nxt
        return even,odd
    def display(self):
        cur=self.head
        parts = ["Head"]
        if not cur:
            parts.append("")
        while cur:
            parts.append(str(cur.data))
            cur=cur.next
        parts.append("None")
        print(" -> ".join(parts))

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

def main():
    postfix_exprs = [
        "5 3 +", "8 2 - 3 +", "5 3 8 * +", "6 2 / 3 +", "5 8 + 3 -",
        "5 3 + 8 *", "8 2 3 * + 6 -", "5 3 8 * + 2 /", "8 2 + 3 6 * -", "5 3 + 8 2 / -"
    ]
    
    for expr in postfix_exprs:
        print(f"[{expr}] = {evaluate_postfix(expr)}")
    
    infix_exprs = [
        "A + B", "A + B * C", "( A + B ) * C", "A * B + C / D",
        "( A + B ) * ( C - D )", "A + B * C - D / E", "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )", "A +  ( B - C ) * D", "( A + B * ( C - D ) ) / E"
    ]
    
    for expr in infix_exprs:
        print(f"[{expr}] -> [{infix_to_postfix(expr)}]")
    
    sll = SinglyLinkedList()
    for i in [1,2,3,4,5,6,7,8,15,14,13,12,11,10,9]:
        sll.append(i)
    sll.display()
    
    seo = SplitEvensOdds()
    for i in [1,2,3,4,5,6,7,8,15,14,13,12,11,10,9]:
        seo.append(i)
    even, odd = seo.split()
    even.display()
    odd.display()
    
    empty = SinglyLinkedList()
    empty.display()

if __name__=="__main__":
    main()

