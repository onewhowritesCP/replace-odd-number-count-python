# replace-odd-number-count-python
"It reads integers from the standard input (until it gets a negative number) and puts them into an array.
Any sequence of two or more consecutive odd numbers in the array are removed from the array and replaced by a single number representing the length of that sequence.
For example, if these numbers were provided on the standard input:[222,3,35,62,124,61,29,375,66,7,-1]
output:[222, 2, 62, 124, 3, 66, 7]

Try below Python Code: First replace the last consecutive odd number with the count and then the preceding odd number with -1. Finally, remove all -1 from the list.

Reason: It would be convenient to traverse the whole list with replacing consecutive odd numbers with -1, else the structure and indices of numbers would change and makes it difficult to iterate."

l=[222,3,35,62,124,61,29,375,66,7,-1]
count = 0
for i in range(0,len(l)):
    if l[i]%2!=0 and i!=len(l)-1:
        count +=1
    else:
        if count > 1:
            l[i-1]=count
            while count != 1:
                l[i-count]= -1
                count -= 1
        count = 0
l = [i for i in l if i>=0 ]

print(l)
