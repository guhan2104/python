def change(string):
    return string[-1:] + string[1:-1] + string[:1]

change("dfghjuyht")
print(change("dfghjuyht"))




s1 = input('enter string1 : ')
s2 = input('enter string2 : ')
if (len(s1) > len(s2)):
    print ('string1 is greater '+ s1)
else:
    print ('string2 is greater')