char = input("Enter a character: ")
if len(char) == 1:
    if not (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
        print(f"'{char}' is not an alphabet.")
    else:
        print(f"'{char}' is an alphabet.")
else:
    print("You have not entered A CHARACTER... U were supposed to enter one :(.")
