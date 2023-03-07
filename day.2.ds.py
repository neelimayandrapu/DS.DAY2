
#insertSLL.position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_position(self,n,data):
        np=Node(data)
        temp=self.head
        for i in range(n-1):
            temp=temp.next
            np.next=temp.next
            temp.next=np
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next
obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
print("before inserting 8")
obj.display()
print(" ")
print("after inserting 8")
obj.insert_position(2,8)
obj.display()



#deletion sll.beg
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
     
    
obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
print("before deleting 2")
obj.display()
print(" ")
print("after deleting 2 ")
obj.delete()
obj.display()



#deletion SLL.end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next
    def delete(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
            prev.next=None

obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
print("before deleting 6")
obj.display()
print(" ")
print("after deleting 6 ")
obj.delete()
obj.display()


#deletion SLL.position

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def deletion_position(self,n):
        temp=self.head.next
        prev=self.head
        for i in range(1,n-1):
            temp=temp.next
            prev=prev.next
            prev.next=temp.next
            temp.next=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next

obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
n3=Node(10)
n2.next=n3
print("before deletion 6")
obj.display()
print(" ")
print("after deletion 6")
obj.deletion_position(3)
obj.display()
            

#DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def dispaly(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," <-->",end=" ")
                temp=temp.next

obj=DLL()
n1=Node(12)
obj.head=n1
n2=Node(24)
n2.prev=n1
n1.next=n2
obj.dispaly()


#GAME1
import random
n=random.randrange(1,100)
guess=int(input("enter the num "))
while n!=guess:
    if guess< n:
        print("too low")
        guess=int(input("enter the num  again  "))
    elif guess>n:
        print("toon high ")
        guess=int(input("enter the num  again  "))
    else:
        break
print(" you guess it right ")



#DLL.INSERTION_BEG
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," <-->",end=" ")
                temp=temp.next

obj=DLL()
n1=Node(12)
obj.head=n1
n2=Node(24)
n2.prev=n1
n1.next=n2
print("before inserting")
obj.display()
print(" ")
print("after inserting")
obj.insert_start()
obj.display()


#DLLdeletion at end

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self):
            n=Node(300)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," <-->",end=" ")
                temp=temp.next

obj=DLL()
n1=Node(12)
obj.head=n1
n2=Node(24)
n2.prev=n1
n1.next=n2
print("before inserting")
obj.display()
print(" ")
print("after inserting")
obj.insert_end()
obj.display()


#DLL inserting.position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DLL:
    
    def __init__(self):
        self.head=None

    def insert_pos(self,n):
      np=Node(300)
      temp=self.head
    def insert_position(self,n,data):
        np=Node(data)
        temp=self.head
        for i in range(1,n-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=n
        temp.next=np
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next
obj=DLL()
n1=Node(12)
obj.head=n1
n2=Node(24)
n2.prev=n1
n1.next=n2
print("before inserting 8")
obj.display()
print(" ")
print("after inserting 8")
obj.insert_position(2,8)
obj.display()
            


            
