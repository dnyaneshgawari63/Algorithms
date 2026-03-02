# finding an element in array
def find(array, target):
    for x in range(len(array)):
        if array[x] == target:
            return x
    return -1

# array = [10,11,12,13,14,15,16,17,18,19,20] 
target = 14
print(find(array, target))

# example 2
def reverse(aaa):
    aaa.sort()
    return aaa[::-1]
# arr = [10,1111,12,1332,14,150,16,17,14, 180,19,220]
reverse(arr)

# example 3
def duplics(aaa):
    dups ={}
    for x in aaa:
        if aaa.count(x) > 1:
            dups[x] = dups.count(x)

#aaa= [11,3,5,3,6,7,3,8]
duplics(aaa)

# example 4
#list comprehension
aaa= [11,3,5,3,6,7,3,8]
[x for x in aaa if aaa.count(x) > 1]

# example 5
aaa= [11,3,5,3,6,7,3,8]
aaa.sort()
set(aaa)
aaa[:-2]

# Example 6 Find median

aaa = [3,56,3,5,23,8]

aaa.sort()
n = len(aaa)
middle_num = n //2

if n % 2 == 0: # for even numbers 
    median  = aaa[middle_num -1] + aaa[middle_num]  / 2
else:
    median = aaa[middle_num]
    

# Example 7 
# replace every third item in an array with first one

a = [1,2,3,4,5,6,7,8,9,10]
for x in range(2, len(a), 3):
    a[x] = a[x-2] # replace the current element with the element two position before it

print(a)
# output [1,2,4,5,4 . . .]

# Example 8
# out of index error handeling 
a = [1,2,3,4,5,6,7,8,9,10]
try:
    for x in range(1, len(a), 2):
        a[x] = a[x+2]
except Exception as e:
    e

# Example 9 
# String array

abc = "Here is a better version of a software, we found"
abc = abc + " named elephant"
abc[4:25]

#list array append method
abc = []
x = 12
abc.append(x)

# Dictionary methods
abc = {}
abc["Name"] = "Bhalu" # name becomes key and Bhalu is value in abc dictionary form
abc[("1,2,3")] = 1000 # In dictionary only tuple can add multiple keys or values as tuple can notbe modified
abc

# Set
a = {}
a.add(12)
a

# set methods
a  = {12,"banana", 234,23,42,23,34}
a.pop()
a.remove(234)



# tuple methods
b = (123,342,234,23,12 "doooodooo")
a = (1,23,4,56,67,566)
a = a + 400
a = a + b
a.add(111)
a.remove(4)
a

#dict meth
a {nums: 1123,
   days:1234}
a={1:4465, 2:6767, 5:89787}
a.get("nums")
a.clear()
a.pop()
a.popitem()
a.get("days)
    
