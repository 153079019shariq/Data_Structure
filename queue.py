
class Queue():
  def __init__(self):
    self.list =[]
  def is_empty(self):
    return self.list==[]
  def enqueue(self,item):
     self.list.insert(0,item)
  def dequeue(self):
     return self.list.pop()
  def size(self):
     return len(self.list)
  def print(self):
     print (self.list)




def Hotpotato(lis,num):
    q =Queue()
    for elem in lis:
      q.enqueue(elem)
    q.print()
    i = 0
    while(q.size()>1):
      #print("Inside",i)
      if(i<num):
        q.enqueue(q.dequeue())
        i = i+1
      else:
       print("Element removed",q.dequeue())
       i = 0
    print("Person who won the game")
    q.print()

lis = ["Bill","David","Susan","Jane","Kent","Brad"]
Hotpotato(lis,7)



class De_queue():
  def __init__(self):
    self.list =[]
  def is_empty(self):
    return self.list==[]
  def enqueue_rear(self,item):
    return self.list.insert(0,item)
  def enqueue_front(self,item):
    return self.list.append(item)
  def dequeue_front(self):
     return self.list.pop()
  def dequeue_rear(self):
     return self.list.pop(0)
  def size(self):
     return len(self.list)
  def print(self):
     print (self.list)



#Application of Dequeuue
def check_pallindrome(s):
  d =De_queue()
  for i in s:
    d.enqueue_rear(i)

  #Remove the element from the front and rear end check if they are equal or not
  
  while(d.is_empty()==False):
    if(d.size()>1):   
      if(d.dequeue_front() != d.dequeue_rear()):
        equal = False
        break
      else:
        equal =True
    else:
      break
  print("The string searched is a pallindrome",equal)


s ="madam"
check_pallindrome(s)

