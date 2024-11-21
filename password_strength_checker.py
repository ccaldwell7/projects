import re

def check_password(password):
    digit_error = not re.search(r"\d", password)
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    special_character_error = not re.search(r"\W", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    #This defines the requirements meant for the password by utilizing 're'

    errors = []
    #This whole section tallies the errors in order to later be able to return the errors to the user
    if digit_error:
        errors.append("Password should contain at least one digit.")
    if length_error:
        errors.append("Password should be at least 8 characters long")
    if lowercase_error:
        errors.append("Password should contain at least one lowercase letter.")
    if special_character_error:
        errors.append("Password should contain at least one special character.")
    if uppercase_error:
        errors.append("Password should contain at least one uppercase letter.")

    if not errors:
        return "Password is strong and meets the necessary requirements."
        #If the password meets the requirements this returns to the user
    else:
        return "Password is weak. Please look at the following: \n" + "\n".join(errors)
        # Returns the errors that were found to tell the user what needs to be fixed

#USAGE
password = input("Please enter your password: ")
result = check_password(password)
print(result)
