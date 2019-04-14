
###################################_STACK_USING_OOPS###################################################################
class Stack():
  def __init__(self):
    self.list = []
  def empty(self):
    return self.list ==[]
  def push (self,item):
     self.list.append(item)
  def pop(self):
    return self.list.pop()
  def peek(self):
    return self.list[len(self.list)-1]
  def print(self):
     print(self.list)
  def size(self):
     return len(self.list)


#s = Stack()
#s.push(10)
#s.push(20)
#s.push(30)
#print("The top ofthe stack is",s.peek())

#######################################_INFIX_TO_POSTFIX_USING_STACK_###########################################
def infix_to_postfix(s):
  precedence={'/':2,'*':2,'+':1,'-':1,'(':4,')':4,'^':3}
  lis =list(s.split())
  post_lis =[]
  s = Stack()
  #print(lis)
  for i in lis:
    #print(i,post_lis)
    if((i in '0123456789')or (i in 'ABCDEFGHIJKLMNOPQRSTUVWYYZ')): #Operand
      post_lis.append(i)
    else:                                                          #Operator
       #Check for the bracket terms
        if(i==')'):
            while(s.peek()!='('):
              post_lis.append(s.pop())
            s.pop()  #Removes the '(' operaator
        else:
        #Pop all the element in the stack with equal or higher precedence
          while((s.empty()==False) and (precedence[i]<=precedence[s.peek()])and (s.peek()!='(')):
              post_lis.append(s.pop())
          s.push(i)
  #As  the expression is over so I have to pop all the operator in the Stack into post_lis
  while(s.empty()==False):
    post_lis.append(s.pop())
  
  #Convert postfix list to postfix string
  post_str =''
  for i in post_lis:
    post_str +=' '+ i
  return(post_str)

s  ="A * B + C * D"
s2 ="( A + B ) * C - ( D - E ) * ( F + G )"
print(infix_to_postfix(s2))



def operation(op1,op2,op):
  if(op =='+'):
    return str(op1 + op2)
  elif(op == '-'):
    return str(op1 - op2)
  elif(op == '/'):
    return str(op1/op2)
  elif(op == '*'):
    return str(op1*op2)
  elif(op == '^'):
    return str(op1**op2)


def postfix_evaluation(st):

  s_eval = Stack()
  lis  = list(st.split())
  #print("List is",lis)
  for i in lis:
    if(i in "0123456789"):
      s_eval.push(i)
    else:
      #Operators
      operator = i
      b = s_eval.pop() # The 1st element poped out is the 2nd operand
      a = s_eval.pop() # The 2nd element popped out is the 1st operand
      c = operation(int(a),int(b),operator)
      s_eval.push(c)
  postfix_eval =s_eval.peek()
  return postfix_eval

str1 ='7 8 + 3 2 + /'
str2 ='5 * 3 ^ ( 4 - 2 )'
s=infix_to_postfix(str2)
print(postfix_evaluation(s))




#########################_BASE_CONVERSION_USING_STACK_#############################################################

def base_conversion(num,base):
  st = Stack()
  while(num>0):
    rem = num % base
    st.push(rem)
    num = num // base
  
  string = ''
  while(st.empty()==False):
    string += str(st.pop())
  print(string)

num  = 42
base = 8
base_conversion(num,base)

###################################################################################################################

