import streamlit as st
import mysql.connector
import Searching
import Sorting
import Stack
import Queue
import LinkedList
import Hashing
import UndirectedGraph
import DirectedGraph
import TraversalAndView
import Tree
import base64
import os

st.set_option('deprecation.showfileUploaderEncoding', False)


#Mysql Connection
mydb=mysql.connector.connect(host="localhost",
user="root",
password="root",
database="majorProject2")
mycursor=mydb.cursor()



#To check that whether username is already registered or not   
def search(username):
    global mycursor
    mycursor.execute('Select countId from register where email_id="{}"'.format(username))
    res=mycursor.fetchall()
    if len(res)>=1:
        return True
    return False

# Register a new user
def register(username,password):
    k=search(username)
    if k==False:
        global mycursor,mydb
        mycursor.execute('Insert into register (email_id,password) values ("{}","{}")'.format(username,password))
        mydb.commit()
        return True
    else:
        return False

    
# Login 
def login(username,password):
    global mycursor
    mycursor.execute('Select password from register where email_id="{}"'.format(username))
    res=mycursor.fetchall()
    for i in res:
        if i[0]==password:
            return True
    return False

#Download Function
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<center><h3><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a></h3></center>'
    return href

#If algorithm option is Searching 
def searchingFunc():
    search=Searching.Searching()
    algorithmOption=st.selectbox("Choose searching algorithm",["Linear Search","Binary Search","Ternary Search"])
    searchElement=st.text_input("Enter element to be searched")
    searchArray=st.text_input("Enter array")
    st.markdown('<p style="color:red">Array should be written in this format -> <br>10,20,30,40,50</p>', unsafe_allow_html=True)
    button= st.button("Search")
    
    if button==True:
        if searchElement.isnumeric() == False or searchElement=='':
            st.error("Search Element not in proper format")
        elif searchArray=='':
            st.error("Array not in proper format")
        else:
            try:
                searchArray=list(map(int,searchArray.split(',')))
                searchElement=int(searchElement)
                if algorithmOption=="Linear Search":
                    search.output=[]
                    search.linearSearch(searchArray,searchElement)
                    output="<br>".join(search.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinearSearch.txt', 'Java and Python Code'), unsafe_allow_html=True)

                elif algorithmOption=="Binary Search":
                    search.output=[]
                    search.binarySearch(searchArray,searchElement)
                    output="<br>".join(search.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BinarySearch.txt', 'Java and Python Code'), unsafe_allow_html=True)

                elif algorithmOption=="Ternary Search":
                    search.output=[]
                    search.ternarySearch(searchArray,searchElement)
                    output="<br>".join(search.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/TernarySearch.txt', 'Java and Python Code'), unsafe_allow_html=True)
            except:
                st.error("Array not in proper format")

def sortingFunc():
    sorting=Sorting.Sorting()
    algorithmOption=st.selectbox("Choose searching algorithm",["Bubble Sort","Insertion Sort","Selection Sort","Merge Sort","Quick Sort","Counting Sort"])
    if algorithmOption=="Quick Sort":
        pivot = st.selectbox("Select pivot element [Used only in  quick sort]",["MID","FIRST","END"])
    unsortArray=st.text_input("Enter array")
    st.markdown('<p style="color:red">Array should be written in this format -> <br>10,20,30,40,50</p>', unsafe_allow_html=True)
    button= st.button("Sort")
    
    if button==True:
        if unsortArray=='':
            st.error("Array not in proper format")
        else:
            try:
                unsortArray=list(map(int,unsortArray.split(',')))
                if algorithmOption=="Bubble Sort":
                    sorting.output=[]
                    sorting.bubbleSort(unsortArray)
                    output="<br>".join(sorting.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BubbleSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif algorithmOption=="Insertion Sort":
                    sorting.output=[]
                    sorting.insertionSort(unsortArray)
                    output="<br>".join(sorting.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/InsertionSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif algorithmOption=="Selection Sort":
                    sorting.output=[]
                    sorting.selectionSort(unsortArray)
                    output="<br>".join(sorting.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/SelectionSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif algorithmOption=="Merge Sort":
                    sorting.output=[]
                    array=sorting.mergeSort(unsortArray)
                    sorting.output.append("Sorted Array is {}".format(array))
                    output="<br>".join(sorting.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/MergeSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif algorithmOption=="Counting Sort":
                    sorting.output=[]
                    sorting.countingSort(unsortArray)
                    k=list(filter(lambda x:x<0,unsortArray))
                    if len(k)==0:
                        output="<br>".join(sorting.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/CountingSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                    else:
                        st.error("Counting sort is for positive integer")
            
                elif algorithmOption=="Quick Sort":
                    sorting.output=[]
                    array=sorting.quickSort(unsortArray,pivot)
                    sorting.output.append("Sorted Array is {}".format(array))
                    output="<br>".join(sorting.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/QuickSort.txt', 'Java and Python Code'), unsafe_allow_html=True)
                    
            except:
                st.error("Array not in proper format")


def stackFunc():
    stack=Stack.Stack()
    option=st.selectbox("Action to be performed",["Push","Pop","Peek","isEmpty","Print"])
    element=st.text_input("Value to be pushed")
    button = st.button("Start")
    clearStack=st.button("Make a new stack")
    if clearStack==True:
        st.caching.clear_cache()
    
    if button==True:
        if option=="Push":
            if element!='' and element.isnumeric():
                element=int(element)
                stack.output=[]
                stack.push(element)
                output="<br>".join(stack.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Stack.txt', 'Java and Python Code'), unsafe_allow_html=True)
            else:
                st.error("Value is not given")
        elif option=="Pop":
            stack.output=[]
            stack.pop()
            output="<br>".join(stack.output)
            st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
            st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Stack.txt', 'Java and Python Code'), unsafe_allow_html=True)
        elif option=="Peek":
            stack.output=[]
            stack.peek()
            output="<br>".join(stack.output)
            st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
            st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Stack.txt', 'Java and Python Code'), unsafe_allow_html=True)
        elif option=="isEmpty":
            stack.output=[]
            stack.isEmpty()
            output="<br>".join(stack.output)
            st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
            st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Stack.txt', 'Java and Python Code'), unsafe_allow_html=True)
        elif option=="Print":
            stack.output=[]
            stack.print()
            output="<br>".join(stack.output)
            st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
            st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Stack.txt', 'Java and Python Code'), unsafe_allow_html=True)


def hashFunc():
    option=st.selectbox("Select type of hashing",["Separate Chaining","Linear Probing","Quadratic Probing"])
    subOption=st.selectbox("Select action to be performed",["Insert","Delete","Search"])
    size=st.text_input("Enter size of hash table")
    value=st.text_input("Enter a value")
    button=st.button("Start")
    clearHash=st.button("Make a new hash table")
    if clearHash==True:
        st.caching.clear_cache()

    if button==True:
        if value!='' and value.isnumeric() and size!='' and size.isnumeric():
            value=int(value)
            if option=="Separate Chaining":
                separateChaining=Hashing.SeparateChaining(int(size))
                if subOption=="Insert":
                    separateChaining.output=[]
                    separateChaining.insert(value)
                    output="<br>".join(separateChaining.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/SeparateChaining.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Search":
                    separateChaining.output=[]
                    separateChaining.search(value)
                    output="<br>".join(separateChaining.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/SeparateChaining.txt', 'Java and Python Code'), unsafe_allow_html=True)
                
                elif subOption=="Delete":
                    separateChaining.output=[]
                    separateChaining.delete(value)
                    output="<br>".join(separateChaining.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/SeparateChaining.txt', 'Java and Python Code'), unsafe_allow_html=True)
                
            elif option=="Linear Probing":
                linearProbing=Hashing.LinearProbing(int(size))
                if subOption=="Insert":
                    linearProbing.output=[]
                    linearProbing.insert(value)
                    output="<br>".join(linearProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinearProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)
                
                elif subOption=="Search":
                    linearProbing.output=[]
                    linearProbing.search(value)
                    output="<br>".join(linearProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinearProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Delete":
                    linearProbing.output=[]
                    linearProbing.delete(value)
                    output="<br>".join(linearProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinearProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)
            
            elif option=="Quadratic Probing":
                quadraticProbing=Hashing.QuadraticProbing(int(size))
                if subOption=="Insert":
                    quadraticProbing.output=[]
                    quadraticProbing.insert(value)
                    output="<br>".join(quadraticProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/QuadraticProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Search":
                    quadraticProbing.output=[]
                    quadraticProbing.search(value)
                    output="<br>".join(quadraticProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/QuadraticProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Delete":
                    quadraticProbing.output=[]
                    quadraticProbing.delete(value)
                    output="<br>".join(quadraticProbing.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/QuadraticProbing.txt', 'Java and Python Code'), unsafe_allow_html=True)

def queueFunc():
    option=st.selectbox("Select type of queue",["Simple Queue","Priority Queue"])
    subOption=st.selectbox("Select action to be performed",["Enqueue","Dequeue","Front","Rear","Print"])
    if option=="Priority Queue":
        priority=st.text_input("Enter priority")
    value=st.text_input("Enter a value")
    
    button=st.button("Start")
    clearQueue=st.button("Make a new queue")
    if clearQueue:
        st.caching.clear_cache()
    
    if button==True:
            if option=="Simple Queue":
                queue=Queue.Queue()
                if subOption=="Enqueue" :
                    if value.isnumeric() and value!='' :
                        value=int(value)
                        queue.output=[]
                        queue.enqueue(value)
                        output="<br>".join(queue.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Queue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                    else:
                        st.error("Value is not in proper format")

                elif subOption=="Dequeue":
                    queue.output=[]
                    queue.dequeue()
                    output="<br>".join(queue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Queue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Front":
                    queue.output=[]
                    queue.front()
                    output="<br>".join(queue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Queue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Rear":
                    queue.output=[]
                    queue.rear()
                    output="<br>".join(queue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Queue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Print":
                    queue.output=[]
                    queue.print()
                    output="<br>".join(queue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Queue.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif option=="Priority Queue":
                pqueue=Queue.PriorityQueue()
                if subOption=="Enqueue" :
                    if value.isnumeric() and value!='' and priority.isnumeric() and priority!='' :
                        value=int(value)
                        priority=int(priority)
                        pqueue.output=[]
                        pqueue.enqueue(value,priority)
                        output="<br>".join(pqueue.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/PriorityQueue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                    else:
                        st.error("Value or Priority is not in proper format")

                elif subOption=="Dequeue":
                    pqueue.output=[]
                    pqueue.dequeue()
                    output="<br>".join(pqueue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/PriorityQueue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Front":
                    pqueue.output=[]
                    pqueue.front()
                    output="<br>".join(pqueue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/PriorityQueue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Rear":
                    pqueue.output=[]
                    pqueue.rear()
                    output="<br>".join(pqueue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/PriorityQueue.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Print":
                    pqueue.output=[]
                    pqueue.print()
                    output="<br>".join(pqueue.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/PriorityQueue.txt', 'Java and Python Code'), unsafe_allow_html=True)

def linkedListFunc():
    option=st.selectbox("Select type of Linked List",["Singly Linked List","Doubly Linked List"])
    subOption=st.selectbox("Select action to be performed",["Insert End","Insert Beg","Delete","Delete End","Delete Beg","Search","Print","Update"])
    value=st.text_input("Enter a value")
    if subOption=="Update":
        newValue=st.text_input("Enter the new value")
    button=st.button("Start")
    clearLList=st.button("Make a new Linked List")

    if clearLList:
        st.caching.clear_cache()

    if button:
        if option=="Singly Linked List":
            sllist=LinkedList.SinglyLinkedList()
            if subOption=="Insert End":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.insertEnd(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListInsertEnd.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Insert Beg":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.insertBeg(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListInsertBeg.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.delete(value)
                    print(sllist.output)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListDelete.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Update":
                if value!='' and value.isnumeric() and newValue.isnumeric() and newValue!='':
                    value=int(value)
                    newValue=int(newValue)
                    sllist.output=[]
                    sllist.update(value,newValue)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListUpdate.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Search":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.find(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListSearch.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete End":
                sllist.output=[]
                sllist.deleteEnd()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListDeleteEnd.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Delete Beg":
                sllist.output=[]
                sllist.deleteBeg()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListDeleteBeg.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Print":
                sllist.output=[]
                sllist.show()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/LinkedListShow.txt', 'Java and Python Code'), unsafe_allow_html=True)
        
        elif option=="Doubly Linked List":
            sllist=LinkedList.SinglyLinkedList()
            if subOption=="Insert End":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.insertEnd(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListInsertEnd.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Insert Beg":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.insertBeg(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListInsertBeg.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.delete(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListDelete.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Update":
                if value!='' and value.isnumeric() and newValue!='' and newValue.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.update(value,newValue)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListUpdate.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Search":
                if value!='' and value.isnumeric():
                    value=int(value)
                    sllist.output=[]
                    sllist.find(value)
                    output="<br>".join(sllist.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListSearch.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete End":
                sllist.output=[]
                sllist.deleteEnd()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListDeleteEnd.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Delete Beg":
                sllist.output=[]
                sllist.deleteBeg()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListDeleteBeg.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Print":
                sllist.output=[]
                sllist.show()
                output="<br>".join(sllist.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DLinkedListShow.txt', 'Java and Python Code'), unsafe_allow_html=True)

def treeFunc():
    option=st.selectbox("Choose from type of tree",["Binary Search Tree","AVL Tree"])
    subOption=st.selectbox("Choose action to be performed",["Insert","Search","Delete","Left View","Right View","Top View","Bottom View","Inorder Traversal","Preorder Traversal","Postorder Traversal"])
    value=st.text_input("Enter a value")
    button=st.button("Start")
    newTree=st.button("Make a new Tree")
    if newTree:
        st.caching.clear_cache()

    if button:
        if option=="Binary Search Tree":
            bst=Tree.BST()
            bstFunc=Tree.BSTFunction()
            tav=TraversalAndView.TraversalAndView()
            if subOption=="Insert":
                if value.isnumeric() and value!='':
                    value=int(value)
                    bstFunc.output=[]
                    bst.root=bstFunc.insertBST(bst.root,value)
                    output="<br>".join(bstFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BST.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Search":
                if value.isnumeric() and value!='':
                    value=int(value)
                    bstFunc.output=[]
                    bstFunc.searchBST(bst.root,value)
                    output="<br>".join(bstFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BST.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete":
                if value.isnumeric() and value!='':
                    value=int(value)
                    bstFunc.output=[]
                    bst.root=bstFunc.deleteBST(bst.root,value)
                    output="<br>".join(bstFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BST.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Left View":
                tav.output=[]
                tav.leftView(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Right View":
                tav.output=[]
                tav.rightView(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Top View":
                tav.output=[]
                tav.topView(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Bottom View":
                tav.output=[]
                tav.bottomView(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Inorder Traversal":
                tav.output=[]
                tav.inOrderTraversal(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Preorder Traversal":
                tav.output=[]
                tav.preOrderTraversal(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Postorder Traversal":
                tav.output=[]
                tav.postOrderTraversal(bst.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)

        if option=="AVL Tree":
            avl=Tree.AVL()
            avlFunc=Tree.AVLFunction()
            tav=TraversalAndView.TraversalAndView()
            if subOption=="Insert":
                if value.isnumeric() and value!='':
                    value=int(value)
                    avlFunc.output=[]
                    avl.root=avlFunc.insertAVL(avl.root,value)
                    output="<br>".join(avlFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/AVL.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Search":
                if value.isnumeric() and value!='':
                    value=int(value)
                    avlFunc.output=[]
                    avlFunc.searchAVL(avl.root,value)
                    output="<br>".join(avlFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/AVL.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Delete":
                if value.isnumeric() and value!='':
                    value=int(value)
                    avlFunc.output=[]
                    avl.root=avlFunc.deleteAVL(avl.root,value)
                    output="<br>".join(avlFunc.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/AVL.txt', 'Java and Python Code'), unsafe_allow_html=True)
                else:
                    st.error("Value not in proper format")
            elif subOption=="Left View":
                tav.output=[]
                tav.leftView(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Right View":
                tav.output=[]
                tav.rightView(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Top View":
                tav.output=[]
                tav.topView(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Bottom View":
                tav.output=[]
                tav.bottomView(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/View.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Inorder Traversal":
                tav.output=[]
                tav.inOrderTraversal(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Preorder Traversal":
                tav.output=[]
                tav.preOrderTraversal(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)
            elif subOption=="Postorder Traversal":
                tav.output=[]
                tav.postOrderTraversal(avl.root)
                output="<br>".join(tav.output)
                st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Traversal.txt', 'Java and Python Code'), unsafe_allow_html=True)

def graphFunc():
    option=st.selectbox("Select type of graph",["Directed Graph","Undirected Graph"])
    subOptionGraph="Unweighted"
    if option=="Directed Graph":
        subOptionGraph=st.selectbox("Select type of directed graph",["Weighted","Unweighted"])
    if subOptionGraph=="Unweighted":
        subOption=st.selectbox("Choose Action to be performed",["Insert","BFS","DFS","Cycle Detection"])
    else:
        subOption=st.selectbox("Choose Action to be performed",["Insert","BFS","DFS","Cycle Detection","Dijkstra","Bellman Ford","Prim's Algorithm","Topological Sort"])

    nodeCount=st.text_input("Enter total number of nodes")
    if nodeCount.isnumeric():
        nodeValue=",".join([str(i) for i in range(int(nodeCount))])
        st.info("Nodes are -> {}".format(nodeValue))
    
    if option in ["Undirected Graph","Directed Graph"] and subOption in ["BFS","DFS","Dijkstra","Bellman Ford"]:
        values=st.text_input("Enter node number")
    elif option =="Directed Graph" and subOption=="Insert" and subOptionGraph=="Weighted":
        values=st.text_area("Enter edges and their weight")
        st.markdown('<p style="color:red">Edges and weight should be written in this format [node1,node2,weight] -> <br>1,2,10<br>2,3,30<br>3,1,5<br></p>', unsafe_allow_html=True)
    elif option in ["Undirected Graph","Directed Graph"] and subOption=="Insert" and subOptionGraph=="Unweighted":
        values=st.text_area("Enter edges")
        st.markdown('<p style="color:red">Edges should be written in this format [node1,node2] -> <br>1,2<br>2,3<br>3,1<br></p>', unsafe_allow_html=True)

    button=st.button("Start")
    newGraph=st.button("Make a new Graph")
    if newGraph:
        st.caching.clear_cache()
    if button:
        if nodeCount.isnumeric() and nodeCount!='':
            if option=="Undirected Graph":
                ug=UndirectedGraph.UndirectedGraph(int(nodeCount))
                if subOption=="Insert":
                    try:
                        values=values.split("\n")
                        edges=[]
                        for i in values:
                            edges.append(list(map(int,i.split(","))))
                    except:
                        st.error("Wrong format")
                    else:
                        ug.output=[]
                        for i in edges:
                            ug.addEdge(i[0],i[1])
                        output="<br>".join(ug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/UaddEdge.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="BFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        ug.output=[]
                        ug.BFS(int(values))
                        output="<br>".join(ug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="DFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        ug.output=[]
                        ug.DFS(int(values))
                        output="<br>".join(ug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Cycle Detection":
                    ug.output=[]
                    ug.cycleCheck()
                    output="<br>".join(ug.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/CycleDetectUndirected.txt', 'Java and Python Code'), unsafe_allow_html=True)
            
            if option=="Directed Graph" and subOptionGraph=="Unweighted":
                dug=DirectedGraph.unweightedDirectedGraph(int(nodeCount))
                if subOption=="Insert":
                    try:
                        values=values.split("\n")
                        edges=[]
                        for i in values:
                            edges.append(list(map(int,i.split(","))))
                    except:
                        st.error("Wrong format")
                    else:
                        dug.output=[]
                        for i in edges:
                            dug.addEdge(i[0],i[1])
                        output="<br>".join(dug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DUaddEdge.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="BFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dug.output=[]
                        dug.BFS(int(values))
                        output="<br>".join(dug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="DFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dug.output=[]
                        dug.DFS(int(values))
                        output="<br>".join(dug.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Cycle Detection":
                    dug.output=[]
                    dug.cycleCheck()
                    output="<br>".join(dug.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/CycleDetectDirected.txt', 'Java and Python Code'), unsafe_allow_html=True)
            
            
            if option=="Directed Graph" and subOptionGraph=="Weighted":
                dwg=DirectedGraph.weightedDirectedGraph(int(nodeCount))
                if subOption=="Insert":
                    try:
                        values=values.split("\n")
                        edges=[]
                        for i in values:
                            edges.append(list(map(int,i.split(","))))
                    except:
                        st.error("Wrong format")
                    else:
                        dwg.output=[]
                        for i in edges:
                            dwg.addEdge(i[0],i[1],i[1])
                        output="<br>".join(dwg.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DWaddEdge.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="BFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dwg.output=[]
                        dwg.BFS(int(values))
                        output="<br>".join(dwg.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/BFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="DFS":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dwg.output=[]
                        dwg.DFS(int(values))
                        output="<br>".join(dwg.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/DFS.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Cycle Detection":
                    dwg.output=[]
                    dwg.cycleCheck()
                    output="<br>".join(dwg.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/CycleDetectDirected.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Topological Sort":
                    dwg.output=[]
                    dwg.topologicalSort()
                    output="<br>".join(dwg.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Topological.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Prim's Algorithm":
                    dwg.output=[]
                    dwg.Prims()
                    output="<br>".join(dwg.output)
                    st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                    st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Prims.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Dijkstra":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dwg.output=[]
                        dwg.Dijkstra(int(values))
                        output="<br>".join(dwg.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Dijkstra.txt', 'Java and Python Code'), unsafe_allow_html=True)
                elif subOption=="Bellman Ford":
                    try:
                        values=int(values)
                    except:
                        st.error("Wrong Format")
                    else:
                        dwg.output=[]
                        dwg.BellmanFord(int(values))
                        output="<br>".join(dwg.output)
                        st.markdown('<div style="background-color:grey; color:white;width: 700px;padding: 30px; font-size: 20;font-weight: bolder;">{}</div>'.format(output),unsafe_allow_html=True)
                        st.markdown(get_binary_file_downloader_html('./Python and Java DSA/Bellman.txt', 'Java and Python Code'), unsafe_allow_html=True)





#Main Page
def home():
    algorithmOption=st.selectbox("Choose algorithm",["Searching","Sorting","Hashing","Linked List","Stack","Queue","Tree","Graph"])
    
    if algorithmOption=="Searching":
        searchingFunc()
    elif algorithmOption=="Sorting":
        sortingFunc()
    elif algorithmOption=="Stack":
        stackFunc()
    elif algorithmOption=="Hashing":
        hashFunc()
    elif algorithmOption=="Queue":
        queueFunc()
    elif algorithmOption=="Linked List":
        linkedListFunc()
    elif algorithmOption=="Tree":
        treeFunc()
    elif algorithmOption=="Graph":
        graphFunc()

#Home Page
def intro():
    option=st.sidebar.selectbox("Choose page to navigate",options=["Login","Register"])

    if option=="Login":
        username=st.sidebar.text_input("Enter email address")
        password=st.sidebar.text_input("Enter password",type="password")
        button=st.sidebar.checkbox("Login")
        st.markdown("<h1 style='text-align: center;'>Portal for Frequently used DSA</h1>", unsafe_allow_html=True)
        if button:
            if username=="" or password=="":
                st.sidebar.error("Enter the details")
            else:
                if login(username,password):
                    home()
                    st.sidebar.success("Logged In")
                else:
                    st.sidebar.error("Wrong email address/password")
    elif option=="Register":
        username=st.sidebar.text_input("Enter email address")
        password=st.sidebar.text_input("Enter password",type="password")
        button=st.sidebar.checkbox("Register")
        
        st.markdown("<h1 style='text-align: center;'>Portal for Frequently used DSA</h1>", unsafe_allow_html=True)

        if button:
            if username=="" or password=="":
                st.sidebar.error("Enter the details")
            else:
                if register(username,password):
                    st.sidebar.info("Move to login page")
                else:
                    st.sidebar.error("Email id already registered")


if __name__=="__main__":
    intro()
