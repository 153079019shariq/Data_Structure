

#Building a min heap. WE ARE BEGINING FROM INDEX 1 INSTEAD OF 0.THIS IS ACHIEVIED BY INSERTING list1 =[0] +list1.THATS WHY IN THE CODE I HAVE STARTED FROM self.heap_list =[0] and then append the item to be be inserted instead of starting from self.heap_list =[]
class heap_sort(): 
  
  def __init__(self):
    self.heap_list  = [0]
    self.current_size =0

  def min_child(self,i):   #Check the child node of the parent node and return the minimum of both of them
    try :
      if(self.heap_list[2*i]<self.heap_list[2*i+1]):
        return 2*i
      else:
        return 2*i+1
    except:
        return 2*i  #Case when left child node exist but right child node did not exist

  def insert(self,item):
    self.heap_list.append(item)
    self.current_size = self.current_size + 1
    self.percup_up(item)

  def create_heap(self,list1):
    for i in range(len(list1)):
      self.insert(list1[i])
      
    
  def percup_up(self,item):
     i = len(self.heap_list)-1 
     while( i//2>0):  #Check whether root node exist or not.THE NODE in the HEAP START FROM 1 INSTEAD OF 0. 
        #Swap the parent_node with the child node if child node is less than parent node
        if(self.heap_list[i] < self.heap_list[i//2]):
          tmp                  = self.heap_list[i] 
          self.heap_list[i]    = self.heap_list[i//2]
          self.heap_list[i//2] = tmp
          i = i//2
        else:
          break   # Stop as soon as child node is greator than parent node

  def percup_down(self):
    i=1
    while((2*i)<= self.current_size):  #Check whether Left child left node exist or not
      min_childr = self.min_child(i)
      if(self.heap_list[min_childr] < self.heap_list[i]): 
        #Swap the parent_node with the child node if child node is less than parent node
        tmp  = self.heap_list[min_childr]
        self.heap_list[min_childr] = self.heap_list[i]
        self.heap_list[i]      =tmp
        i = min_childr
      else:
        break  # Stop as soon as child node is greator than parent node


  def delete_down(self):
    node_delete = self.heap_list[1]
    #Put the last element of heap into the root
    if(len(self.heap_list)>2):                 #Insert the last node as the root node
      self.heap_list[1] = self.heap_list.pop() # If condition not checked then at [1] position it is self.heap[1] always
    else:
      self.heap_list.pop()
    self.current_size = self.current_size -1
    self.percup_down()
    return node_delete


     

  def print_heap(self):
     return self.heap_list




heap_sor = heap_sort()
list1    = [109,10,5,6,2,3,4] 
heap_sor.create_heap(list1)
print(heap_sor.print_heap())
list2=[heap_sor.delete_down() for i in range(len(list1))]
print(list2)
#heap_sor.insert(1)
#print(heap_sor.print_heap())
         


