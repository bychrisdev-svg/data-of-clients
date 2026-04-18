from verification import verificationNumber, verificationString, validate_date, validate_number

def collect_patient(patients):
    dni = verificationNumber("\nEnter the patient's DNI: ", allow_dni=True, patients=patients)
    name = verificationString("Enter the patient's name: ")
    phone = verificationNumber("Enter the patient's phone number: ")
    type_of_client = verificationString("Particular, EPS or Prepaid: ", allow_client=True)
    type_of_care = verificationString("Enter the type of care needed (Cleaning, Fillings, Extraction, Diagnosis): ", allow_care=True)
    amount = validate_number("How many things were done in the consultation? (1 for Cleaning and Diagnosis) (For fillings and extractions, please indicate the number of procedures performed): ", type_of_care)
    priority_of_attention = verificationString("Enter the priority of attention (Normal or Urgent): ")
    appointment_date = validate_date("Enter the appointment date (YYYY-MM-DD): ")

    return {
        "DNI": dni,
        "Name": name,
        "Phone": phone,
        "Type of Client": type_of_client,
        "Type of Care": type_of_care,
        "Amount": amount,
        "Priority of Attention": priority_of_attention,
        "Appointment Date": appointment_date
    }

def add_patient(patients):
    while True:
        patient = collect_patient(patients)
        patients.append(patient)

        print("\nPatient added successfully!")

        while True:
            continue_input = input("\nDo you want to enter another patient's data? (yes/no): ").strip().lower()
            if continue_input in ['yes', 'no']:
                break
            else:
                print("Unknown option. Please enter 'yes' or 'no'")
        if continue_input != 'yes':
            break