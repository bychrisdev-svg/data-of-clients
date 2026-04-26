from patients.add_patient import add_patient
from patients.list_patient import menu_list
from patients.prices import menu_prices
from verifications.verification import count_extraction
from appointments.appointment_menu import menu_appointment

def main():
    patients = []

    turn_counter = 0

    while True:
        print("\n----- Menu -----")
        print("1. Add new patient")
        print("2. List of added patients")
        print("3. Consultation prices")
        print("4. Appointments")
        print("5. Total number of patients requiring extraction")
        print("6. Quit")

        option = input("\nWhich option will you use?: ").strip()

        if option == "1":
            add_patient(patients)
        elif option == "2":
            menu_list(patients)
        elif option == "3":
            menu_prices(patients)
        elif option == "4":
            turn_counter = menu_appointment(patients, turn_counter)
        elif option == "5":
            count_extraction(patients)
        elif option == "6":
            print("\nGoodbye ;)")
            break
        else:
            print("\nError. Unknown option")
            continue

if __name__ == "__main__":
    main()