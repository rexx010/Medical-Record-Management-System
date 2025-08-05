import unittest
from datetime import datetime, timedelta
from medical_system import MedicalSystem
from patient import Patient
from doctor import Doctor
from appointment import Appointment

class TestMedicalSystem(unittest.TestCase):

    def setUp(self):
        self.system = MedicalSystem()
        self.new_doc = Doctor("Dr. Will", "Dermatology", {"phone": "123456789", "email": "will@gmail.com", "home address": "2, broad street", "gender": "Male"})
        self.new_patient = Patient("Ade", "10/10/1995", "Skin rash", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad way", "email": "ade@gmail.com"})

    def test_that_medical_system_can_add_patient(self):
        self.system.add_patient(self.new_patient)
        self.assertEqual(self.system.find_patient_record(self.new_patient.get_id), str(self.new_patient))

    def test_that_medical_system_cannot_add_same_patient_twice(self):
        self.system.add_patient(self.new_patient)
        self.assertRaises(ValueError, self.system.add_patient, self.new_patient)


    def test_that_medical_system_cannot_add_patient_with_future_dob(self):
        wrong_patient = Patient("ada", "01/01/2026", "Skin disease", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad lane", "email": "ada@gamil.com"})
        self.assertRaises(ValueError, self.system.add_patient, wrong_patient)


    def test_that_medical_system_cannot_add_patient_with_dob_format(self):
        wrong_dob = Patient("ify", "2000/03/23", "skin", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad way", "email": "ade@gmail.com"})
        self.assertRaises(ValueError, self.system.add_patient, wrong_dob)


    def test_that_medical_system_cannot_add_patient_with_no_info(self):
        no_name = Patient("", "10/05/1996", "skin", "Dermatology", {})
        self.assertRaises(ValueError, self.system.add_patient, no_name)

        no_problem = Patient('olu', '10/05/2000', '', 'Dermatology', {})
        self.assertRaises(ValueError, self.system.add_patient, no_problem)

        no_speciality = Patient('ade', '10/05/2000', 'cough', '', {})
        self.assertRaises(ValueError, self.system.add_patient, no_speciality)

    def test_that_medical_system_have_unique_patient_ids(self):
        patient2 = Patient("Bola", "15/06/1990", "Cough", "General", {"phone": "888", "email": "bola@email.com"})
        self.system.add_patient(self.new_patient)
        self.system.add_patient(patient2)
        self.assertNotEqual(self.new_patient.get_id, patient2.get_id)

    def test_that_medical_system_can_add_doctor(self):
        self.system.add_doctor(self.new_doc)
        self.assertEqual(self.system.find_doctor_record(self.new_doc.get_id), str(self.new_doc))


    def test_that_medical_system_cannot_add_same_doctor_id(self):
        self.system.add_doctor(self.new_doc)
        self.assertRaises(ValueError, self.system.add_doctor, self.new_doc)


    def test_that_medical_system_cannot_add_doctor_with_no_info(self):
        no_name = Doctor("", "Cardiology", {})
        self.assertRaises(ValueError, self.system.add_doctor, no_name)

        no_specialty = Doctor('Dr. Will', '', {})
        self.assertRaises(ValueError, self.system.add_doctor, no_specialty)


    def test_that_medical_system_can_assign_doctor_to_patient(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        result = self.system.assign_doctor_to_patient(self.new_patient, "25/08/2026 03:00pm")
        self.assertIn("Appointment has been scheduled for patient Ade", result)


    def test_that_medical_system_cannot_find_doctor(self):
        another_patient = Patient('Ice', '10/01/1995', 'toothache', 'Dentistry', {'phone number': '123456789', 'email': 'ice@email.com', 'home address': 'Den close'})
        self.system.add_patient(another_patient)
        self.system.add_doctor(self.new_doc)
        result = self.system.assign_doctor_to_patient(another_patient, "25/08/2026 02:00pm")
        self.assertIn("No doctor available for this patient", result)

    def test_that_medical_system_doctor_speciality_matches_patient_need(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        date = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M%p")
        self.system.assign_doctor_to_patient(self.new_patient, date)
        appointment = self.new_patient.get_medical_history()[0]
        self.assertEqual(appointment.doctor.specialisation, self.new_patient.speciality_needed)

    def test_that_medical_system_can_get_patient_by_invalid_id(self):
        self.assertRaises(ValueError, self.system.get_patient_by_id, "INVALID123")

    def test_that_medical_system_can_get_doctor_by_invalid_id(self):
        self.assertRaises(ValueError, self.system.get_doctor_by_id, "INVALID456")

    def test_that_medical_system_patient_contact_info_structure_is_valid(self):
        self.assertEqual(self.new_patient.contact_info['phone'], "123456789")
        self.assertIn('email', self.new_patient.contact_info)

    def test_that_medical_system_can_create_appointment_with_datetime_object(self):
        future_datetime = datetime(2025, 12, 25, 14, 30)
        appointment = Appointment(self.new_patient, self.new_doc, future_datetime)
        self.assertEqual(appointment.date, future_datetime)

    def test_that_medical_system_patient_can_have_multiple_appointments(self):
        doctor2 = Doctor("Dr. Ken", "Dermatology", {"phone": "999", "email": "ken@email.com"})
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.system.add_doctor(doctor2)

        date1 = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M%p")
        date2 = (datetime.now() + timedelta(days=2)).strftime("%d/%m/%Y %H:%M%p")

        self.system.assign_doctor_to_patient(self.new_patient, date1)
        self.system.assign_doctor_to_patient(self.new_patient, date2)

        history = self.new_patient.get_medical_history()
        self.assertEqual(len(history), 2)

    def test_appointment_raises_error_for_invalid_date_type(self):
        self.assertRaises(ValueError, Appointment, self.new_patient, self.new_doc, 12345)


    def test_appointment_raises_error_for_past_date(self):
        past_date = "01/01/2020 09:00pm"
        self.assertRaises(ValueError, Appointment, self.new_patient, self.new_doc, past_date)


    def test_appointment_raises_error_for_invalid_string_format(self):
        invalid_format = "2025/12/26 02:30pm"
        self.assertRaises(ValueError, Appointment, self.new_patient, self.new_doc, invalid_format)

    def test_appointment_str_method(self):
        future_date = datetime(2025, 12, 25, 14, 30)
        appointment = Appointment(self.new_patient, self.new_doc, future_date)
        expected = (f"Patient: {self.new_patient.name} with ID {self.new_patient.get_id}\n"
                    f"Doctor: {self.new_doc.name} with ID {self.new_doc.get_id}\n"
                    f"Date: {future_date.strftime('%d/%m/%Y %H:%M%p')}")
        self.assertEqual(str(appointment), expected)

    def test_that_medical_system_can_cancel_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        appointment_date = "25/08/2026 03:00pm"
        self.system.assign_doctor_to_patient(self.new_patient, appointment_date)

        cancel_result = self.system.cancel_appointment(self.new_patient.get_id, appointment_date)
        self.assertIn("Appointment for patient Ade on 25/08/2026 03:00pm has been cancelled", cancel_result)

        result = self.system.get_patient_appointment(self.new_patient.get_id)
        self.assertEqual(result, "No appointments found for this patient")

    def test_that_medical_system_cannot_cancel_appointment_without_booking(self):
        result = self.system.cancel_appointment("", "25/08/2026 03:00pm")
        self.assertIn("No appointment scheduled for this patient", result)

    def test_that_medical_system_can_reschedule_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.system.assign_doctor_to_patient(self.new_patient, "27/09/2026 14:00pm")
        result = self.system.reschedule_appointment(self.new_patient.get_id, "27/09/2026 14:00pm","30/09/2026 11:30am")
        self.assertIn("Appointment for patient Ade has been rescheduled to 30/09/2026 11:30am", result)

    def test_that_medical_system_cannot_reschedule_appointment(self):
        self.assertRaises(ValueError, self.system.reschedule_appointment, "", "01/01/2024 10:00am", "02/01/2024 11:00am")

    def test_that_medical_system_cannot_reschedule_with_wrong_date(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.assertRaises(ValueError, self.system.reschedule_appointment, self.new_patient.get_id, "01/01/2024 10:00am", "02/01/2024 11:00am")

    def test_that_medical_record_can_get_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        date: str = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M%p")
        self.system.assign_doctor_to_patient(self.new_patient, date)
        result = self.system.get_patient_appointment(self.new_patient.get_id)
        expected = (f"Patient: {self.new_patient.name} with ID {self.new_patient.get_id}\n"
                    f"Doctor: {self.new_doc.name} with ID {self.new_doc.get_id}\n"
                    f"Date: {date}")
        self.assertEqual(result, expected)



    def test_that_medical_system_cannot_get_appointment_without_booking(self):
        result = self.system.get_patient_appointment("")
        self.assertEqual(result, "No appointments found for this patient")


    def test_that_medical_system_can_find_patient_record(self):
        self.assertRaises(ValueError, self.system.find_patient_record, self.new_patient.get_id)


    def test_that_medical_system_can_find_doctor_record(self):
        self.assertRaises(ValueError, self.system.find_doctor_record, self.new_doc.get_id)


