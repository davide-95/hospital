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
        if personId in self.lista_pazienti:
            if doctorId not in self.lista_dottori:
                self.lista_dottori[doctorId] = doctor


    ## Person not present exception
    def getPerson(self, personId):
        for person in self.lista_pazienti:
            if personId == person:
                return self.lista_pazienti
            else:
                raise Exception("Paziente non trovato")

    ## Doctor not present exception
    def getDoctor(self, doctorId):
        for doctor in self.lista_dottori:
            if doctorId == doctor:
                return self.lista_dottori
            else:
                raise Exception("Dottore non trovato")


    def assignDoctor(self, doctorId, personId):
        for persona in self.lista_pazienti:
            if personId == persona:
                for dottore in self.lista_dottori:
                    if doctorId == dottore:
                        self.lista_pazienti[persona].setDoctor(dottore)
                        self.lista_dottori[dottore].addPatient(self.lista_pazienti[persona])
                        break






