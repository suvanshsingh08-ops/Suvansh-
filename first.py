# factorial
'''n=int(input("Enter the number"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)'''

#Armstrong
'''n=int(input("Enter the number"))
t=n
s=0
while n>0:
    d=n%10
    s=s+d**3
    n=n//10
if s==t:
    print("armstrong")
else:
    print("not armstrong")'''

#Palindrome
'''n=input("Enter the number")
t=n
s=0
while n>0:
    d=n%10
    s=s*10+d
    n=n//10
if s==t:
    print("palindrome")
else:
    print("not palindome")'''

#Fibonacci series
'''n=int(input("Enter the number"))
a=0
b=1
for i in range(1,n+1):
    print(a," ",end='')
    c=a+b
    a=b
    b=c'''

#Prime number
'''n=int(input("enter the number"))
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=1
if s==2:
    print("prime")
else:
    print("not prime")'''

# 1^2+2^2+3^2.....n^2
'''n=int(input("Enter the number"))
s=0
for i in range(1,n+1):
    s=s+i**2
print(s)'''

#1/1!+2/2!+3/3!....n/n!
'''n=int(input("Enter the number"))
s=0
for i in range(1,n+1):
    f=1
    for j in range(i,0,-1):
        f=f*j
    s=s+i/f
print(s)'''

#1/1!-2/2!+3/3!....n/n!
'''n=int(input("Enter the number"))
s=0
t=1
for i in range(1,n+1):
    f=1
    for j in range(i,0,-1):
        f=f*j
    s=s+t*i/f
    t=t*-1
print(s)'''

#1
#12
#123
#1234
'''for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#1
#22
#333
#4444
'''for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

#*
#**
#***
'''for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()'''

#333
#22
#1
'''for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

#5
#4 4 
#3 3 3
#2 2 2 2
#1 1 1 1 1
'''for i in range(5,0,-1):
    for y in range(5,i-1,-1):
        print(i,end="")
    print()'''

#5
#5 4
#5 4 3
#5 4 3 2
#5 4 3 2 1

'''for i in range(5,0,-1):
    for y in range(5,i-1,-1):
        print(y,end="")
    print()'''

#*****
#****
#***
#**
#*
"""for i in range(5,0,-1):
    for y in range(1,i+1):
        print("*",end="")
    print()"""

#1 1 1 1 1 
#2 2 2 2 
#3 3 3
#4 4 
#5

'''for i in range(1,6):
    for y in range(5,i-1,-1):
        print(i,end="")
    print()'''


#12345
#1234
#123
#12
#1
'''for i in range(5,0,-1):
    for y in range(1,i+1):
        print(y,end="")
    print()'''

#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5
'''for i in range(1,6):
    for y in range(5,i-1,-1):
        print(y,end="")
    print()'''

#WAP to calculate simple interest
'''P=int(input("Enter P ="))
R=int(input("Enter R ="))
T=int(input("Enter T ="))
Simple_Interest=(P*R*T)/100
print("SI->",Simple_Interest)'''

#WAP to calculate copound interest
'''P=int(input("Enter P ="))
R=int(input("Enter R ="))
T=int(input("Enter T ="))
Compound_interest=P*(1+R/100)**T-P
print("CP",Compound_interest)'''

#WAP to check wether a number is even or odd
'''n=int(input("Enter"))
if n%2==0:
    print("even")
else:
    print("odd")'''

#10.Print a table of any number(n) in this format: n*1=z.
'''n=int(input("enter="))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#18.WAP to reverse of the string
'''my_str="I am live in Mathura."
print(my_str[::-1])'''

#19.WAP to check weather an entered string is palindrome or not.
'''name=input("Enter")
str=''
for i in range(-1,-len(name)-1,-1):
    str += name[i]
if str==name:
    print("Palindrome")
else:
    print("Not Palindrome")
print(str)'''

#20.WAP to split the string  
'''my="my name is suvansh singh yadav"
print(my.split())'''

#21.WAP to replace a substring.
'''text = input("Enter the main string: ")
old = input("Enter the substring to replace: ")
new = input("Enter the new substring: ")

result = text.replace(old, new)

print("Resultant string:", result)'''

#22.WAP to find first and last position of a substring. 😒
'''main = "hello world, hello universe"
sub = "hello"
first = -1
last = -1
for i in range(len(main) - len(sub) + 1):
    if main[i:i+len(sub)] == sub:
        if first == -1:   
            first = i
        last = i        
print("First:", first)
print("Last:", last)'''

#23.WAP to create and print a user define list.
'''n = int(input("Enter the number of elements in the list: "))
user_list = []
for i in range(n):
    element = input("Enter element : ")
    user_list.append(element)
print("The user-defined list is:", user_list)'''

#24.WAP to find sum of all the elements of the list.
'''n=[2,45,6,7,8,9,2]
sum=0
for i in n:
    sum+=i
print("sum of list elements =",sum)'''

#25.WAP to print reverse of the list. 
'''list=[2,3,5,6,7,8,9,0,4,2]
print(list[::-1])'''

#26.WAP to find common elements from two different lists.
'''list1=[2,3,4,5,6,7,8,9]
list2=[2,34,56,78,89,3]
my=[]
for i in list1:
    for y in list2:
        if i==y:
            my.append(i)
print(my)'''

#27.WAP to remove duplicate elements from a list.
'''list1 = [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7]  
my = []
for i in list1:
    if i not in my:  
        my.append(i)
print("List without duplicates:", my)'''

