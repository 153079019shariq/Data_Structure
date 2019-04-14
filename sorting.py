


def insertion_sort(a_list):

  for i in range(1,len(a_list)):
   # print("insertion",i)
    current_val =a_list[i]
    current_pos   =i 
    while (current_pos > 0 and a_list[current_pos-1] >current_val):
      #Swap the elements
      a_list[current_pos] = a_list[current_pos-1]
      current_pos         = current_pos - 1
    a_list[current_pos]    = current_val

  print(a_list)

 
def bubble_sort(a_list):
   print("length",len(a_list))
   for i in range(len(a_list)-1,0,-1):
  #   print("i",i)
     for j in range(i):
       #print(j)
       if(a_list[j]>a_list[j+1]):
         temp       = a_list[j]
         a_list[j]  = a_list[j+1]
         a_list[j+1]= temp
  # print(a_list)


def selection_sort(a_list):
   
   for i in range(len(a_list)-1,0,-1):
     index_max =0
     for j in range(1,i+1):
       if(a_list[j]>a_list[index_max]):
         index_max = j
     a_list[j] = a_list[index_max]
   print(a_list)


def quick_sort(a_list):
  low   = 1
  high  = len(a_list) -1
  quick_sort_helper(a_list,low,high)
  print("a_list",a_list)



def quick_sort_helper(a_list,low,high):
  if(low<high):
    j = partition(a_list,low,high)
    quick_sort_helper(a_list,low,j-1)
    quick_sort_helper(a_list,j+1,high)
  


def partition(a_list,low,high):
  pivot = a_list[0] 
  while(low < high):
     while(a_list[low]<pivot):
      # print("Inside_while_low",low)
       low = low +1

     while(a_list[high]>pivot):
       #print("Inside_while",high)
       high = high -1
     #Swap the high and low element
     if(low<high):
       temp         = a_list[low]
       a_list[low]  = a_list[high]
       a_list[high] = temp
  #As low is greator than high so swap the pivot and low
  temp2       = pivot
  pivot       = a_list[high]
  a_list[high] = temp2
  a_list[0]   =pivot

  return low





alist = [54,26,93,17,77,31,44,55,20]
#insertion_sort(alist)
#bubble_sort(alist)
#selection_sort(alist)
quick_sort(alist)
