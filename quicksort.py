import random
def quicksort(arr):
    if len(arr)< 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
    
ans =quicksort([7,5,4,3,2])
print(ans)
