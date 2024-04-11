def partition(array, low, high, asc = True):
  """
  Splitting the array about the pivot
  """
  p = array[high]  #considering last element as pivot
  
  i = low-1 #consider it as the greatest element index in the partition
  if asc == True:
    for j in range(low, high):
      if array[j] <= p:
        i = i + 1
        array[i], array[j] = array[j], array[i]
  
    array[i+1], array[high] = array[high], array[i+1]
    return i+1
  if asc == False:
    for j in range(low, high):
      if array[j] >= p:
        i = i + 1
        array[i], array[j] = array[j], array[i]
  
    array[i+1], array[high] = array[high], array[i+1]
    return i+1
    
def quick_sort(array, low, high, asc = True):
  if low<high:
    pi = partition(array, low, high, asc)
    
    quick_sort(array, low, pi-1, asc)
    quick_sort(array, pi + 1, high, asc)

arr = [1, 7, 4, 1, 10, 9, -2]    
quick_sort(arr,0,len(arr)-1, asc = False)
print(arr)
      
   
