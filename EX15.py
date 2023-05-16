#Provide an algorithm that finds the largest and smallest elements of an array of n members in the least number of comparisons
def MinMax(arr):
     
    n = len(arr)   #n number
     
    # if array has even number
    #we initialize 
    if(n % 2 == 0):
        maximom = max(arr[0], arr[1])
        minimom = min(arr[0], arr[1])
         
        # start index in loop
        i = 2
         
    # if array has odd number
    # we initialize as minimum and maximum
    else:
        maximom = minimom = arr[0]
         
        # start index in loop
        i = 1
         
    # in while loop, we pair numbers and compare them
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            maximom = max(maximom, arr[i + 1])
            minimom = min(minimom, arr[i])
        else:
            maximom = max(maximom, arr[i])
            minimom = min(minimom, arr[i + 1])
             
        # we increase index with 2
        
        i += 2
     
    return (maximom, minimom)
     

