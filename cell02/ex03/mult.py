firstnum = int(input("first number: "))
secnum = int(input("second number: "))

mult = firstnum * secnum

print (mult)

if mult > 0:
    print ("The result is positive.")
elif mult < 0:
    print ("The result is negative.")
else:
    print ("The result is both positive and negative.")