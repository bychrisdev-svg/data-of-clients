import re

def verificationString(prompt):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if not re.fullmatch(r'[a-zA-Z ]+', x):
            print("Input cannot contain numbers or special characters.")
            continue
        return x
    
def verificationNumber(prompt, allow_dash=False):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if allow_dash == True:
            if not re.fullmatch(r'[0-9-]+', x):
                print("Only numbers and dashes allowed.")
                continue
        else:
            if not re.fullmatch(r'[0-9]+', x):
                print("Input must be a number.")
                continue
        return x