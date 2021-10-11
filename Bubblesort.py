def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if len(arr[j]) > len(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)
x = str(input('What is your sentence? '))
arr = [x]
x = arr[0].split()
print(bubbleSort(x))
