class Patient:
    pid_counter = 0

    def __init__(self, name: str, dob: str, problem: str, speciality_needed: str ,contact_info: dict):
        self.id = self.__create_id()
        self.name = name
        self.dob = dob
        self.problem = problem
        self.speciality_needed = speciality_needed
        self.contact_info = contact_info
        self.medical_history = []


    @classmethod
    def __create_id(cls):
        cls.pid_counter += 1
        return f"PAT00{cls.pid_counter}"

    @property
    def get_id(self):
        return self.id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def problem(self):
        return self.__problem

    @problem.setter
    def problem(self, problem):
        self.__problem = problem

    @property
    def speciality_needed(self):
        return self.__speciality_needed

    @speciality_needed.setter
    def speciality_needed(self, speciality_needed):
        self.__speciality_needed = speciality_needed

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        self.__contact_info = contact_info


    def add_medical_history(self, appointment):
        self.medical_history.append(appointment)

    def get_medical_history(self):
        return self.medical_history

    def _str_(self):
        contact = self.contact_info
        return (
            f"Patient ID: {self.i_d}\n"
            f"Name: {self.name}\n"
            f"DOB: {self.dob}\n"
            f"Problem: {self.problem}\n"
            f"Specialty Needed: {self.speciality_needed}\n"
            f"Phone: {contact.get('phone number', '')}\n"
            f"Email: {contact.get('email', '')}\n"
            f"Address: {contact.get('address', '')}\n"
            f"Gender: {contact.get('gender', '')}"
        )