from verification import verificationNumber, verificationString

patients = []

#Patient data collection by the specialist
def add_patient():
    while True:
        DNI = verificationNumber("Enter the patient's DNI: ")
        name = verificationString("Enter the patient's name: ")
        phone = verificationNumber("Enter the patient's phone number: ")
        type_of_client = verificationString("Particular, EPS or Prepaid: ")
        type_of_care = verificationString("Enter the type of care needed (Cleaning, Fillings, Extraction, Diagnosis): ")
        amount = verificationNumber("How many things were done in the consultation? (1 for Cleaning and Diagnosis) (For fillings and extractions, please indicate the number of procedures performed): ")
        priority_of_attention = verificationString("Enter the priority of attention (Normal or Urgent): ")
        appointment_date = verificationNumber("Enter the appointment date (DD-MM-YYYY): ", allow_dash=True)

        print("\nPatient Data Collected:")
        print(f"DNI: {DNI}")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Client: {type_of_client}")
        print(f"Type of Care: {type_of_care}")
        print(f"Amount: {amount}")
        print(f"Priority of Attention: {priority_of_attention}")
        print(f"Appointment Date: {appointment_date}")

        patients.append({
        "DNI": DNI,
        "Name": name,
        "Phone": phone,
        "Type of Client": type_of_client,
        "Type of Care": type_of_care,
        "Amount": amount,
        "Priority of Attention": priority_of_attention,
        "Appointment Date": appointment_date
        })

        continue_input = input("\nDo you want to enter another patient's data? (yes/no): ")
        if continue_input.lower() != 'yes':
            break