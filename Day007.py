# Assignment - 02

# #1 

# s = int(input("Enter the Salary: "))

# if (s<30000):
#     print("You have to pay 5% tax.")

# elif (s<=70000):
#     print("You have to pay 15% tax.")

# else:
#     print("You have to pay 25% tax.")

# #2

# def A(a,b): 
      
#     for i in range(a,b+1):
#         if (i%2==0):
#             print(i)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# A(num1,num2)

# #3

# def B(n):

#     if (n<0):
#         n = n*(-1)

#     else:
#         n=n*1

#     count = 0
#     while (n>0):
#         l = n%10
#         a = count + l
#         n = n//10
#         print(a)

# num = int(input("Enter the number: "))

# B(num)

# #4

# def C(n):

#     if n<0:
#         n = n*(-1)
#     else:
#         n = n*1

#     count = 0

#     while (n>0):
#         n = n//10
#         count = count + 1
#     print(count)

# num = int(input("Enter the number: "))

# C(num)

# #5

# def S(n):

#     if (n<0):
#         n = n*(-1)
#     else:
#         n = n*1

#     sum = 0

#     while (n>0):
#         l = n%10
#         sum = sum + l
#         n = n//10

#     print(sum)

# num = int(input("Enter the number: "))
# S(num)   

# #6

# def E(a,b):

#     for i in range(a,b+1):
#         if (i%3==0 and i%5==0):
#             print(i)

# E(1,100)

# # 7(Doubt)

# while True:

#     n = input("Enter the number: ")

#     if (n == "quit"):
#         print("Program Stopped")
#         break
    
    
#     e = float(n)

#     if (e<0):
#         print(f"{e} is negative")
#     elif (e>0):
#         print(f"{e} is positive")
    
    

# #8

# def C(a,b,o):

#     if (o == "+"):
#         print(a+b)

#     elif (o == "-"):
#         print(a-b) 

#     elif (o == "*"):
#         print(a*b)

#     elif (o == "/"):

#         if (b == 0):
#             print("b could not be zero")

#         else:
#             print(a/b)

#     else:
#         print("Invalid term cannot be calculate")

# l = float(input("Enter the number1: "))
# m = float(input("Enter the number2: "))
# n = input("Enter the operation: ")

# C(l,m,n)

# #9

# def is_prime(n):

#     if n <= 1:
#         print(f"{n} is neither prime nor non-prime")
#         return
#     for i in range(2,n):
#         if (n%i==0):
#             print(f"{n} is not prime")
#             return
#     print(f"{n} is Prime")

# num = int(input("Enter the number: "))
# is_prime(num)

# #10

# num = 28

# while True:
#     n = int(input("Guess the number: "))

#     if (n>28):
#         print("Too high")

#     elif (n<28):
#         print("Too low")

#     elif (n==28):
#         print("Congratulations you guessed it right")
#         break
    
    

    