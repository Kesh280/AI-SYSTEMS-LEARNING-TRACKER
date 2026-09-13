# --------------------BASIC DRILLS-------------------------



# Print Counting (while): 1 se 50 tak numbers print karo.

i = 0
while(i<51):
    print(i)
    i = i + 1

# Print Counting (for): 1 se 50 tak numbers print karo range() use karke.

for i in range (51):
    print(i)

# Sum of N: 1 se lekar 100 tak ke sabhi numbers ko add karke total Sum print karo.

for i in range(1,101):
    print(i*(i+1)/2)

# ---------------------------------------- Both approaches are right.
  
# By For Loop

total_sum = 0
for i in range(1, 101):
   total_sum = total_sum + i
print("1 se 100 tak ka total sum hai:", total_sum)

# By While Loop 

total_sum = 0
i = 1
while(i<=100):
    total_sum = total_sum + i
    i = i + 1
    print("SUM: ",total_sum)

# Multiplication Table: Ek number lo (jaise 5) aur uska poora table print karo (5 x 1 = 5...).

# By For loop:-

for i in range(11):
    print("4","x",i,"=",4*i)

# By While loop:- 

i = 0
while(i<=10):
    print("4","x",i,"=",4*i)
    i = i + 1

# Even Numbers Only: 1 se 50 ke beech aane wale sirf Even (sam) numbers print karo.

# By For Loop  

for i in range(1,51):
    if(i%2==0):
        print(i)

# By While Loop 

i = 1
while(i<=50):
    if(i%2==0):
        print(i)
    i = i + 1

# Count Digits: Ek number mein total kitne digits hain, yeh count karo (e.g., 4567 mein 4 hain).

# By for loop

n = "893"
count = 0
for i in n:
    count = count + 1
print(count)

# By While loop

n = 893
count = 0
while(n>0):
    n = n//10
    count = count + 1
print(count)

# Sum of Digits: Ek number ke saare digits ko aapas mein plus karo (e.g., 123 ➔ 1+2+3 = 6).

# By While Loop

n = 456
total = 0
while(n>0):
    last_digit = n%10
    total = total + last_digit
    n = n//10
print("Total sum:",total)

# By For loop

n = "875"
sum = 0
for i in n:
    sum = sum + int(i)
print(sum)

# Reverse the Number: Kisi number ko ulta kardo (e.g., 876 ➔ 678).

# By While loop

n = 568
new = 0
while(n>0):
    last_digit = n%10
    new = (new*10) + last_digit
    n = n//10
print(new)

# By For loop

n = "345"
new = ""
for i in n:
    new = i + new 
print(new)

# Palindrome Check: Check karo ki koi number ulta karne par original number jaisa same rehta hai ya nahi (e.g., 121).

# By For Loop

n = str(input("Enter the number: "))
new = ""
for i in n:
    new = i + new
if (n==new):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")

# By While Loop

n = int(input("Enter the number: "))
original = n
new = 0
while(n>0):
    last_digit = n%10
    new = (new*10) + last_digit
    n = n//10
if(original==new):
   print(original,"is a palindrome")
else:
   print(original,"is not a palindrome")
      
# Largest of Three: 3 alag-alag numbers mein se sabse bada number print karo (sirf if-elif-else use karke).

a = int(input("Enter the 1st no. "))
b = int(input("Enter the 2nd no. "))
c = int(input("Enter the 3rd no. "))

if(a>b and a>c):
    print("The largest number:",a)

elif(b>a and b>c):
    print("The Largest number:",b)

else:
    print("The Largest number:",c)

# Leap Year Check: Check karo ki diya hua year leap year hai ya nahi.

year = int(input("Enter the year: "))

if(year%4==0):
    print("This is leap year")

elif(year%400==0):
    print("This is leap year")

else:
    print("This is not leap year")

# Factorial Finder: Kisi number ka factorial nikalo (e.g., 5! = 5 * 4 * 3 * 2 * 1).

# By For Loop

m = int(input("Enter the number:"))
n = 1
for i in range(m):
    n = n*(i + 1)
print(n)

# By While Loop

n = 1
i = int(input("Enter the number:"))
while(i>0):
   n = n*i
   i = i - 1
print(n)

# Fibonacci Series: Fibonacci series ke pehle 10 numbers print karo (0, 1, 1, 2, 3, 5, 8...).

# By For Loop

m = int(input("Enter the number: "))
a = 0
b = 1
for i in range(m):
    c = a + b
    print(a)
    a = b
    b = c

# By While Loop

a = 0
b = 1
n = 0
while(n<10):
    print(a)
    c = a + b
    a = b
    b = c
    n = n + 1

# Star Pattern: for loop use karke yeh right-angle triangle print karo:

# By For Loop

n = "*"
for i in range(4):
    print(n)
    n = n + "*"

# By While Loop

n = "*"
i = 0
while(i<4):
   print(n)
   n = n + "*"
   i = i + 1
