import re
from datetime import datetime
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
    user_input = input("Enter your option: ").strip()
    print()

    match user_input:

        case "1":
            contact_info = {}

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
                phone = input("Enter Doctor's Phone Number (11 digits starting with 070,071,080,081,090,091): ").strip()
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

            contact_info['phone number'] = phone
            contact_info['email'] = email
            contact_info['address'] = address
            contact_info['gender'] = gender

            while True:
                try:
                    doctor = Doctor(name, specialisation, contact_info)
                    medical_sys.add_doctor(doctor)
                    print("\nDoctor added successfully:\n")
                    print(doctor)
                    break
                except ValueError:
                    print("Invalid input. Please check and try again.\n")

        case "2":
            contact_info = {}

            while True:
                p_name = input("Enter Patient's Full Name: ").strip().title()
                if p_name:
                    break
                print("Name cannot be empty")

            while True:
                date_of_birth = input("Enter Patient's Date of Birth (DD/MM/YYYY): ").strip()
                try:
                    datetime.strptime(date_of_birth, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Date must be in DD/MM/YYYY format")

            problem = input("Enter the Patient's Problem: ").strip().capitalize()
            specialty = input("Enter Required Speciality: ").strip().capitalize()

            while True:
                phone = input("Enter Patient's Phone Number (11 digits starting with 070,080,081,090,071,091): ").strip()
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

            contact_info['phone number'] = phone
            contact_info['email'] = email
            contact_info['address'] = address
            contact_info['gender'] = gender

            while True:
                try:
                    patient = Patient(p_name, date_of_birth, problem, specialty, contact_info)
                    medical_sys.add_patient(patient)
                    print("\nPatient added successfully:\n")
                    print(patient)
                    break
                except ValueError:
                    print("Invalid patient details. Please check and try again.\n")

        case "3":
            while True:
                pid = input("Enter Patient ID: ").strip()
                try:
                    patient = medical_sys.get_patient_by_id(pid)
                    break
                except ValueError:
                    print("Patient ID not found. Try again.")

            while True:
                schedule_date = input("Enter Appointment Date (DD/MM/YYYY HH:MM): ").strip()
                try:
                    result = medical_sys.assign_doctor_to_patient(patient, schedule_date)
                    print(result)
                    break
                except ValueError as msg:
                    print(msg)

        case "4":
            medical_sys.view_all_appointments()

        case "5":
            while True:
                pid = input("Enter Patient ID: ").strip()
                try:
                    patient = medical_sys.get_patient_by_id(pid)
                    break
                except ValueError:
                    print("Patient ID not found. Try again.")

                date = input("Enter Appointment Date (DD/MM/YYYY HH:MM): ").strip()
                try:
                    result = medical_sys.cancel_appointment(pid, date)
                    print(result)
                    break
                except ValueError as msg:
                    print(msg)

        case "6":
            while True:
                pid = input("Enter Patient ID: ").strip()
                try:
                    patient = medical_sys.get_patient_by_id(pid)
                    break
                except ValueError:
                    print("Patient ID not found. Try again.")

                old_date = input("Enter OLD Appointment Date (DD/MM/YYYY HH:MM): ").strip()
                new_date = input("Enter NEW Appointment Date (DD/MM/YYYY HH:MM): ").strip()
                try:
                    result = medical_sys.reschedule_appointment(pid, old_date, new_date)
                    print(result)
                    break
                except ValueError:
                    print("Invalid appointment date. Please try again.")

        case "7":
            while True:
                pid = input("Enter Patient ID: ").strip()
                try:
                    print(medical_sys.get_patient_appointment(pid))
                    break
                except ValueError:
                    print("Patient ID not found")

        case "8":
            while True:
                did = input("Enter Doctor ID: ").strip()
                try:
                    print(medical_sys.find_doctor_record(did))
                    break
                except ValueError:
                    print("Doctor ID not found")

        case "9":
            while True:
                pid = input("Enter Patient ID: ").strip()
                try:
                    print(medical_sys.find_patient_record(pid))
                    break
                except ValueError:
                    print("Patient ID not found")

        case "10":
            medical_sys.view_all_patients()

        case "11":
            medical_sys.view_all_doctors()

        case "0":
            print("Exiting Medical System. Goodbye!")
            break

        case _:
            print("Invalid option. Please try again.")