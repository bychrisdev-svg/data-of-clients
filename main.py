#Patient data collection by the specialist
def verificationString(prompt):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
        elif any(char.isdigit() for char in x):
            print("Input cannot contain numbers. Please try again.")
            continue
        return x
    
def verificationNumber(prompt):
    while True:
        x = input(prompt).strip()
        if not x:
            print("Input cannot be empty. Please try again.")
        elif any(char.isalpha() for char in x):
            print("Input cannot contain letters. Please try again.")
            continue
        return x

while True:
    DNI = verificationNumber("Enter the patient's DNI: ")
    name = verificationString("Enter the patient's name: ")
    phone = verificationNumber("Enter the patient's phone number: ")
    type_of_client = verificationString("Particular or EPS: ")
    type_of_care = verificationString("Enter the type of care needed: ")
    amount = verificationNumber("Enter the amount to be paid: ")
    priority_of_attention = verificationString("Enter the priority of attention (Normal or Urgent): ")
    appointment_date = verificationNumber("Enter the appointment date (DD-MM-YYYY): ")

    print("\nPatient Data Collected:")
    print(f"DNI: {DNI}")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Client: {type_of_client}")
    print(f"Type of Care: {type_of_care}")
    print(f"Amount: {amount}")
    print(f"Priority of Attention: {priority_of_attention}")
    print(f"Appointment Date: {appointment_date}")

    continue_input = input("\nDo you want to enter another patient's data? (yes/no): ")
    if continue_input.lower() != 'yes':
        break