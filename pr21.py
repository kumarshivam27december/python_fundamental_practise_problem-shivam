# def check(string,ch):
#       if not string:
#         return 0
#       elif string[0]==ch:
#             return 1+check(string[1:],ch)
#       else:
#             return check(string[1:],ch)
# string=raw_input("Enter string:")
# ch=raw_input("Enter character to check:")
# print("Count is:")
# print(check(string,ch))
# char=chr(input())
# str=str(input())

# def countLetterString(char, str):
#     if not str:
#         return 0
#     else:
#         return 1 + countLetterString(char, str[1:])


# print(countLetterString()) 

count = 0

my_string = input()
my_char = input()

for i in my_string:
    if i == my_char:
        count += 1

print(count)