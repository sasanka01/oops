class Patients(object):
    def __init__(self,id,name,allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = "None"


class Hospital(object):
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def admit(self,patient):
        if len(self.patients) >= self.capacity:
            print "Hospital is full right now cannot admit {}".format(patient.name)
        else:
            self.patients.append(patient)
            patient.bed_num = len(self.patients)
        return self

    def discharge(self,pid):
        for patient in self.patients:
            if patient.id == pid:
                del self.patients[0]
                patient.bed_num = "None"

    def display(self):
        for patient in self.patients:
            print "{} on bed {} has {} allergies".format(patient.name,patient.bed_num,patient.allergies)


p1 = Patients(1, "jon", "flu")
p2 = Patients(2, "don", "cough")
p3 = Patients(3, "mon", "sugar")
p4 = Patients(4, "gon", "lactose")

hosp = Hospital("Good Samaritan", 3)

hosp.admit(p1).admit(p2).admit(p3).admit(p4)
hosp.display()
hosp.discharge(123)
hosp.display()
