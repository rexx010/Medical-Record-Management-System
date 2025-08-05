from datetime import datetime

class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self, patient):
        if not patient:
            raise ValueError("Patient cannot be empty ")
        self.__patient = patient

    @property
    def doctor(self):
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        if not doctor:
            raise ValueError("Doctor cannot be empty")
        self.__doctor = doctor

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date_string):
        if isinstance(date_string, str):
            try:
                appointment_date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
            except ValueError:
                raise ValueError("Appointment date must be in DD/MM/YYYY HH:MM format(eg, 10/05/2000 04:30)")
        elif isinstance(date_string, datetime):
            appointment_date = date_string
        else:
            raise ValueError("Date must be a string or datetime")

        if appointment_date < datetime.today():
            raise ValueError("Appointment date cannot be in the past")

        self.__date = appointment_date

    def __str__(self):
        return (f'Appointment:\n'
                f'Patient: {self.patient.name} with ID: {self.patient.get_id}\n'
                f'Doctor: {self.doctor.name} with ID: {self.doctor.get_id}\n'
                f'Date: {self.date.strftime("%d/%m/%Y %H:%M")}')