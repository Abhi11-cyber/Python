#1.factorial of number using function 
def factorial(n):
 
 if n!=0 or n!=1:
     return n*factorial(n-1)
 else:
     return 1
n=int()
print(f"factorial of{n}is{factorial()}")

#2.string return in function
def my_fun(msg):
    msg="hello world"
    return msg
msg=n
my_fun(msg)
print(my_fun(msg))

#3.sum of  two numbers.
def sum(a,b):
  a = int(input("enter 1st numbers "))
  b = int(input("enter 2nd numbers "))
  return a+b
print(sum(a,b))


# 4.sum of multi numbers.
def sum(*n):
  total=0
  for i in n:
   total=total+i
  print("sum of above numbers is",total)

print(sum(10,20))

def rangesum():
 s = int(input("enter stater number"))
 d = int(input("enter stater number"))
 sum = 0

 for i in range(s,d+1):
    sum=sum+i
 print(sum)

#calculate area and perimeter of rectangle
def recarea():
   l=int(input("enter lenght of rectangle: "))
   b=int(input("enter breadth of rectangle: "))
    
   perimeter=l+l+b+b
   area=l*b
   print("perimeter of rectangle is: ",perimeter)
   print("area of rectangle is: ",area)

