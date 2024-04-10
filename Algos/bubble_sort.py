def bubble_sort(array):
  '''
  Simple bubble sorting algorithm :
    
    The smallest element bubbles up to the correct position.
    
    Iterate through the array until there is no need for swapping. Hence maintain a Flag to track if a swap happens. i.e, when there are iteration breakout of the loop or end iterations.
  '''
  n = len(array)
  for i in range(n-2):
    # takes n-1 iterations
    flag_swap = False
    for j in range(n-1,i,-1):
      #starting from the last element
      if array[j] < array[j-1]:
        array[j-1],array[j] = array[j],array[j-1]
        flag_swap = True
    if flag_swap == False:
      break 
  return array
