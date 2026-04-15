import re
from datetime import datetime

def verificationString(prompt, allow_client=False, allow_care=False):
    valid_client = {"particular", "eps", "prepaid"}
    valid_care = {"cleaning", "fillings", "extraction", "diagnosis"}

    while True:
        x = input(prompt).strip().lower()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if not re.fullmatch(r'[a-zA-Z ]+', x):
            print("Input cannot contain numbers or special characters.")
            continue
        if allow_client and x not in valid_client:
            print("Only allowed: Particular, EPS, Prepaid")
            continue
        if allow_care and x not in valid_care:
            print("Only allowed: Cleaning, Fillings, Extraction, Diagnosis")
            continue
        return x.title()
    
def verificationNumber(prompt):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if not re.fullmatch(r'[0-9]+', x):
            print("Input must be a number.")
            continue
        return int(x)
    
def validate_date(prompt):
    while True:
        x = input(prompt).strip()

        try:
            date = datetime.strptime(x, "%Y-%m-%d")
            return x
        except ValueError:
            print("Enter a valid date in format YYYY-MM-DD")

def validate_number(prompt, type_consult):
    consult_one = {"Cleaning", "Diagnosis"}
    consult_max_one = {"Filling", "Extraction"}

    while True:
        x = input(prompt).strip()

        if not x:
            print("Input cannot be empty. Please try again.")
            continue
        if not re.fullmatch(r'[0-9]+', x):
            print("Input must be a number.")
            continue

        x = int(x)

        if type_consult in consult_one:
            if x != 1:
                print("The number must be one. Because you chose the option: Cleaning, Diagnosis.")
                continue
        if type_consult in consult_max_one:
            if not x > 0:
                print("The number must be greater than or equal to one.")
                continue
        return x