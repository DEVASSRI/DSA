import random
import time
k = 10 # Set number of samples in each array size 
 
def generate_array_list(n):
  arr_list = [] 
  for _ in range(k):
    arr_list.append([random.randint(-100,200) for _ in range(n)])
  return arr_list

def avg_time_elapsed(x, lst):
  exec_time = []
  for i in lst:
    start_time = time.time()
    x(lst)
    end_time = time.time()
    exection_time = end_time - start_time
    exec_time.append(exection_time)
  #print(exec_time)
  s = 0
  for i in exec_time:
    s += i
  return s/len(lst)
  
