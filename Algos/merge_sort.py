def merge(array1, array2, asc):
  n1, n2 = len(array1), len(array2)
  new_sorted_array = []
  i, j = 0, 0   #These are intializing the variables
   
  while  i<n1 and j<n2 and asc == True:
    if array1[i] < array2[j]:
      new_sorted_array.append(array1[i])
      i+=1
    else:
      new_sorted_array.append(array2[j])
      j+=1
  while  i<n1 and j<n2 and asc == False:
    if array1[i] > array2[j]:
      new_sorted_array.append(array1[i])
      i+=1
    else:
      new_sorted_array.append(array2[j])
      j+=1
  
  if i<n1:
    new_sorted_array.extend(array1[i:])
  
  if j<n2:
    new_sorted_array.extend(array2[j:])
  
  return new_sorted_array
    
def mergesort(array, asc = True):
  n = len(array)
  if n<=1:
    return array
  m = n // 2
  arr1 = mergesort(array[:m], asc)
  arr2 = mergesort(array[m:], asc)
  
  return merge(arr1, arr2, asc)
  
arr = [12, 11, 13, 5, 6, 7, 29, 36]

print(mergesort(arr, asc = False))
  



