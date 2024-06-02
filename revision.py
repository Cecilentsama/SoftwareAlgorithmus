def quicksort(array):
    left = []
    right = []
    equal = []
    if len(array) > 1:
        pivot = array.pop
        for x in array :
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            elif x == pivot:
                equal.append(x)

        return quicksort(left) + quicksort(right)
    else:
        return array

print(quicksort([23,5,675,2,98,5,0, 9, 16]))