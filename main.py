from Hospital import Hospital
from Person import Person
from Doctor import Doctor

hosp = Hospital()

hosp.addDoctor("giorgio", "butera", "Z983", "H00")
hosp.addDoctor("alessandro", "fumagalli", "Z984", "H01")
hosp.addPerson("guido", "macconi", "P3225")
hosp.addPerson("giannino", "malessere", "P3226")

person1 = Person("guido", "macconi", "P3225")
person2 = Person("giannino", "malessere", "P3226")

doctor1 = Doctor("giorgio", "butera", "Z983", "H00")
doctor2 = Doctor("alessandro", "fumagalli", "Z984", "H01")

hosp.getPerson("P3225")

hosp.assignDoctor("H00", "P3225")
hosp.assignDoctor("H01", "P3226")

paziente = Person("guido", "macconi", "P3225")
paziente.getName()
paziente.getId()
paziente.setDoctor([person1])
paziente.setDoctor([person2])
paziente.getDoctor()

dottore = Doctor("giorgio", "butera", "Z983", "H00")
dottore.addPatient(dottore)


print("ok")
print(person1)
print(person2)
print("\n")
print(doctor1)
print(doctor2)

