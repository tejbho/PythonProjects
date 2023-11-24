def switch(lst, a, b):
    m = lst[b]
    lst[b] = lst[a]
    lst[a] = m
        
#numbers = input("Enter the numbers you want to sort")
numbers = [6,7,9,8,0]
lst = list(numbers)
for z in range(0,len(lst)):
    for x in range(1, len(lst)):
        y = x-1
        i = lst[x]
        j = lst[y]

        if j > i:
            switch(lst,x,y)

def bin_search(x):

    low = 0
    high = len(lst) - 1
    mid = 0

    while high >= low:
        mid = high+low // 2

        if lst[mid] < x:
            low = mid + 1

        elif lst[mid] > x:
            high = mid - 1

        else:
            return mid
            
    return -1        

print(lst)
print(bin_search(6))

