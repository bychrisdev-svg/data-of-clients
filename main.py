from add_patient import add_patient
from list import list_added
from prices import consultation_prices

#Options Menu
def main():
    program = True
    while program:
        print("\n----- Menu -----")
        print("1. Add new patient")
        print("2. List of added patients")
        print("3. Consultation prices")
        print("4. Quit")

        option = input("\nWhich option will you use?: ")

        if option == "1":
            add_patient()
        elif option == "2":
            list_added()
        elif option == "3":
            consultation_prices()
        elif option == "4":
            print("\nGoodbye ;)")
            program = False
        else:
            print("Error. Unknown option")
            continue

if __name__ == "__main__":
    main()