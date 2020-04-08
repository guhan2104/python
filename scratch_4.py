a1 = input("enter string: ")
n = input("enter n: ")

s= int(n)
a2 = a1[:s]
print (a2)
a3 = a1[s+1:]
print (a3)
finalstring = a2+a3
print (finalstring)

# s1= input("Enter first string:")
# s2= input("Enter second string:")
# if(sorted(s1) == sorted(s2)):
#       print("The strings are anagrams.")
# else:
#       print("The strings aren't anagrams.")