#       --Author:- Keshav Bhardwaj--

#        --Print Statement--

print("Hello World")
print(28)
print(23*43)
print(34+45)
print("Hey" ,6 ,7 , sep="~" , end="007")
 
#     --These line i wrote in the the front of #are the comments.

print("We can write comments in front of line") #Like this one 

#       --Escape sequence character--

print("I am a good boy \n and i am an artist also")

print('I am a \'Good Boy\'')

#        --Variables-- 

a = 1
print(a)   # We can only write variable to get the value stored in it
b = "Keshav"
print(b)

#       --Data Types--

a = 1234214 #integer
b = 1.3  #float
c = complex(4,2) #complex number
d = "Keshav" #string
e = True  #Boolean
list = [1,2,3, "Keshav"]
print(list[2])

Tupple = (1,2,3, "Keshav")
print(list[2])

dict = {"name":"Keshav","job":"AI System Engineer"} #dictionary
print(dict["name"])

#         --Typecasting--

a = "1"
b = "2"

print(int(a) + int(b)) # Explicit typecasting (we order it to convert)

x = 1.7
y = 4 
sum = x + y

print(sum) # Implicit Typecasting (Python converted it itself in the float from int)
