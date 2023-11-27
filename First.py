from math import *
# Question 1:-
def fact (num) :
    f = 1 
    for i in range (1,num+1):
        f = f* i 
    return f
num =int(input("Enter your number "))
print(fact(num))
#_______________________________________________________________
# Question 2:-
def up_lo_case (name):
    counter_lower = 0 
    counter_upper = 0 
    for i in range(len(name)) :
        if (name[i].islower()):
            counter_lower= counter_lower+1 
        elif (name[i].isupper()) :
            counter_upper = counter_upper+1
    print("No. of Upper case characters:" , counter_upper)
    print ("No. of Lower case Characters:" , counter_lower)
name=input("Enter the name ")
up_lo_case(name)
#_______________________________________________________________
# Question 3:-
class Pair_Ele:
    def __init__(self, arr: list):
        self.arr = arr

    def find_pair(self, target):
        indices = []
        size = len(self.arr)
        for i in range(size):
            for j in range(i + 1, size):
                if self.arr[i] + self.arr[j] == target:
                    indices.append((i, j))
        return indices


numbers = [10, 20, 10, 40, 50, 30, 70]
target = 50
finder = Pair_Ele(numbers)
print(finder.find_pair(target))
#______________________________________________________________________
# Question 4 
def is_prime(n):
    for i in range(2,int(n/2)):
      if (n%i) == 0:
         return False
    return True
num = int(input("Enter the number "))
if (is_prime(num)):
    print(num ,"it is Prime")
else:
    print(num ,"it isn't Prime")
    
#_____________________________________________________________________
# Question 5
def is_palindrome(st):
    st=st.lower()
    last = len(st)-1 
    i = 0 
    flag = True
    while(last>i):
        if (st[i]==st[last]):
            last=last-1 
            i=i+1 
        else:
            flag = False
            break 
    if (flag):
        print("Yes, it is palindrome")
    else:
        print("NO, it isn't palindrome")
st = input("Enter The String ")
is_palindrome(st)
#___________________________________________________________________________
# Question 6
def is_pangram (st):
    st = st.lower()
    temp = set(st)
    if (len(temp)==27): #I'm using length 27 because the Set counts the space
        return True
    else:
        return False 
st = input("Enter the String ")
if (is_pangram(st)):
    print ("Yes, it is a pangram")
else:
    print("No, it isn't a pangram")
    
    
        