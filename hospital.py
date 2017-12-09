class Patients(object):
    def __init__(self,patient_id,patient_name,patient_allergies):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_allergies = patient_allergies
        self.bed_num = "None"


class Hospital(object):
    def __init__(self,hospital_name,hospital_capacity):
        self.hostpital_name = hospital_name
        self.hospital_capacity = hospital_capacity
        self.patients = []

    def admit(self,patient):
        if len(self.patients) >= self.hospital_capacity:
            print "Hospital is full right now cannot admit {}".format(patient.patient_name)
        else:
            self.patients.append(patient)
            patient.bed_num = len(self.patients)
        return self

    def discharge(self,pid):
        for patient in self.patients:
            if patient.patient_id == pid:
                del self.patients[0]
                patient.bed_num = "None"

    def display(self):
        for patient in self.patients:
            print "{} on bed {} has {} allergies".format(patient.patient_name,patient.bed_num,patient.patient_allergies)


p1 = Patients(1, "jon", "flu")
p2 = Patients(2, "don", "cough")
p3 = Patients(3, "mon", "sugar")
p4 = Patients(4, "gon", "lactose")

hosp = Hospital("Good Samaritan", 3)

hosp.admit(p1).admit(p2).admit(p3).admit(p4)
hosp.display()
hosp.discharge(123)
hosp.display()
