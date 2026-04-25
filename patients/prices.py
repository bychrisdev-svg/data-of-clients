procedure_prices = {
    "Particular": {
        "Cleaning": 60000,
        "Fillings": 80000,
        "Extraction": 100000,
        "Diagnosis": 50000
    },
    "Eps": {
        "Cleaning": 0,
        "Fillings": 40000,
        "Extraction": 40000,
        "Diagnosis": 0
    },
    "Prepaid": {
        "Cleaning": 0,
        "Fillings": 10000,
        "Extraction": 10000,
        "Diagnosis": 0
    }
}

base_prices = {
    "Particular": 80000,
    "Eps": 5000,
    "Prepaid": 30000
}

def organize_patients(patients):
    if not patients:
        print("\nNo patients registered.")
        return
    
    sorted_patients = sorted(patients, key=lambda patient: consultation_prices(patient), reverse=True)

    print("\n--- List of patients from highest to lowest price ---")
    for patient in sorted_patients:
        total = consultation_prices(patient)
        print("DNI:", patient["DNI"])
        print("Patient:", patient["Name"])
        print("Type of Care:", patient["Type of Care"])
        print("Amount:", patient["Amount"])
        print(f"Total: {total}")
        print("-----------------")

def total_revenue(patients):
    if not patients:
        print("\nNo patients registered")
        return

    total_prices = 0

    for patient in patients:
        total_prices += consultation_prices(patient)

    print("\n--- Total Revenue ---")
    print(f"Total: {total_prices}")
    print("----------------------")

def consultation_prices(patients):
    type_of_client = patients["Type of Client"]
    type_of_care = patients["Type of Care"]
    amount = patients["Amount"]

    price = base_prices.get(type_of_client, 0)
    procedure = procedure_prices.get(type_of_client, {}).get(type_of_care, 0)
    total_price = (procedure * amount) + price
    return total_price

def menu_prices(patients):
    from patients.list_patient import search_dni

    while True:
        print("\n---- Menu Prices ----")
        print("1. Search by patient")
        print("2. Total patient to pay")
        print("3. Total Revenue")
        print("4. Back to main menu")

        option = input("\nSelect your option: ").strip()

        if option == "1":
            search_dni(patients, allow_prices=True)
        elif option == "2":
            organize_patients(patients)
        elif option == "3":
            total_revenue(patients)
        elif option == "4":
            break
        else:
            print("Unknown option")
            continue