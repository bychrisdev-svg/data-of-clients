from patients.prices import consultation_prices

def show_patient(patients):
    if not patients:
        print("\nNo patients registered")
        return

    print(f"\nTotal Patients: {len(patients)}")
    print("Patients in the list: ")
    for i, patient in enumerate(patients, start=1):
        print(f"{i}. {patient['Name']}: {patient['DNI']}")
    
    option = input("\nIf you wish to know a patient's details, write the corresponding number. Otherwise, write 'no': ").strip().lower()
    if option == "no":
        return
    if not option.isdigit():
        print("Invalid input.")
        return
    
    index = int(option) - 1

    if 0 <= index < len(patients):
        patient = patients[index]
        print("\n--- Patient Details ---")
        for key, value in patient.items():
            print(f"{key}: {value}")
    else:
        print("Patient not found")

def search_dni(patients, allow_prices=False):
    if not patients:
        print("\nNo patients registered.")
        return
    
    patient_dni = input("\nEnter the patient's DNI number: ").strip()

    if not patient_dni.isdigit():
        print("Invalid DNI. DNI must be a number")
        return
    else:
        patient_dni = int(patient_dni)

    for patient in patients:
        if patient["DNI"] == patient_dni:
            print("\n--- DNI found ---")
            if allow_prices:
                total_price = consultation_prices(patient)
                print("DNI:", patient["DNI"])
                print("Patient:", patient["Name"])
                print("Type of Care:", patient["Type of Care"])
                print("Amount:", patient["Amount"])
                print(f"Total: {total_price}")
            else:
                for key, value in patient.items():
                    print(f"{key}: {value}")
            return
        
    print("\nPatient not found")

def menu_list(patients):
    while True:
        print("\n---- Patient List Menu ----")
        print("1. Show Total Patients")
        print("2. Search patient by DNI")
        print("3. Back to main menu")

        option = input("\nSelect your option: ").strip()

        if option == "1":
            show_patient(patients)
        elif option == "2":
            search_dni(patients)
        elif option == "3":
            break
        else:
            print("Unknown option")
            continue