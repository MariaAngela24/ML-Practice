#Given a list of integers and a target sum, return the indices of any
#two values in the list that sum to that number.

lst = [1, 0, 4, 8]
target = 12


#Brute force solution
def find_indices(lst, target):
  for item in lst:
    idx = lst.indexof(item)
    value = lst[idx]
    next_idx = idx + 1
    second_lst = lst[next_idx::]
    for item in second_lst:
        idx_2 = second_lst.indexof(item)
      value_2 = lst[idx_2]
      result = value + value_2
      if result == target:
        solution = (idx, idx_2)
        return solution
      else:
        continue
  return None
      
find_indices(lst, target)   
#Better solution - use a dictionary to keep track of everything you have 
#already seen. Iterate over list, and at each item, use math to determine
#the value of what you need to find to get target.  Check dictionary to see
#if you have already seen that value.  