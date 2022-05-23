from Hospital import Hospital
from Person import Person
from Doctor import Doctor

hosp = Hospital()

hosp.addDoctor("giorgio", "butera", "Z983", "H00")
hosp.addDoctor("alessandro", "fumagalli", "Z984", "H01")
hosp.addPerson("guido", "macconi", "P3225")
hosp.addPerson("giannino", "malessere", "P3226")

hosp.getDoctor("H00")
hosp.getDoctor("H02")
hosp.getPerson("P3225")
hosp.getPerson("3i0")
#il paziente non esiste

hosp.assignDoctor("H00", "P3225")
hosp.assignDoctor("H01", "P3226")

paziente = Person("guido", "macconi", "P3225")
paziente.getName()
paziente.getId()
paziente.setDoctor([{'name':"guido", 'surname':"macconi",'personId':"P32255",'doctorId':"H00"}])
paziente.getDoctor()

dottore = Doctor("giorgio", "butera", "Z983", "H00")
dottore.addPatient(dottore)



print("ok")