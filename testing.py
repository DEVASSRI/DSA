from Algos.bubble_sort import bubble_sort
from utils import generate_array_list
from utils import avg_time_elapsed
import time
array_size = [2**i for i in range(3,18)]
list_arrays = [generate_array_list(i) for i in array_size]
print("Average Time for different sample sizes:")
x = bubble_sort
for a in list_arrays:
  print(len(a[0]))
  time_elapsed = avg_time_elapsed(x, a)
  print(f"Time taken for sorting array of size {len(a[0])}: {time_elapsed:.8f} seconds") 
