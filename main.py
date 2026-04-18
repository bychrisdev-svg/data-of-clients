from add_patient import add_patient
from list_patient import menu_list
from prices import menu_prices
from verification import count_extraction

def main():
    patients = []

    while True:
        print("\n----- Menu -----")
        print("1. Add new patient")
        print("2. List of added patients")
        print("3. Consultation prices")
        print("4. Total number of patients requiring extraction")
        print("5. Quit")

        option = input("\nWhich option will you use?: ").strip()

        if option == "1":
            add_patient(patients)
        elif option == "2":
            menu_list(patients)
        elif option == "3":
            menu_prices(patients)
        elif option == "4":
            count_extraction(patients)
        elif option == "5":
            print("\nGoodbye ;)")
            break
        else:
            print("\nError. Unknown option")
            continue

if __name__ == "__main__":
    main()