# Python program to convert infix expression to postfix 
num='0123456789'
fun=['sin','cos','ln','exp','sqrt']

def isNum(c): 
    return c in num

precedence = {'+':1, '-':1, '*':2, '/':2, '^':3, 'sin':4, 'cos':4, 'ln':4, 'exp':4, 'sqrt':4} 
presetdvar={'e':'2.718281828','Pi':'3.1415926535'}
dvar=presetdvar
dfunc={}

# A utility function to check is the given character 
# is operand

def isOperand(ch): 
    return (ch.isalpha())and(ch not in precedence.keys()) 

def isnmb(n):
    try: 
        a = float(n)
        return True
    except ValueError:  
        return False
    except TypeError:  
        return False

def convint(n):
    try:
        return int(n)
    except ValueError:
        return float(n)
    except TypeError:  
        return None 

class Conversion: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
        # Precedence setting 
        self.output = [] 
        
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  

    # Check if the precedence of operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = precedence[i] 
            b = precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
    def compos(self,exp):
        l=len(exp)
        j=0
        d=[]
        while(j<l):
            i=exp[j] 
            # If the character is an operand,  
            # add it to output 

            if (isNum(i)):
                a=''
                while((j<l)and(isNum(exp[j]) or exp[j]=='.')):
                     a+=exp[j]
                     j+=1
                d+=[a]
                j-=1
            elif((i=='-') and (j==0 or exp[j-1]=='(' or exp[j-1]==')')):
                a='-'
                j+=1
                while((j<l)and(isNum(exp[j]) or exp[j]=='.')):
                    a+=exp[j]
                    j+=1
                d+=[a]
                j-=1
            elif((j+1<l)and (exp[j]+exp[j+1]) in fun):
                d+=[(exp[j]+exp[j+1])]
                j+=1
            elif((j+2<l)and (exp[j]+exp[j+1]+exp[j+2]) in fun):
                d+=[(exp[j]+exp[j+1]+exp[j+2])]
                j+=2
            elif((j+3<l)and (exp[j]+exp[j+1]+exp[j+2]+exp[j+3]) in fun):
                d+=[(exp[j]+exp[j+1]+exp[j+2]+exp[j+3])]
                j+=3
            elif(i in '+-*/^'):
                d+=[i]
            elif(i.isalpha()):
                a=''
                while( (j<l) and ((exp[j]).isalpha()) ):
                     a+=exp[j]
                     j+=1
                d+=[a]
                j-=1 
            j+=1 
        return d
          
    # The main function that converts given infix expression 
    # to postfix expression 
    def infixToPostfix(self, exp): 
        d=self.compos(exp)
        # Iterate over the expression for conversion 
        for i in d:
            # If the character is an operand,  
            # add it to output 

            if isOperand(i): 
                self.output.append(i)
             
            elif isnmb(i):
                self.output.append(i)
            # If the character is an '(', push it to stack 
            elif i  == '(': 
                self.push(i) 
  
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop()
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i)
  
        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
        return self.output
  
# Driver program to test above function 




#************************************************************

  


def copyEt(a): 
    if a is not None:
        b=Et(a.value)
        b.left=copyEt(a.left)
        b.right=copyEt(a.right)
        return b
    else:
        return None

def isOperator(c): 
    return (c in precedence.keys())
def inorder(t): 
    if t is not None: 
        if ( t.value=='+' or t.value=='-'or (t.value in precedence.keys() and precedence[t.value] == 4 )):		
            print('(',end='')		
        inorder(t.left) 
        print(t.value,end='') 
        inorder(t.right) 
        if ( t.value=='+' or t.value=='-'or (t.value in precedence.keys() and precedence[t.value] == 4 )):		
            print(')',end='')
def FuncTree(t): 
    if t is not None: 
        print(t.value,end='') 
        if ( t.value in precedence.keys()):		
            print('(',end='')
        FuncTree(t.left) 
        if((t.left is not None) and (t.right is not None)):
            print(',',end='')
        FuncTree(t.right) 
        if ( t.value in precedence.keys()):		
            print(')',end='')
def constructTree(postfix): 
    stack = []  
    # Traverse through every character of input expression 
    for char in postfix: 
        # if operand, simply push into stack 
        if not (isOperator(char)) and not (isnmb(char)): 
            t = Et(char) 
            stack.append(t) 

        elif (isnmb(char)):
            try:
                t = Et(int(char))
            except ValueError:
                t = Et(float(char)) 
            stack.append(t)
        # Operator 
        else:
            if(precedence[char]<4): 
                # Pop two top nodes 
                t = Et(char) 
                t1 = stack.pop() 
                t2 = stack.pop() 
                
                # make them children 
                t.right = t1 
                t.left = t2 
            else:
                t = Et(char) 
                t1 = stack.pop() 
                
                # make them children  
                t.left = None 
                t.right= t1  
            # Add this subexpression to stack 
            stack.append(t) 
  
    # Only element  will be the root of expression tree 
    t = stack.pop() 
     
    return t 
