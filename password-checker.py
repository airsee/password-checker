# This "project" checks password strength. Program prompts user for password, and the function password_checker will run
# the password through 5 checks. It returns 2 values, password_strength. Then the program will print the password strength out
# of 5, and give advice if its under 5. 

def main():
    password = input("What is your password? ")
    strength, tips = password_checker(password)
    print(f"Password strength: {strength}/5")
    if tips:
        print(f"Your password {', '.join(tips)}")
        
    
    
def password_checker(password):
    password_strength = 5
    advice = []
    
    #checks length, if its 16 or greater
    if not len(password) >= 16:
        password_strength -= 1
        advice.append("needs to be greater than 16 characters")
        
    # checks if there is at least one UPPERCASE letter  
    has_upper = False
    for upper in password:
        if upper.isupper():
            has_upper = True
    if not has_upper:
        password_strength -= 1
        advice.append("needs to have at least one uppercase letter")
            
    # checks if there is at least one LOWERCASE letter
    has_lower = False
    for lower in password:
        if lower.islower():
            has_lower = True
    if not has_lower:
        password_strength -= 1
        advice.append("needs to have at least one lowercase letter")
        
    # checks for number
    has_number = False
    for number in password:
        if number.isdigit():
            has_number = True
    if not has_number:
        password_strength -= 1
        advice.append("needs to have at least one number")
        
    # checks for special character
    has_specialdigit = False
    for specialdigit in password:
        if specialdigit in "!@#$%^&*()-_=+[]{}|;:',.<>/?~":
            has_specialdigit = True
    if not has_specialdigit:
        password_strength -= 1
        advice.append("needs to have at least one special character")
    
    return(password_strength, advice)


main()