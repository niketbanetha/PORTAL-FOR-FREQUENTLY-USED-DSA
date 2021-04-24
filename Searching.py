class Searching():
    def __init__(self):
        self.output=[]


    def linearSearch(self,array,searchElement):
        self.output.append ("Linear Search Algorithm Start")
        for index in range(len(array)):
            self.output.append ("{}=={} -> {}".format(array[index],searchElement,array[index]==searchElement))
            if array[index]==searchElement:
                self.output.append ("Element Found at index {}".format(index))
                self.output.append ("Linear Search Algorithm End")
                return
        self.output.append ("Element not present in array")
        self.output.append ("Linear Search Algorithm End")
        

    def binarySearch(self,array,searchElement):
        self.output.append ("Binary Search Algorithm Start")
        array.sort()
        first=0
        last=len(array)-1
        while first<=last:
            mid=(first+last)//2
            self.output.append ("Middle Element for array {} is {}".format(array[first:last+1],array[mid]))

            if array[mid]==searchElement:
                self.output.append ("Element Found at index {}".format(mid))
                self.output.append ("Binary Search Algorithm End")
                return 
            elif array[mid]>searchElement:
                self.output.append ("Mid element greater than search element [{} > {} ]".format(array[mid],searchElement) )
                self.output.append ("Comparing in left side of mid element , Array for comparision is {}".format(array[first:mid]))
                last=mid-1
            else:
                self.output.append ("Mid element lesser than search element [{} < {} ]".format(array[mid],searchElement))
                self.output.append ("Comparing in right side of mid element, Array for comparision is {}".format(array[mid+1:last+1]))
                first=mid+1
                
        self.output.append ("Element not present in array")
        self.output.append ("Binary Search Algorithm End")


    def ternarySearch(self,array,searchElement):
        self.output.append ("Ternary Search Algorithm Start")
        array.sort()
        first=0
        last=len(array)-1
        while first<=last:
            mid1=first+(last-first)//3
            mid2=last-(last-first)//3
            self.output.append ("First Middle Element for array {} is {}".format(array[first:last+1],array[mid1]))
            self.output.append( "Second Middle Element for array {} is {}".format(array[first:last+1],array[mid2]))
            if searchElement==array[mid1]:
                self.output.append ("Element Found at index {}".format(mid1))
                self.output.append ("Ternary Search Algorithm End")
                return 
            elif searchElement==array[mid2]:
                self.output.append ("Element Found at index {}".format(mid2))
                self.output.append ("Ternary Search Algorithm End")
                return 
            elif searchElement<array[mid1]:
                self.output.append ("First middle element is greater than search element [{} > {} ]".format(array[mid1],searchElement) )
                self.output.append ("Comparing in left side of first mid element , Array for comparision is {}".format(array[first:mid1]) )
                last=mid1-1
            elif searchElement>array[mid2]:
                self.output.append ("Second middle element is less than search element [{} < {} ]".format(array[mid2],searchElement) )
                self.output.append ("Comparing in right side of second mid element , Array for comparision is {}".format(array[mid2+1:last+1]) )
                first=mid2+1
            else:
                self.output.append ("Search element lies between first and second middle element [ {} < {} < {} ]".format(array[mid1],searchElement,array[mid2]) )
                self.output.append ("Comparing in between first and second mid element , Array for comparision is {}".format(array[mid1+1:mid2]) )
                last=mid2-1
                first=mid1+1
        self.output.append ("Element not present in array")
        self.output.append ("Ternary Search Algorithm End")

