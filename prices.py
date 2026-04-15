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


def consultation_prices(patients):
    if not patients:
        print("\nNo patients registered.")
        return
    
    for patient in patients:
        type_of_client = patient["Type of Client"]
        type_of_care = patient["Type of Care"]
        amount = patient["Amount"]

        price = base_prices.get(type_of_client, 0)
        procedure = procedure_prices.get(type_of_client, {}).get(type_of_care, 0)
        total = (procedure * amount) + price

        print("\nPatient:", patient["Name"])
        print("Type of Care:", patient["Type of Care"])
        print("Amount:", patient["Amount"])
        print(f"Total: {total}")
        print("-----------------------------------")