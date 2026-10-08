a = 0
if not a:
    print(True)
else:
    print(False)
print(not a)
print(bool(a))


a = 10
b = 12
c = 0 

if a and b and c:
    print("All values are True!")
else:
    print("At least one of the values is false")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("One of the numbers is greater than zero.")
else:
    print("Neither of them are greater than zero.")

if b > 0 or c > 0:
    print("One of the numbers is greater than zero.")
else:
    print("Neither of them are greater than zero.")   