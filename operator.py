# Program to check the application of logical not operator
print ("Part 1")
a = 10
b = 12
c = 12
#not is used here to reverse the result of (a == b)
print(not (a == b))
# not is used here to reverse the result of (b ==c)
print(not (b == c))

print(" ")
print ("Part 2")
a = "python"
b = "coding"

#not is used here to check that a is not equal to b
if not (a == b):
    print (a, 'and', b, 'are different.')

print("")
print("Part 3")

a = int(input("Enter any number: "))
print("Is 'a' a odd number?... Drumroll pls...")
if not (a%2 == 0):
    print(True)
else:
    print(False)

