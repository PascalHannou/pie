import random
passlen = int(input("Enter the length of the password \n"))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen))

while passlen <= 5:        
    passlen = int(input("No can do. Enter a longer length of the password \n"))
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,passlen))
print(p)

#if passlen <= 5:
    #print("No can do, pick a longer length.")
#else:
 #   print(p)
