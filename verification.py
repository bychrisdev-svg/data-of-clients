import re

def verificationString(prompt):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if any(c.isdigit() for c in x):
            print("Input cannot contain numbers. Please try again.")
            continue
        if re.search(r'[^a-zA-Z" "]', x):
            print("Input cannot contain especial characters.")
            continue
        return x
    
def verificationNumber(prompt, allow_dash=False):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if any(c.isalpha() for c in x):
            print("Input cannot contain letters. Please try again.")
            continue

        patent = r'[^0-9-]' if allow_dash else r'[^0-9]'

        if re.search(patent, x):
            print("Input cannot contain especial characters.")
            continue
        return x