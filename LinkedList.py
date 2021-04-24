import streamlit as st


class SNode():
    def __init__(self,data):
        self.data=data
        self.next=None

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class SinglyLinkedList():
    
    def __init__(self):
        self.head=None
        self.output=[]
    
    def insertEnd(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Empty Linked List, Storing value at head of linked list")
            self.head=SNode(data)
        else:
            self.output.append("Checking for empty node")
            temp=self.head
            while temp.next!=None:
                self.output.append("Moving to next node")
                temp=temp.next
            self.output.append("Inserting value after this value {}".format(temp.data))
            temp.next=SNode(data)
    
    def insertBeg(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Empty Linked List, Storing value at head of linked list")
            self.head=SNode(data)
        else:
            self.output.append("Storing head into temp node")
            temp=self.head
            self.head=SNode(data)
            self.head.next=temp
            self.output.append("Swapping head node with new node")
    
    def find(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
            
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(data,temp.data))
                if temp.data==data:
                    self.output.append("Value found in linked list")
                    return True
                temp=temp.next
            self.output.append("Value not found in linked list")
        return False

    def delete(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
        elif self.head.data==data:
            self.output.append("Data present at head node, Pointing head node to next node ")
            self.head=self.head.next
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            flag=0
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(data,temp.data))
                if temp.data==data:
                    flag=1
                    break
                prev=temp
                temp=temp.next
            if flag:
                self.output.append("Pointing deleted previous node to deleted next node")
                prev.next=temp.next
                temp=None
            else:
                self.output.append("Value not present in linked list")
        
        
    def deleteBeg(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
        else:
            self.output.append("Deleting head node")
            self.head=self.head.next
    
    def deleteEnd(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
        elif self.head.next==None:
            self.output.append("Making head node null ")
            self.head=None
        else:
            self.output.append("Traversing at end of linked list")
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            self.output.append("Making last node of linked list null")
            temp.next=None

    def show(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
        else:
            temp=self.head
            while temp!=None:
                self.output.append("Data is {}".format(temp.data))
                temp=temp.next
    
    def update(self,old,new):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Singly Linked List empty")
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            flag=0
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(old,temp.data))
                if temp.data==old:
                    flag=1
                    break
                temp=temp.next
            if flag:
                self.output.append("Swapping old data value {} with new value {}".format(old,new))
                temp.data=new
            else:
                self.output.append("Value not present in linked list")

class DNode():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.output=[]
    
    def insertEnd(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Empty Linked List, Storing value at head of linked list")
            self.head=DNode(data)
        else:
            self.output.append("Checking for empty node")
            temp=self.head
            while temp.next!=None:
                self.output.append("Moving to next node")
                temp=temp.next
            self.output.append("Inserting value after this value {}".format(temp.data))
            temp.next=DNode(data)
            temp.next.prev=temp
    
    def insertBeg(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Empty Linked List, Storing value at head of linked list")
            self.head=DNode(data)
        else:
            self.output.append("Storing head into temp node")
            temp=self.head
            self.head=DNode(data)
            self.head.next=temp
            temp.prev=self.head
            self.output.append("Swapping head node with new node")

    
    def delete(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            flag=0
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(data,temp.data))
                if temp.data==data:
                    flag=1
                    break
                prevNode=temp
                temp=temp.next
            if flag==1:
                self.output.append("Pointing deleted previous node to deleted next node")
                if temp.next==None:
                    prevNode.next=temp.next
                    temp=None
                else:
                    prevNode.next=temp.next
                    temp.next.prev=prevNode
                    temp=None
            else:
                self.output.append("Value not present in linked list")
                
    
    def deleteBeg(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        else:
            self.output.append("Deleting head node")
            self.head=self.head.next
            self.head.prev=None
    
    def deleteEnd(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        elif self.head.next==None:
            self.output.append("Making head node null ")
            self.head=None
        else:
            self.output.append("Traversing at end of linked list")
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            self.output.append("Making last node of linked list empty")
            temp.prev.next=None

    def show(self):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        else:
            temp=self.head
            while temp!=None:
                self.output.append("Data is {}".format(temp.data))
                temp=temp.next
    
    def update(self,old,new):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            flag=0
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(old,temp.data))
                if temp.data==old:
                    flag=1
                    break
                temp=temp.next
            if flag:
                self.output.append("Swapping old data value {} with new value {}".format(old,new))
                temp.data=new
            else:
                self.output.append("Value not present in linked list")
    
    def find(self,data):
        self.output.append("Checking whether head is empty or not")
        if self.head==None:
            self.output.append("Doubly Linked List empty")
        else:
            self.output.append("Finding element in linked list")
            temp=self.head
            while temp!=None:
                self.output.append("Comparing value to node value {} == {} ".format(data,temp.data))
                if temp.data==data:
                    self.output.append("Value found in linked list")
                    return True
                temp=temp.next
            self.output.append("Value not found in linked list")
            return False





