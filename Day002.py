#         --Operations on Strings--

a = "Keshav"
print(a[3])

print(a[0:5])

print(a[-5:-1])

#       --String methods--

print(len(a)) #len()

print(a.upper()) #upper()

print(a.lower()) #lower()

b = "Keshav#,######,Harry##" #rstrip()
c = b.rstrip("#")

print(c)

d = b.replace("Kesh", "Resh") #replace()

print(d)

e = b.split(",") #split()
print(e)

f = "introducTion to JS" #capitalize()

g = f.capitalize()

print(g)

h = f.center(25) #center()

print(h)

a = "He is well trained. He is also very strong" #count()

b = a.count("is")

print(b)

b = a.endswith("ed",0,18) #endswith()

print(b)

b = a.find("is") #find()

print(b)

b = a.index("is") #index()

print(b)

a = "HeiswelltrainedHeisalsoverystrong" #isalnum()

b = a.isalnum()

print(b)

b = a.isalpha() #isalpha()

print(b)

b = a.islower() #islowe()

print(b)

c = a.isupper() #isupper

print(c)

d = a.isprintable() #isprintable()

print(d)

e = a.isspace() #isspace()

print(e)

f = a.istitle() #istitle()

print(f)

g = a.swapcase() #swapcase()

print(g)

h = a.title() #title()

print(h)

##       --If else statements and conditional operators--

a = int(input("Enter the age: "))

print(a>18)
print(a<18)
print(a<=18)
print(a>=18)
print(a==18)

if (a>18):
    print("you can drive")
    
elif(a==18):
    print("You have to give the test")
    
else:
    print("You cannot Drive")

#               --Nested Condition--

a = int(input("Enter the number: "))

if (a<0):
    print("Number is negative")

elif(a>0):
    if(a<=10):
        print("The number is between 0-10")

    elif(a<=20):
        print("The number is between 11-20")

    else:
        print("The number is greater than 20")

else:
    print("The number is zero")