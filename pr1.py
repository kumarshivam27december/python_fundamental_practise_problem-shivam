def recursion_sum(n):
   if n <= 1:
       return n
   else:
       return n + recursion_sum(n-1)

num = int(input("enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recursion_sum(num))