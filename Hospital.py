from Doctor import Doctor
from Person import Person

class Hospital:

    def __init__(self):
        self.lista_pazienti = {}
        self.lista_dottori = {}

    def addPerson(self, name, surname, personId):
        person = Person(name, surname, personId)
        if personId not in self.lista_pazienti:
            self.lista_pazienti[personId] = person

    def addDoctor(self, name, surname, personId, doctorId):
                doctor = Doctor(name, surname, personId, doctorId)
                self.lista_dottori[doctorId] = doctor


    ## Person not present exception
    def getPerson(self, personId):
        return self.lista_pazienti[personId]

    ## Doctor not present exception
    def getDoctor(self, doctorId):
        return self.lista_dottori[doctorId]


    def assignDoctor(self, doctorId, personId):
        self.lista_pazienti[personId].setDoctor(doctorId)
        self.lista_dottori[doctorId].addPatient(self.lista_pazienti[personId])







