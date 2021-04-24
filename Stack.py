import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class Stack():
    def __init__(self):
        self.stack=[]
        self.output=[]
    
    def push(self,item):
        self.output.append("Before pushing stack-> {}".format(self.stack[::-1]))
        self.stack.append(item)
        self.output.append("After pushing stack -> {}".format(self.stack[::-1]))
    
    def pop(self):
        self.output.append("Before pop stack-> {}".format(self.stack[::-1]))
        if len(self.stack)==0:
            self.output.append("Stack is empty")
            return
        self.stack.pop()
        self.output.append("After pop stack-> {}".format(self.stack[::-1]))

    def peek(self):
        if len(self.stack)==0:
            self.output.append("Stack is empty")
            return
        self.output.append("Element at top of stack is {}".format(self.stack[-1]))
    
    def print(self):
        self.output.append("Stack -> {}".format(self.stack[::-1]))
    
    def isEmpty(self):
        self.output.append("Checking wether stack is empty or not ")
        if len(self.stack)==0:
            self.output.append("Stack is empty")
            return
        self.output.append("Stack is not empty")
        return 


