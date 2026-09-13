# #1

# n = int(input("Enter the number: "))

# rev = 0
# while n>0:
#     a = n%10
#     rev = rev*10 + a
#     n = n//10

# print(rev)

# #2

# n = int(input("Enter the number: "))

# b = n%10

# m = 0
# while n>0:
#     a = n%10
#     m = m*10 + a
#     n = n//10


# c = m%10
# s = b + c
# print(s)

# #3

# n = float(input("Enter the number: "))

# a = n - int(n)
# b = round(a,2)

# print(b)

# #4

# n = int(input("Enter the time in seconds: "))

# h = n/3600
# m = (n%3600)/60
# s = n%60

# print(f"Time = {int(h)} Hours, {int(m)} Minutes, {int(s)} Seconds")

# #5

# n = int(input("Enter the amount: "))

# a = n/500
# b = n%500
# c = b/100
# d = b%100
# e = d/50

# print(f"{int(a)} 500 Notes in {n}")
# print(f"{int(c)} 100 Notes in {n}")
# print(f"{int(e)} 50 Notes in {n}")

# #6 

# y = int(input("Enter the year: "))

# print(y%4==0 and y%100!=0 or y%400==0)

# #7

# a = int(input("Enter the first side: "))
# b = int(input("Enter the second side: "))
# c = int(input("Enter the third side: "))

# print((a+b)>c and (b+c)>a and (a+c)>b)

# #8

# n = int(input("Enter the number: "))

# print(not(n%2!=0))

# #9

# n = int(input("Enter the marks: "))

# print(n>60 and n<80 or n==100)

# #10

# s1 = int(input("Enter the marks of subject 1: "))
# s2 = int(input("Enter the marks of subject 2: "))
# s3 = int(input("Enter the marks of subject 3: "))

# a = (s1+s2+s3)/3

# print(a>50 )

# #11

# print(10 + 20 * 30 // 10 ** 2 % 3 - 2.0)

# #12

# print("Circle coordinates:")
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))

# r = int(input("Enter the radius: "))

# print("Random Point coordinates:")
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))

# e = (((x2-x1)**2)-((y2-y1)**2))**1/2

# if (r>e):
#     print(f"Random point lies inside the circle.")

# elif (r<e):
#     print(f"Random point lies outside the circle.")

# else:
#     print(f"Random point lies on the edge of the circle.")

# #13

# b = int(input("Enter the amount: "))

# d = (b >= 2500) * 500
# p = b - d
# print(p)

# #14

# h = int(input("Enter the time: "))

# d = int(input("Enter the delayed time: "))

# t = h + d

# a = t%24

# s = t<24

# print(f"Alaram time:{a}")
# print(f"same day:{s}")

# #15

# n = int(input("Enter the number: "))

# a = n//50

# l = a*50

# b = (n//50)+1

# u = b*50

# print(f"Lower multiple of 50 is {l}")
# print(f"Upper multiple of 50 is {u}")

#16

