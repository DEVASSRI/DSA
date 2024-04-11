def max_fn(array):
  max_val = array[0]
  idx = 0
  for i, ele in enumerate(array[1:]):
    if ele > max_val:
      max_val = ele
      idx = i+1
  return max_val, idx 
  
