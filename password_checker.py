password=input("Enter the password:")
score=0
if len(password) <= 8:  #checks the length of the password
    print("password should be greater than equal to 8 charectors")
else:
    score+=1
#uppercase check    
has_upper=False
for char in password :
    if char.isupper():
        has_upper=True
        break

if has_upper:
    score+=1
else:
    print("Add at least one uppercase letter")
has_digit=False
for char in password :
    if char.isdigit():
        has_digit=True
        break

if has_digit:
    score+=1
else:
    print("Add at least one number")    
print(f"password score:{score}")


