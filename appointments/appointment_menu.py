from verifications.verification import separate_appointments

def view_appointments(patients):
    urgent, normal, others = separate_appointments(patients)

    print("\n--- Urgent Extractions ---")
    for patient in urgent:
        print(f"{patient['Name']} - {patient['DNI']} - {patient['Phone']} - {patient['Appointment Date']}")

    print("\n--- Normal Extractions ---")
    for patient in normal:
        print(f"{patient['Name']} - {patient['DNI']} - {patient['Phone']} - {patient['Appointment Date']}")

    print("\n--- Other Appointments ---")
    for patient in others:
        print(f"{patient['Name']} - {patient['DNI']} - {patient['Phone']} - {patient['Appointment Date']}")

def attend_appointment(patients, turn_counter):
    urgent, normal, others = separate_appointments(patients)
    
    cycle = turn_counter % 6

    next_patient = None

    if cycle in [0, 1, 2]:
        if urgent:
            next_patient = urgent[0]
        elif normal:
            next_patient = normal[0]
        elif others:
            next_patient = others[0]

    elif cycle in [3, 4]:
        if normal:
            next_patient = normal[0]
        elif urgent:
            next_patient = urgent[0]
        elif others:
            next_patient = others[0]

    else:
        if others:
            next_patient = others[0]
        elif urgent:
            next_patient = urgent[0]
        elif normal:
            next_patient = normal[0]
    
    if not next_patient:
        print("\nNo appointments scheduled")
        return turn_counter
    
    print("\nPatient attended successfully!")
    print(f"Name: {next_patient['Name']}")
    print(f"DNI: {next_patient['DNI']}")
    print(f"Type: {next_patient['Type of Care']}")
    print(f"Priority: {next_patient['Priority of Attention']}")
    print(f"Date: {next_patient['Appointment Date']}")
    print("------------------------")

    patients.remove(next_patient)

    return turn_counter + 1

def cancel_appointment(patients):
    patient_dni = input("\nEnter the patient's DNI number to cancel the appointment: ").strip()

    if not patient_dni.isdigit():
        print("Invalid DNI. DNI must be a number")
        return
    else:
        patient_dni = int(patient_dni)

    for patient in patients:
        if patient["DNI"] == patient_dni:
            patients.remove(patient)
            print("\nAppointment cancelled successfully")
            return
        
    print("\nPatient not found")

def menu_appointment(patients, turn_counter):
    if not patients:
        print("\nNo patients registered")
        return turn_counter
    
    while True:
        print("\n--- Appointments ---")
        print("1. View scheduled appointments")
        print("2. Attend appointment")
        print("3. Cancel an appointment")
        print("4. Back to main menu")

        option = input("\nWhich option will you use?: ").strip()

        if option == "1":
            view_appointments(patients)
        elif option == "2":
            turn_counter = attend_appointment(patients, turn_counter)
        elif option == "3":
            cancel_appointment(patients)
        elif option == "4":
            return turn_counter
        else:
            print("\nError. Unknown option")
            continue

#Profe voy hacer este pequeño comentario en Español. El codigo lo realice con lo que mas pude entender en la solicitud de la actividad (...)
#(...) porque medio me hice conflicto con lo que solo se debe atender las Extracciones Urgentes y despues abajo nos dijiera (...)
#(...) que se debe atender los demas usuarios segun el orden de la agenda que sería primero las Extracciones Urgentes, entonces (...)
#(...) tome de idea lo que vimos en la clase que paso esta semana para hacer un atencion a los pacientes en orden para que (...)
#(...) todos fueran atendidos y no solo las Extracciones Urgentes. Pero bueno... Este es mi codigo final, la verdad (...)
#(...) aprendi demasiado con este proyecto jajaja.