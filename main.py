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

def infix_to_postfix_demo():
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = Stack()
    postfix = []
    expr = input().replace(" ","")
    for c in expr:
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
    print(''.join(postfix))

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
        out=[]
        while cur:
            out.append(str(cur.data))
            cur=cur.next
        print(" -> ".join(out) if out else "Empty")
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

def linked_list_demo():
    sll=SinglyLinkedList()
    while True:
        c=input()
        if c=='1': sll.append(input())
        elif c=='2': sll.prepend(input())
        elif c=='3': sll.delete(input())
        elif c=='4': sll.remove_all(input())
        elif c=='5': sll.display()
        elif c=='6': sll.reverse_display()
        elif c=='7': break

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
        out=[]
        while cur:
            out.append(str(cur.data))
            cur=cur.next
        print(" -> ".join(out) if out else "Empty")

def split_demo():
    nums=input().split()
    seo=SplitEvensOdds()
    for n in nums:
        seo.append(int(n))
    even,odd=seo.split()
    even.display()
    odd.display()

def main():
    while True:
        c=input()
        if c=='1': infix_to_postfix_demo()
        elif c=='2': linked_list_demo()
        elif c=='3': split_demo()
        elif c=='4': break

if __name__=="__main__":
    main()

=== Data Structures Demo ===
1. Infix to Postfix Converter
2. Singly Linked List Operations
3. Split Evens and Odds
4. Exit
Enter your choice: 1
Enter an infix expression (e.g., A+B*C): A+B*C
ABC*+

=== Data Structures Demo ===
1. Infix to Postfix Converter
2. Singly Linked List Operations
3. Split Evens and Odds
4. Exit
Enter your choice: 2

1.Append 2.Prepend 3.Delete 4.RemoveAll 5.Display 6.ReverseDisplay 7.Back
Choice: 1. Append

1.Append 2.Prepend 3.Delete 4.RemoveAll 5.Display 6.ReverseDisplay 7.Back
Choice: 2. Prepend

1.Append 2.Prepend 3.Delete 4.RemoveAll 5.Display 6.ReverseDisplay 7.Back
Choice: 3.Delete

1.Append 2.Prepend 3.Delete 4.RemoveAll 5.Display 6.ReverseDisplay 7.Back
Choice: 1
Value: 1

1.Append 2.Prepend 3.Delete 4.RemoveAll 5.Display 6.ReverseDisplay 7.Back
Choice: 7

=== Data Structures Demo ===
1. Infix to Postfix Converter
2. Singly Linked List Operations
3. Split Evens and Odds
4. Exit
Enter your choice: 4