#28.WAP to concatenate two different lists.
'''list1=[2,3,4,5,6,7,8,9]
list2=[2,34,56,78,89,3]
sum=list1+list2
print(sum)'''

#29.WAP to find sum of all the even and odd numbers of the user define list.
'''list1=[1,1,1,2,2,2]
e=0
o=0
for i in list1:
    if i%2==0:
        e+=i
    else:
        o+=i
print("sum of even number",e)
print("odd",o)'''

#30.WAP to find sum of all the numbers from even and odd index of a user define list.
'''list1=[1,1,1,2,2,2]
e=0
o=0
for i in range(0,len(list1)):
    if i%2==0:
        e+=list1[i]
    else:
        o+=list1[i]
print("sum of even index",e)
print("sum of odd index",o)'''

#31.WAP to swap first and last elements of a list.
'''numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("List after swapping:", numbers)'''

#32.WAP to create and print a user define tuple.
'''n = int(input("Enter the number of elements in the tuple: "))
elements = []
for i in range(n):
    value = input("Enter element : ")
    elements.append(value)
user_tuple = tuple(elements)
print("The user-defined tuple is:", user_tuple)'''

#33.WAP to find sum of all the elements of the tuple.
'''tuple1=(1,2,3,4,5,6,7,8,9,10)
s=0
for i in tuple1:
    s+=i
print(s)'''

#34.WAP to print reverse of the tuple.
'''tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1[::-1])'''

#35.WAP to find common elements from two different tuples.
'''tuple1=(2,3,4,5,6,7,8,9)
tuple2=(2,34,56,78,89,3)
my=[]
for i in tuple1:
    for y in tuple2:
        if i==y:
            my.append(i)
        user=tuple(my)    
print(user)'''

#36.WAP to remove duplicate elements from a tuple.
'''tuple1 = [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7]  
my = []
for i in tuple1:
    if i not in my:  
        my.append(i)
    user=tuple(my)
print("List without duplicates:",user)'''

#37.WAP to concatenate two different tuples.
'''tuple1=(2,3,4,5,6,7,8,9)
tuple2=(2,34,56,78,89,3)
sum=tuple1+tuple2
print(sum)'''

#38.WAP to find sum of all the even and odd numbers of the user define tuple.
'''tuple1=(1,1,1,2,2,2)
e=0
o=0
for i in tuple1:
    if i%2==0:
        e+=i
    else:
        o+=i
print("sum of even number",e)
print("odd",o)'''

#39.WAP to find sum of all the numbers from even and odd index of a user define tuple.
'''tuple1=(1,1,1,2,2,2)
e=0
o=0
for i in range(0,len(tuple1)):
    if i%2==0:
        e+=tuple1[i]
    else:
        o+=tuple1[i]
print("sum of even index",e)
print("sum of odd index",o)'''

#40.WAP to swap first and last elements of a tuple.
'''tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)   
list1[0], list1[4] = list1[4], list1[0]  
tuple1 = tuple(list1)  
print(tuple1)'''

#41.WAP to create user define dictionary and display it.
'''n=int(input("enter ="))
dict={}
for i in range(1,n+1):
    keys=input("enter keys")
    values=input("enter values")
    dict[keys]=values
print(dict)'''

#42.WAP to create a dictionary in the format {x : x*x}.
'''n=int(input("enter ="))
dict={}
for i in range(1,n+1):
    k=int(input("enter keys"))
    values=k*k
    dict[k]=values
print(dict)'''

#43.WAP to create the following dictionary: {1:1,2:4,3:9,4:16,5:25}.
'''dict={}
for i in range(1,6):
    k=i
    values=k*k
    dict[k]=values
print(dict)'''

#44.WAP to add a new item in a dictionary.
'''dict={
    "Name":"suvansh",
    "Age":18
}
dict.update({"Cast":"Yadav"})
print(dict)'''

#45.WAP to delete an item from a dictionary.
'''my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
del my_dict['b'] 
print("After Deletion:", my_dict)'''

#46.WAP to concatenate two or more dictionaries.
'''dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}
m={ }
for i in (dict1,dict2,dict3):
    m.update(i)
print("Concatenated Dictionary:",m)'''

#48.WAP to check weather a number is prime or not using user define function.
'''def prime(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=1
    if s==2:
        print("prime")
    else:
        print("not prime")
n=int(input("enter the number"))
prime(n)'''

#50.WAP to demonstrate default arguments of a function.
'''def greet(name="Guest"):
    print("Hello,", name)
greet("Suvansh")   
greet()'''   

#51.WAP to demonstrate keyword arguments of a function.
'''def student_info(name, age):
    print("Name:", name)
    print("Age:", age)
student_info(age=20, name="Suvansh")
student_info(name="Riya", age=22)'''

#52.WAP to demonstrate variable length argument of a function
'''def add_numbers(*numbers):
    total = sum(numbers)
    print("Sum:", total)
add_numbers(10, 20)
add_numbers(5, 15, 25, 35)'''

#53.WAP to demonstrate module.
'''import mymodule

print("Square of 4:", mymodule.square(4))
print("Cube of 3:", mymodule.cube(3))'''

#54.WAP to count the number of lines in a text file.
'''filename = "sample.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))'''

#55.WAP to copy the contents of one file into another.

'''source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print("File copied successfully!")'''