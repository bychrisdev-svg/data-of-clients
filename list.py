from add_patient import patients

#Patient List
def list_added():          
    for patient in patients:
        print("\nDNI:", patient["DNI"])
        print("Name:", patient["Name"])
        print("Phone:", patient["Phone"])
        print("Type Of Client:", patient["Type of Client"])
        print("Type of Care:", patient["Type of Care"])
        print("Amount:", patient["Amount"])
        print("Priority of Attention:", patient["Priority of Attention"])
        print("Appointment Date:", patient["Appointment Date"])
        print("\n-----------------------------------")