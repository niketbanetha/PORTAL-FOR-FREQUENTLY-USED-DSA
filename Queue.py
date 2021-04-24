import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class Queue():
    def __init__(self):
        self.queue=[]
        self.output=[]

    def enqueue(self,item):
        self.output.append("Inserting element into queue")
        self.queue.append(item)
        self.output.append("After enqueue -> {}".format(self.queue))
    
    def dequeue(self):
        self.output.append("Before dequeue -> {}".format(self.queue))
        if len(self.queue)==0:
            self.output.append("Queue is empty")
            return
        self.queue.pop(0)
        self.output.append("Before dequeue -> {}".format(self.queue))
    
    def front(self):
        if len(self.queue)==0:
            self.output.append("Queue is empty")
            return
        self.output.append("Element at top of queue is {}".format(self.queue[0]))
    
    def rear(self):
        if len(self.queue)==0:
            self.output.append("Queue is empty")
            return
        self.output.append("Element at end of queue is {}".format(self.queue[-1]))
    
    def print(self):
        self.output.append("Queue -> {}".format(self.queue))


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class PriorityQueue():
    def __init__(self):
        self.pqueue=[]
        self.output=[]
    
    def enqueue(self,key,priority):
        self.output.append("Inserting value {} of priority {}".format(str(key),str(priority)))
        self.pqueue.append([key,priority])
        self.pqueue=sorted(self.pqueue,key=lambda k:k[1])
        self.output.append("After enqueue -> {}".format(self.pqueue))
    
    def dequeue(self):
        if len(self.pqueue)==0:
            self.output.append("Priority Queue is empty")
            return
        self.output.append("Before dequeue -> {}".format(self.pqueue))
        self.pqueue.pop(0)
        self.output.append("After dequeue -> {}".format(self.pqueue))
    
    def print(self):
        self.output.append("Priority Queue -> {}".format(self.pqueue))
    
    def front(self):
        if len(self.pqueue)==0:
            self.output.append("Priority Queue is empty")
            return
        self.output.append("Element at top of priority queue is {}".format(self.pqueue[0]))
    
    def rear(self):
        if len(self.pqueue)==0:
            self.output.append("Priority Queue is empty")
            return
        self.output.append("Element at end of priority queue is {}".format(self.pqueue[-1]))
    

