from Person import Person
#DoctorID
#3454FHHG

class Doctor(Person):

    def __init__(self, name, surname, doctorId, personId):
        super(Doctor, self).__init__(name, surname, personId)
        self.doctorId = doctorId
        self.lista_pazienti = {}

    def __repr__(self):
       return "il nome del dottore è " + self.name + " " + "il cognome è " + self.surname + ", il codice identificativo del dottore è " + self.doctorId


    def getDoctorId(self):
        return self.doctorId

    def addPatient(self, person):
        if person not in self.lista_pazienti:
            self.lista_pazienti[person.personId] = person


    def getPatients(self):
        return self.lista_pazienti


