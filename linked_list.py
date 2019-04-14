

#A NODE in aa linked list has 

class Node():
  def __init__(self,initial_data):
    self.data = initial_data
    self.next = None

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_data(self,new_data):
    self.data = new_data

  def set_next(self,new_next):
    self.next  = new_next




class linked_list():
  def __init__(self):
   self.head = None
    
  def insert_end(self,item):
    if(self.head==None):
        node      = Node(item)
        self.head = node
    else:
       current = self.head
       # Iterate until I reach the end of linked list
       while(current.get_next() !=None):
         current =current.get_next()
       node = Node(item) 
       current.set_next(node)
  
  def insert_front(self,item):
    if(self.head == None):
      node      = Node(item)
      self.head = node
    else:
       #Insert in the begining
       node = Node(item)
       node.set_next(self.head)
       self.head = node 
  
  def remove_end(self):
    previous = None
    current  = self.head
    while(current.get_next() != None):
      previous = current
      current  = current.get_next()
    previous.set_next(None)
     

  def remove_begin(self):
    current  = self.head
    self.head= current.get_next()
  
  def remove_item(self,item):
    previous =None
    current =self.head
    found =0
    while(found ==0):
      if(current.get_data()==item):
        found  = 1
      else:
         previous = current
         current  = current.get_next()

    previous.set_next(current.get_next())

  def print(self):
     current =self.head
     while (current != None):
       print(current.get_data())
       current = current.get_next()

  def size(self):
    current = self.head
    count   =0
    while(current != None):  #Taken current in the while loop if I taken current.get_next() in the while loop then it would not consider the last element
      count   = count + 1
      current = current.get_next()
    return count
   
  def search (self,item):
    current  = self.head
    position = 1
    found    = False
    while(current != None):
      #print("INSIDE_WHILE",current.get_data())
      if(current.get_data()==item):
        found   = True
        break
      else:
        current = current.get_next()
        position = position +1
    return position,found


  def max_linked(self):
    current = self.head
    maxim = 0
    while(current !=None):
      if(current.get_data()>maxim):
        maxim =current.get_data()
      current =current.get_next()
    return maxim

  def sum_linked(self):
    current =self.head
    sum_link  = 0
    while(current != None):
      sum_link += current.get_data()
      current = current.get_next()
    return sum_link
    


link  = linked_list()
link.insert_front(10)
link.insert_front(20)
link.insert_front(30)
link.insert_front(40)
link.insert_front(50)
link.insert_front(5)
print("Maximum element",link.max_linked())
print("Sum of data",link.sum_linked())

#link.remove_begin()
#link.remove_begin()
#link.remove_item(30)
#link.remove_item(20)
link.print()
elem_present,elem_position =link.search(10)
print(elem_present,elem_position)
#print(link.size())



