import re
from medical_system import MedicalSystem
from doctor import Doctor
from patient import Patient

medical_sys = MedicalSystem()

message = """
Welcome to Medical System 
=========================
press 1 to Add a Doctor
press 2 to Add a Patient
press 3 to Create Appointment
press 4 to View all Appointments
press 5 to Cancel Appointment
press 6 to Reschedule Appointment
press 7 to Get patient Appointments
press 8 to Find doctor Records
press 9 to Find patient Records
press 10 to View all Patients
press 11 to View all Doctors
press 0 to Exit
"""
while True:
    print(message)
    user_input = input("Enter your option: ")
    print()
    match user_input:

        case "1":
            contact_info = {}
            print("Add Doctor")
            while True:
                name = input("Enter Doctor's Full Name: ").strip().title()
                if name:
                    break
                print("Name cannot be empty")

            while True:
                specialisation = input("Enter Doctor's Specialisation: ").strip().title()
                if specialisation:
                    break
                print("Specialisation cannot be empty")

            while True:
                phone = input("Enter Doctor's Phone Number (11 digits starting with 070–091): ").strip()
                if re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                    break
                print("Invalid phone number. Please try again.")
            while True:
                email = input("Enter Doctor's Email Address: ").strip()
                if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                    break
                print("Invalid email address format. Please try again.")

            address = input("Enter Doctor's Address: ").strip().title()
            gender = input("Enter Doctor's Gender: ").strip().capitalize()

            contact_info = {
                "phone number": phone,
                "email": email,
                "address": address,
                "gender": gender
            }

            try:
                doctor = Doctor(name, specialisation, contact_info)
                medical_sys.add_doctor(doctor)
                print("\nDoctor added successfully:\n")
                print(doctor)
            except ValueError:
                print("Invalid input. Please check and try again.\n")

        case "2":
            contact_info = {}
            while True:
                p_name = input("Enter Patient's Full Name: ").strip().title()
                if p_name:
                    break
                print("Name cannot be empty")

            date_of_birth = input("Enter Patient's Date of Birth (DD/MM/YYYY): ").strip()
            problem = input("Enter the Patient's Problem: ").strip().capitalize()
            specialty = input("Enter Required Speciality: ").strip().capitalize()

            while True:
                phone = input("Enter Patient's Phone Number (11 digits starting with 070–091): ").strip()
                if re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                    break
                print("Invalid phone number. Please try again.")

            while True:
                email = input("Enter Patient's Email Address: ").strip()
                if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                    break
                print("Invalid email address format. Please try again.")

            address = input("Enter Patient's Address: ").strip().title()
            gender = input("Enter Patient's Gender: ").strip().capitalize()
            allergies = input("Enter Patient's Allergies: ").strip().capitalize()


            contact_info = {
                "phone": phone,
                "email": email,
                "address": address,
                "gender": gender,
                "allergies": allergies
            }

            try:
                patient = Patient(p_name, date_of_birth, problem, specialty, contact_info)
                medical_sys.add_patient(patient)
                print("\nPatient added successfully:\n")
                print(patient)
            except ValueError:
                print("Invalid patient details. Please try again\n")

        case "3":
            pid = input("Enter Patient ID: ").strip().upper()
            schedule_date = input("Enter Appointment Date (DD/MM/YYYY HH:MM): ").strip()
            try:
                result = medical_sys.assign_doctor_to_patient(medical_sys._MedicalSystem__patient_records[pid],schedule_date)
                print(result)
            except KeyError:
                print("Patient ID not found.")
            except ValueError:
                print("Invalid appointment details.")

        case "4":
            medical_sys.view_all_appointments()

        case "5":
            pid = input("Enter Patient ID: ").strip().upper()
            date = input("Enter Appointment Date (DD/MM/YYYY HH:MM): ").strip()
            try:
                result = medical_sys.cancel_appointment(pid, date)
                print(result)
            except ValueError:
                print("Could not cancel appointment. Check date and ID.")

        case "6":
            pid = input("Enter Patient ID: ").strip().upper()
            old_date = input("Enter OLD Appointment Date (DD/MM/YYYY HH:MM): ").strip()
            new_date = input("Enter NEW Appointment Date (DD/MM/YYYY HH:MM): ").strip()
            try:
                result = medical_sys.reschedule_appointment(pid, old_date, new_date)
                print(result)
            except ValueError:
                print("Could not reschedule. Check details provided.")

        case "7":
            pid = input("Enter Patient ID: ").strip().upper()
            print(medical_sys.get_appointment(pid))

        case "8":
            did = input("Enter Doctor ID: ").strip().upper()
            try:
                print(medical_sys.find_doctor_record(did))
            except ValueError:
                print("Doctor not found.")

        case "9":
            pid = input("Enter Patient ID: ").strip().upper()
            try:
                print(medical_sys.find_patient_record(pid))
            except ValueError:
                print("Patient not found.")

        case "10":
            medical_sys.view_all_patients()

        case "11":
            medical_sys.view_all_doctors()

        case "0":
            print("Exiting Medical System. Goodbye!")
            break

        case _:
            print("Invalid option. Please try again.")
