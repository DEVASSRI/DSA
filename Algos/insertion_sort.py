def insertion_sort(array, asc = True):
  """
  Start at an index, move the element in such a way that the array upto that index is sorted.
  """
  n = len(array)
  
  #Base case: Array has only one element or zero elements
  if n <= 1:
    return array 
  
  for i in range(1,n): 
  #start from an index, compare with the elements onto the left and swap them if sorting required.
    
    curr = array[i]        #This holds the element for comparing
    j = i-1                # initiating another index 
    while asc == True and j>=0 and curr < array[j]:
      array[j+1] = array[j]        #moving elements to the right
      j-=1 
    array[j+1] = curr      #inserting the element in its right position
     
    while asc == False and j>=0 and curr > array[j]:
      array[j+1] = array[j]        
      j-=1 
    array[j+1] = curr 
  
  return array
    
    
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr, asc = False))

