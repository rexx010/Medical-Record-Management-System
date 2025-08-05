
class Doctor:
    did_counter = 0

    def __init__(self, name, specialisation, contact_info: dict):
        self.id = self.__create_id()
        self.name = name
        self.specialisation = specialisation
        self.contact_info = contact_info

    @classmethod
    def __create_id(cls):
        cls.did_counter += 1
        return f"DOC00{cls.did_counter}"

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

    def _str_(self):
        contact = self.contact_info
        return (
            f"Doctor ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Specialisation: {self.specialisation}\n"
            f"Phone: {contact.get('phone number', '')}\n"
            f"Email: {contact.get('email', '')}\n"
            f"Address: {contact.get('address', '')}\n"
            f"Gender: {contact.get('gender', '')}"
        )
