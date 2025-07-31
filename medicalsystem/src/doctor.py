
class Doctor:
    doctor_id_counter = 0

    def __init__(self, name, specialisation, contact_info: dict):
        self.id = self.__create_id()
        self.name = name
        self.specialisation = specialisation
        self.contact_info = contact_info

    @classmethod
    def __create_id(cls):
        cls.doctor_id_counter += 1
        return f"DOC{cls.doctor_id_counter}"

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
    def specialisation(self):
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, specialisation):
       self.__specialisation = specialisation

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        self.__contact_info = contact_info


    def __str__(self):
        return (f'Name: {self.name}.\n'
                f'Doctor contact: {self.contact_info}\n'
                f'Specialisation: {self.specialisation}.\n'
                f'Assigned ID: {self.get_id}')


