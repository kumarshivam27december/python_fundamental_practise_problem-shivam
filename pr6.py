m=int(input())
n=int(input())
start, end = m,n
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
        