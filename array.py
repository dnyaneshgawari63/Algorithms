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

# Example 6
aaa = [3,56,3,5,23,8]
median = aaa.sort()
if len(aaa)%2 != 0:
    median = len(aaa)/n

else:
    median =(len(aaa)+1)/n
median







