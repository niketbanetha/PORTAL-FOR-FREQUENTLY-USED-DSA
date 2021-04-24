import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class SeparateChaining():
    
    def __init__(self,size):
        self.hash={i:{} for i in range(0,size)}
        self.size=size
        self.output=[]
        self.output.append("Creating hash of size {}".format(self.size))

    
    def insert(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.hash[index][data]=1
        self.output.append("After inserting -> {}".format(self.hash))
    
    def search(self,data):
        self.output.append("Converting search element into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking whether index is present in hash")
        if index in self.hash:
            self.output.append("Checking whether search element is there is hash")
            if data in self.hash[index]:
                return True
        return False
    
    def delete(self,data):
        self.output.append("Converting delete element into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking whether index is present in hash")
        if index in self.hash:
            self.output.append("Checking whether delete element is there is hash")
            if data in self.hash[index]:
                self.output.append("Element is found at index {}".format(index))
                self.hash[index].pop(data)
                self.output.append("After deleting hash -> {}".format(self.hash))
                return 
        self.output.append("Element not present in hash")
        return False

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class LinearProbing():

    def __init__(self,size):
        self.output=[]
        self.hash={i:None for i in range(size)}
        self.size=size
        self.output=[]
        self.output.append("Creating hash of size {}".format(self.size))
    
    def insert(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==None:
            self.hash[index]=data
            self.output.append("Element is inserted into hash table at index {}".format(index))
            self.output.append("Hash after insertion -> {}".format(self.hash))
            return 
        else:
            self.output.append("Element present at index {}".format(index))
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Linear probing -> ({}+{})%{}".format(index,i,self.size))
                cng_index=(index+i)%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==None:
                    self.hash[cng_index]=data
                    self.output.append("Element is inserted into hash table at index {}".format(cng_index))
                    self.output.append("Hash after insertion -> {}".format(self.hash))
                    return
        self.output.append("Element cannot be inserted into hash table.")
        self.output.append("Hash table -> {}".format(self.hash))
        return 

    def delete(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==data:
            self.output.append("Element found at index {} ".format(index))
            self.hash[index]=None
            self.output.append("Hash table after deletion -> {}".format(self.hash))
            return
        else:
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Linear probing -> ({}+{})%{}".format(index,i,self.size))
                cng_index=(index+i)%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==data:
                    self.output.append("Element found at index {} ".format(index))
                    self.hash[cng_index]=None
                    self.output.append("Hash table after deletion -> {}".format(self.hash))
                    return
        self.output.append("Value not present in hash table")
        return 
        
    def search(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==data:
            self.output.append("Element found at index {} ".format(index))
            return
        else:
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Linear probing -> ({}+{})%{}".format(index,i,self.size))
                cng_index=(index+i)%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==data:
                    self.output.append("Element found at index {} ".format(cng_index))
                    return
        self.output.append("Value not present in hash table")
        return 

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class QuadraticProbing():

    def __init__(self,size):
        self.output=[]
        self.hash={i:None for i in range(size)}
        self.size=size
        self.output=[]
        self.output.append("Creating hash of size {}".format(self.size))
    
    def insert(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==None:
            self.hash[index]=data
            self.output.append("Element is inserted into hash table at index {}".format(index))
            self.output.append("Hash after insertion -> {}".format(self.hash))
            return 
        else:
            self.output.append("Element present at index {}".format(index))
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Quadratic probing -> ({}+({}*{}))%{}".format(index,i,i,self.size))
                cng_index=(index+(i*i))%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==None:
                    self.hash[cng_index]=data
                    self.output.append("Element is inserted into hash table at index {}".format(cng_index))
                    self.output.append("Hash after insertion -> {}".format(self.hash))
                    return
        self.output.append("Element cannot be inserted into hash table.")
        self.output.append("Hash table -> {}".format(self.hash))
        return 




    def delete(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==data:
            self.output.append("Element found at index {} ".format(index))
            self.hash[index]=None
            self.output.append("Hash table after deletion -> {}".format(self.hash))
            return
        else:
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Quadratic probing -> ({}+({}*{}))%{}".format(index,i,i,self.size))
                cng_index=(index+(i*i))%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==data:
                    self.output.append("Element found at index {} ".format(index))
                    self.hash[cng_index]=None
                    self.output.append("Hash table after deletion -> {}".format(self.hash))
                    return
        self.output.append("Value not present in hash table")
        return 
    

    def search(self,data):
        self.output.append("Converting value into hash index by hash function-> {}%{} ".format(data,self.size))
        index=data%self.size
        self.output.append("Checking wether a element is present at particular index or not")
        if self.hash[index]==data:
            self.output.append("Element found at index {} ".format(index))
            return
        else:
            i=1
            while i<=self.size:
                self.output.append("Increasing index value using Quadratic probing -> ({}+({}*{}))%{}".format(index,i,i,self.size))
                cng_index=(index+(i*i))%self.size
                # print(index,data)
                i+=1
                self.output.append("Checking wether a element is present at new index {} or not ".format(cng_index))
                if self.hash[cng_index]==data:
                    self.output.append("Element found at index {} ".format(cng_index))
                    return
        self.output.append("Value not present in hash table")
        return 

# s=LinearProbing(7)
# s.insert(50)

# print(s.hash)
# s.insert(700)

# print(s.hash)
# s.insert(76)
# print(s.hash)
# s.insert(85)
# print(s.hash)
# s.insert(92)
# print(s.hash)
# s.insert(73)
# print(s.hash)
# s.insert(101)
# print(s.hash)


# print(s.delete(68))
# s.delete(73)
# print(s.hash)

# # s.delete(55)
# # print(s.hash)

# # print(s.search(47))