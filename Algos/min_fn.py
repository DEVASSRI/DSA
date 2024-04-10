def min_fn(array):
  min_val = array[0]
  idx = 0
  for i, ele in enumerate(array[1:]):
    if ele < min_val:
      min_val = ele
      idx = i+1
  return min_val, idx 
