# for i in 'hello':
    
    # print(i)
# def reverse(string):
#     _reversed_string = ""
#     for i in string:
#         reversed_string=i+reversed_string
# print("reversed string is:",reversed_string)
# string=input("enter a string:")
# print("entered string",string)
# reverse(string)

def reverseStr(s):
    result=""
    for i in s:
        result=i+result
    return result

s="python"
print(reverseStr(s))