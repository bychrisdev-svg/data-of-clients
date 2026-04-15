from add_patient import add_patient
from list_patient import menu_list
from prices import consultation_prices

def main():
    patients = []

    while True:
        print("\n----- Menu -----")
        print("1. Add new patient")
        print("2. List of added patients")
        print("3. Consultation prices")
        print("4. Quit")

        option = input("\nWhich option will you use?: ").strip()

        if option == "1":
            add_patient(patients)
        elif option == "2":
            menu_list(patients)
        elif option == "3":
            consultation_prices(patients)
        elif option == "4":
            print("\nGoodbye ;)")
            break
        else:
            print("Error. Unknown option")
            continue

if __name__ == "__main__":
    main()