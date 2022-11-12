my_string = "Hi there how are you"
print("The string is ")
print(my_string)
my_counter=0

for i in my_string:
   if(i.islower()):
      my_counter=my_counter+1
print("The number of lowercase characters in the string are :")
print(my_counter)