password=input("Enter the password:")
score=0
#checks the length of the password

if len(password) <= 8:#checks the length of the password
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
#Number check    
has_digit=False
for char in password :
    if char.isdigit():
        has_digit=True
        break

if has_digit:
    score+=1
else:
    print("Add at least one number")
#special character
special_chars="!@#$%^&*"
has_special=False
    
for char in password :
    if char in special_chars:
        has_special=True
        break

if has_special:
    score+=1
else:
    print("Add at least one special character(!@#$%^&*)")    
print(f"password score:{score}")
print(f"password score:{score}")

print(f"Final Password Strength:")
if score <= 1:
    print("Weak 🔴")
elif score <= 3:
    print("Medium 🟡")
else:
    print("Strong 🟢")



