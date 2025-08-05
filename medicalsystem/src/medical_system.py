from datetime import datetime
from appointment import Appointment
from doctor import Doctor
from patient import Patient


class MedicalSystem:
    def __init__(self):
        self.__patient_records = {}
        self.__doctor_records = {}
        self.__appointments = []


    def add_patient(self, patient):
        self.__validate_patient(patient)
        self.__patient_records[patient.get_id] = patient

    def add_doctor(self, new_doctor: Doctor):
        self.__validate_doctor(new_doctor)
        self.__doctor_records[new_doctor.get_id] = new_doctor


    def assign_doctor_to_patient(self, patient: Patient, date: str):
        new_date: datetime = self.__validate_appointment_date(date)
        self.__check_future_date(new_date)

        for doctor in self.__doctor_records.values():
            if patient.speciality_needed == doctor.specialisation:
                new_appointment = Appointment(patient, doctor, date)
                self.__appointments.append(new_appointment)
                patient.add_medical_history(new_appointment)
                return f"Appointment has been scheduled for patient {patient.name} on {new_date.strftime('%d/%m/%Y %H:%M%p')}"

        return f"No doctor available for this patient"


    def view_all_appointments(self):
        print("Scheduled appointments:")
        for appointment in self.__appointments:
            print(appointment)

        if not self.__appointments:
            print("No appointments scheduled.")


    def view_all_doctors(self):
        for doctor in self.__doctor_records.values():
            print(doctor)

        if not self.__doctor_records:
            print("No doctors available.")


    def view_all_patients(self):
        for patient in self.__patient_records.values():
            print(patient)
        if not self.__patient_records:
            print("No patients available.")


    def cancel_appointment(self, patient_id: str, date: str):
        cancel_date: datetime = self.__validate_appointment_date(date)

        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id and appointment.date == cancel_date:
                self.__appointments.remove(appointment)
                return f"Appointment for patient {appointment.patient.name} on {date} has been cancelled"
        return "No appointment scheduled for this patient"

    def reschedule_appointment(self, patient_id: str, old_date_str: str, new_date_str: str):
        old_date: datetime = self.__validate_appointment_date(old_date_str)
        new_date: datetime = self.__validate_appointment_date(new_date_str)
        self.__check_future_date(new_date)

        if not patient_id:
            raise ValueError("Patient id cannot be empty")

        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id and appointment.date == old_date:
                appointment.date = new_date
                return f"Appointment for patient {appointment.patient.name} has been rescheduled to {new_date_str}"
        raise ValueError("No appointment scheduled for this patient")


    def get_patient_appointment(self, patient_id: str):
        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id:
                return str(appointment)

        return "No appointments found for this patient"

    def get_doctor_appointments(self, doctor_id: str):
        for appointment in self.__appointments:
            if appointment.doctor.get_id == doctor_id:
                return str(appointment)

        return  "No appointments for this doctor."

    def get_patient_medical_history(self, patient_id: str):
        patient = self.__patient_records.get(patient_id)
        if not patient:
            raise ValueError("Patient not found")

        history = patient.get_medical_history()
        if not history:
            return "No medical history available"
        result = f"Medical history for patient {patient.name} with ID {patient_id}\n"
        for app, appointment in enumerate(history, 1):
            result += f"{app}. {appointment}\n"
        return result


    def get_patient_by_id(self, patient_id: str):
        patient = self.__patient_records.get(patient_id)
        if not patient:
            raise ValueError("Patient ID not found")
        return patient


    def get_doctor_by_id(self, doctor_id: str):
        doctor = self.__patient_records.get(doctor_id)
        if not doctor:
            raise ValueError("Doctor ID not found")
        return doctor


    def find_patient_record(self, patient_id):
        for ID, patient in self.__patient_records.items():
            if ID == patient_id:
                return str(patient)
        raise ValueError("Patient not found.")


    def find_doctor_record(self, doctor_id):
        for ID, doctor in self.__doctor_records.items():
            if ID == doctor_id:
                return str(doctor)
        raise ValueError("Doctor not found.")


    def __validate_patient(self, patient: Patient) -> None:
        if patient.get_id in self.__patient_records:
            raise ValueError("Patient already registered")

        if not patient.name:
            raise ValueError('Patient name cannot be empty')
        try:
            dob = datetime.strptime(patient.dob, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Date of birth must be in DD/MM/YYYY format(eg, 10/05/2000)")

        if dob > datetime.today():
            raise ValueError("Date of birth cannot be in the future")

        if not patient.problem:
            raise ValueError('Patient problem cannot be empty')

        if not patient.speciality_needed:
            raise ValueError('Speciality cannot be empty')


    def __validate_doctor(self, doctor: Doctor) -> None:
        if doctor.get_id in self.__doctor_records:
            raise ValueError('Doctor already registered')

        if not doctor.name:
            raise ValueError('Doctor name cannot be empty')

        if not doctor.specialisation:
            raise ValueError('Doctor specialisation cannot be empty')


    @staticmethod
    def __validate_appointment_date(date: str) -> datetime:
        try:
            return datetime.strptime(date, '%d/%m/%Y %H:%M%p')
        except ValueError:
            raise ValueError("Appointment date must be in DD/MM/YYYY HH:MM format")

    @staticmethod
    def __check_future_date(appointment_date: datetime):
        if appointment_date < datetime.today():
            raise ValueError("New appointment date cannot be in the past")

