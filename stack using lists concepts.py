"""

stack is a DATA STRUCTURE which uses concepts of LIFO 
LIFO - Last In First Out
to uderstand stack consider a cartoon of capacity of 5 small books
- Adding a book is considered as pushing data --> push(x)
- Removing the book ( top most / last book ) is reffered as poping --> Pop()
- Stack Overflow --> error when trying to push data beyond its size
- Stack Underflow --> error when tryig to remove or accesing empty stack

"""

def push(x):                                # fuction to push data into stack 
    global length                           # if stack is not full 
    arr.append(x)
    length+=1
    print( x ,"pushed.\n")

        
def Pop():                                  # function to pop data from stack
    global length                           # if stack is not empty
    print(arr[length-1] ,"popped.\n")
    arr.pop()
    length-=1

def peek():                                 # function to Display the top most
    print(arr[length-1])

def display():                             # function to display datas
    if length == 0 :                       # from stack
        print("stack boundary error occured.\n")
    else:
        print(arr)

#__main__
arr=[]
length = 0
limit = 5 

while True :                               # infinite loop till exit choice made
    print("1:push")
    print("2:pop")
    print("3:peek")
    print("4:display")
    print("0:exit")
    ch = int(input("enter your choice : "))

    if ch == 1 :
        if length != limit :
            x = int(input("enter data you want to enter :"))
            push(x)
        else:
            print("stack overflow.\n")
                
    elif ch == 2 :
        if length != 0 :
            Pop()
        else:
            print("satck underflow\n")

    elif ch == 3 :
        if length == 0 :                        # data from the stack
            print("stack boundary error stack underflow.\n")
        else:
            peek()
        
    elif ch == 4 :
        display()
    elif ch == 0 :
        break
    else:
        print("invalid input please try again.\n")