def Diff(t,exp):
    if(t.value==exp):
        t.value=1
    elif(t.value=='+' or t.value=='-'):
        Diff(t.left,exp)
        Diff(t.right,exp)
    elif(t.value=='^'):
        if(isinstance((t.right).value,int) or isinstance((t.right).value,float)):
            t.value='*'
            tl=copyEt(t.left)
            b=Et('^')
            d=Et('*')
            c=Et((t.right).value)
            Diff(t.left,exp)
            d.left=c
            d.right=t.left
            b.left=tl
            t.right.value-=1
            b.right=t.right
            t.left=d
            t.right=b
        else:
            a=copyEt(t.left)
            b=copyEt(t.right)
            t.value='+'
            Diff(t.left,exp)
            Diff(t.right,exp)
            b1=Et('*')
            b2=Et('*')
            b3=Et('ln')
            b4=Et('^')
            b4.left=a
            b4.right=b
            b3.left=None
            b3.right=a
            b2.left=b3
            b2.right=b4
            b1.left=t.right
            b1.right=b2
            t.left=b1
            #*******
            b5=Et('*')
            b6=Et('*')
            b7=Et('^')
            b8=Et('-')
            b9=Et(1)
            b8.left=b
            b8.right=b9
            b7.left=a
            b7.right=b8
            b6.left=b
            b6.right=b7
            b5.left=t.right
            b5.right=b6
            t.right=b5
            
    elif(t.value=='*'):
        t.value='+'
        tl=copyEt(t.left)
        tr=copyEt(t.right)
        b=Et('*')
        c=Et('*')
        Diff(t.left,exp)
        b.left=t.left
        b.right=tr
        Diff(t.right,exp)
        c.left=t.right
        c.right=tl
        t.left=b
        t.right=c
    elif(t.value=='/'):
        tl=copyEt(t.left)
        tr=copyEt(t.right)
        b=Et('-')
        bl=Et('*')
        br=Et('*')
        c=Et('*')
        Diff(t.left,exp)
        bl.left=t.left
        bl.right=tr
        Diff(t.right,exp)
        br.left=t.right
        br.right=tl
        b.left=bl
        b.right=br
        c.left=tr
        c.right=tr
        t.left=b
        t.right=c
    elif(t.value=='sin'):
        t.value='*'
        tl=copyEt(t.right)
        b=Et('cos')
        Diff(t.right,exp)
        t.left=t.right
        b.left=None
        b.right=tl
        t.right=b
    elif(t.value=='cos'):
        t.value='*'
        tl=copyEt(t.right)
        b=Et('sin')
        c=Et('*')
        d=Et(-1)
        Diff(t.right,exp)
        b.right=tl
        c.left=d
        c.right=t.right
        t.left=c
        t.right=b
    elif(t.value=='ln'):
        t.value='/'
        tl=copyEt(t.right)
        Diff(t.right,exp)
        t.left=t.right
        t.right=tl
    elif(t.value=='exp'):
        t.value='*'
        tl=copyEt(t.right)
        Diff(t.right,exp)
        t.left=t.right
        b=Et('exp')
        b.right=tl
        t.right=b
    elif(t.value=='sqrt'):
        t.value='/'
        tl=copyEt(t.right)
        Diff(t.right,exp)
        t.left=t.right
        b=Et('*')
        c=Et(2)
        d=Et('sqrt')
        d.right=tl
        b.left=c
        b.right=d
        t.right=b
    elif(isinstance(t.value,int) or isinstance(t.value,float)):
        t.value=0

def Eval(t,d):
    if(t.left is not None):
        Eval(t.left,d)
    if(t.right is not None):
        Eval(t.right,d)
    if(t.value in d.keys()):
        t.value=d[t.value]

                
