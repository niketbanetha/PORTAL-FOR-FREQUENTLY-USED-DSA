class Sorting():
    def __init__(self):
        self.output=[]

    def bubbleSort(self,array):
        length=len(array)
        self.output.append( "Bubble Sort Algorithm Start")
        for i in range(length-1):
            self.output.append ("{} Pass".format(i))
            self.output.append (" Array is {}".format(array))
            for j in range(length-i-1):
                self.output.append ("Comparing element at index {} and {} [{} < {}]".format(j+1,j,array[j+1],array[j]))
                if array[j+1]<array[j]:
                    self.output.append ("Swapping value of index {} and {} ".format(j+1,j))
                    array[j],array[j+1]=array[j+1],array[j]
        self.output.append ("Bubble Sort Algorithm End")
        self.output.append ("Sorted Array is {}".format(array))
        return
    
    def insertionSort(self,array):
        self.output.append( "Insertion Sort Algorithm Start")
        for i in range(len(array)):
            key=array[i]
            j=i-1
            self.output.append( "Comparing element {} with all element present before index {} [Array for comparsion is {}]".format(key,j+1,array[:j+1]))
            while j>=0 and key<array[j]:
                self.output.append ("Element is less than element at index {} [{} < {}] ".format(j,key,array[j]))
                array[j+1]=array[j]
                j=j-1
            array[j+1]=key
            self.output.append ("Placing value of element {} at index {} after comparing with array".format(key,j+1))
        self.output.append ("Insertion Sort Algorithm End")
        self.output.append ("Sorted Array is {}".format(array))
        return 
    
    def selectionSort(self,array):
        self.output.append ("Selection Sort Algorithm Start")
        size=len(array)
        for i in range(size):
            min_idx=i
            self.output.append ("Checking for smaller element than {} in right side of array".format(array[i]))
            for j in range(i+1,size):
                self.output.append ("Comparing {} > {} ".format(array[min_idx],array[j]))
                if array[min_idx]>array[j]:
                    self.output.append ("Since value is greater replacing min index value with {} index".format(j))
                    min_idx=j
            self.output.append ("Swapping element {} at index {} with element {} at index {}".format(array[i],i,array[min_idx],min_idx))
            array[i],array[min_idx]=array[min_idx],array[i]
        self.output.append ("Selection Sort Algorithm End")
        self.output.append ("Sorted Array is {}".format(array))
        return 

    def quickSort(self,array,pivot):
        self.output.append ("Checking for length of array is greater 1")
        if len(array)<=1:
            return array
        first=0
        last=len(array)-1
        if pivot=="MID":
            pvalue=array[(first+last)//2]
            pindex=(first+last)//2
            self.output.append ("Pivot for comparing is MID element {}".format(pvalue))
        elif pivot=="END":
            pvalue=array[len(array)-1]
            pindex=len(array)-1
            self.output.append ("Pivot for comparing is END element {}".format(pvalue))
        elif pivot=="FIRST":
            pvalue=array[0]
            pindex=0
            self.output.append ("Pivot for comparing is FIRST element {}".format(pvalue))
        
        greater_array=[]
        lesser_array=[]
        array.pop(pindex)

        self.output.append( "Checking for all element which are greater and less than pivot element {} in array {}".format(pvalue,array))
        for i in array:
            if i>pvalue:
                self.output.append ("Element {} is greater than pivot element {}".format(i,pvalue))
                greater_array.append(i)
            else:
                self.output.append ("Element {} is lesser than pivot element {}".format(i,pvalue))
                lesser_array.append(i)
        return self.quickSort(lesser_array,pivot)+[pvalue]+self.quickSort(greater_array,pivot)

    def mergeSort(self,array):
        self.output.append ("Checking for length of array is greater 1")
        if len(array)<=1:
            return array
        first=0
        last=len(array)-1
        pvalue=array[(first+last)//2]
        pindex=(first+last)//2
        self.output.append ("Pivot for comparing is MID element {}".format(pvalue))
        greater_array=[]
        lesser_array=[]
        array.pop(pindex)
        self.output.append("Checking for all element which are greater and less than pivot element {} in array {}".format(pvalue,array))
        for i in array:
            if i>pvalue:
                self.output.append ("Element {} is greater than pivot element {}".format(i,pvalue))
                greater_array.append(i)
            else:
                self.output.append ("Element {} is lesser than pivot element {}".format(i,pvalue))
                lesser_array.append(i)
        return self.mergeSort(lesser_array)+[pvalue]+self.mergeSort(greater_array)

    
    def countingSort(self,array):
        self.output.append("Counting Sort Algorithm Start")
        countArray=[0 for i in range(max(array)+1)]
        self.output.append("Creating count_array filed with zero of length equal to unsorted array max element [length of count_array == {} ]".format(max(array)))
        self.output.append("Modifying value of count_array such that each index contain count of the occurrence of element in unsorted array")
        for i in array:
            countArray[i]+=1
        sortedArray=[]
        self.output.append("Creating sorted array by traversing count_array and appending into sorted array according to their count")
        for index,value in enumerate(countArray):
            self.output.append("Element {} has count {} is append to sorted array".format(index,value))
            sortedArray.extend([index]*value)
        self.output.append ("Sorted Array is {}".format(sortedArray))

    