def simpl(t):
    if(t.left is not None):
        simpl(t.left)
    if(t.right is not None):
        simpl(t.right)
    s=(t.left is not None)and(t.right is not None)
    s1=(t.left is None)and(t.right is not None)and(isnmb(t.right.value))
    if(s):
        u=(isnmb(t.left.value) and isnmb(t.right.value))
        ul=(isnmb(t.left.value) and not isnmb(t.right.value))
        ur=(not isnmb(t.left.value) and isnmb(t.right.value))
        if(u):
            if(t.value=='+'):
                t.value=t.left.value+t.right.value
                t.left.delnode()
                t.left=None
                t.right.delnode()
                t.right=None
            elif(t.value=='-'):
                t.value=t.left.value-t.right.value
                t.left.delnode()
                t.left=None
                t.right.delnode()
                t.right=None
            elif(t.value=='/'):
                t.value=t.left.value/t.right.value
                t.left.delnode()
                t.left=None
                t.right.delnode()
                t.right=None
            elif(t.value=='*'):
                t.value=t.left.value*t.right.value
                t.left.delnode()
                t.left=None
                t.right.delnode()
                t.right=None
            elif(t.value=='^'):
                t.value=pow(t.left.value,t.right.value)
                t.left.delnode()
                t.left=None
                t.right.delnode()
                t.right=None
        elif(ul):
            if(t.left.value == 0 and t.value == '*'):
                t.right.delnode()
                t.right=None
                t.value=0
                t.left=None
            elif(t.left.value == 1 and t.value == '*'):
                t.left=None
                t.nodecpy(t.right)
            elif(t.left.value == 0 and t.value == '+'):
                t.left=None
                t.nodecpy(t.right)
        elif(ur):
            if(t.right.value == 0 and t.value == '*'):
                t.left.delnode()
                t.left=None
                t.value=0
                t.right=None
            elif(t.right.value == 1 and t.value == '*'):
                t.right=None
                t.nodecpy(t.left)
            elif(t.right.value == 0 and t.value == '+'):
                t.right=None
                t.nodecpy(t.left)
            elif(t.right.value == 1 and t.value == '^'):
                t.right=None
                t.nodecpy(t.left)
            elif(t.right.value == 0 and t.value == '^'):
                t.left.delnode()
                t.left=None
                t.value=1
                t.right=None
            elif(t.right.value == 1 and t.value == '/'):
                t.right=None
                t.nodecpy(t.left)
    elif(s1):
        if(t.value == 'ln'):
            from math import log
            t.value=log((t.right).value)
            t.right.delnode()
            t.right=None
        elif(t.value == 'sin'):
            from math import sin
            t.value=sin((t.right).value)
            t.right.delnode()
            t.right=None
        elif(t.value == 'cos'):
            from math import cos
            t.value=cos((t.right).value)
            t.right.delnode()
            t.right=None  
        elif(t.value == 'sqrt'):
            from math import sqrt
            t.value=sqrt((t.right).value)
            t.right.delnode()
            t.right=None 
        elif(t.value == 'exp'):
            from math import exp
            t.value=exp((t.right).value)
            t.right.delnode()
            t.right=None              

def Et2num(t):
    r=constructTree(Conversion(len(t)).infixToPostfix(t))   
    Eval(r,dvar)
    simpl(r)
    if(isnmb(r.value)and(r.left is None)and(r.right is None)):
        return convint(r.value)
    else:
        print('Cannot evaluate input data')
        return None

def Etconv(r):
    try:
        return int(r)
    except ValueError:
        try:
            return float(r)
        except ValueError:
            try:
                return Et2num(r)
            except ValueError:
                print('Cannot parse input data')
    except TypeError:
        print('Cannot parse input data')
        

def Parse3(s):
    d=s.split()
    u=[]
    for p in d:
        u+=[[Etconv(h) for h in (p[1:-1]).split(',')]]
    return u

def Plot(t):
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    #import numpy as np
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [i[0] for i in t]
    ys = [i[1] for i in t]
    zs = [i[2] for i in t]
    ax.scatter(xs, ys, zs, c='b', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

class Et: 
  
    # Constructor to create a node 
    def __init__(self , value): 
        self.value = value 
        self.left = None
        self.right = None

    def delnode(self): 
        if self is not None:
            del self.value
            if(self.left is not None):            
                self.left.delnode()
            if(self.right is not None):  
                self.right.delnode()
            del self

    def nodecpy(self,t):
        tl=copyEt(t)
        self.delnode()
        self.left=None
        self.right=None
        self.value=tl.value
        if(tl.left is not None):
            self.left=Et('$')
            (self.left).nodecpy(tl.left)
        if(tl.right is not None):
            self.right=Et('$')
            (self.right).nodecpy(tl.right)
        tl.delnode()
        del tl


def setvar(var,val):
    dvar[var]=val

def setfun(namefun,fun):
    dfunc[namefun]=constructTree(Conversion(len(fun)).infixToPostfix(fun))
    inorder(dfunc[namefun])
    print()

def calc(namefun):
    r=Et('$')
    r.nodecpy(dfunc[namefun])
    Eval(r,dvar)
    simpl(r)
    inorder(r)
    print()
    r.delnode()
    del r 

def diffun(namefun,var):
    r=Et('$')
    r.nodecpy(dfunc[namefun])
    Diff(r,var)
    simlp(r)
    inorder(r)
    print()
    del r 

def Expr(s):
    if(s[0]=='setvar'):
        setvar(s[1],float(s[2]))
    elif(s[0]=='setfun'):
        setfun(s[1],s[2])
    elif(s[0]=='calc'):
        calc(s[1])
    elif(s[0]=='diff'):
        diffun(s[1],s[2])
    elif(s[0]=='clear'):
        dvar=presetdvar
        dfunc={}
    elif(s[0]=='clearvar'):
        dvar={}
    elif(s[0]=='clearfun'):
        dfunc={}
    elif(s[0]=='exit'):
        return 0
    elif(s[0]=='plot'):
        Plot(Parse3(' '.join(s[1:])))
    else:
        print("Wrong command!")

k=None
while(k is None):
    k=Expr(input().split())







