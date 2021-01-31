from datetime import date
from datetime import datetime
from collections import OrderedDict


class Patient:
    def __init__(self, pid, dob, vax):
        self.id = pid
        self.dateOfBirth = dob
        self.isVaccinated = vax
        self.age = self.calculate_age()

    def calculate_age(self):
        today = date.today()
        dateobj = datetime.strptime(self.dateOfBirth, '%d/%m/%Y')
        self.dateOfBirth = dateobj
        return today.year - self.dateOfBirth.year - \
               ((today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day))


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for j in range(0, len(lst), n):
        yield lst[j:j + n]


def get_percentage(dictionary: OrderedDict, decade: str):
    total = len(dictionary[decade])
    vaccinated = 0
    for x in dictionary[decade]:
        if x.isVaccinated == "Yes":
            vaccinated += 1
    raw = vaccinated / total * 100
    return int(raw)


with open('data1.txt') as file:
    content = file.read()

content = content.split()
content = list(chunks(content, 3))
patients = []

for i in range(len(content)):
    p = Patient(
        pid=content[i][0],
        dob=content[i][1],
        vax=content[i][2]
    )
    patients.append(p)

d = OrderedDict((("0-9", []), ("10-19", []), ("20-29", []), ("30-39", []), ("40-49", []), ("50-59", [])
                 , ("60-69", []), ("70-79", []), ("80-89", []), ("90-", [])))
for patient in patients:
    if 0 <= patient.age <= 9:
        d["0-9"].append(patient)
    elif 10 <= patient.age <= 19:
        d["10-19"].append(patient)
    elif 20 <= patient.age <= 29:
        d["20-29"].append(patient)
    elif 30 <= patient.age <= 39:
        d["30-39"].append(patient)
    elif 40 <= patient.age <= 49:
        d["40-49"].append(patient)
    elif 50 <= patient.age <= 59:
        d["50-59"].append(patient)
    elif 60 <= patient.age <= 69:
        d["60-69"].append(patient)
    elif 70 <= patient.age <= 79:
        d["70-79"].append(patient)
    elif 80 <= patient.age <= 89:
        d["80-89"].append(patient)
    elif 90 <= patient.age:
        d["90-"].append(patient)


if __name__ == "__main__":
    print("Percentages of vaccinated patients by age group: " +
          "\nUnder 10 years old:  " + str(get_percentage(d, "0-9")) + "%" +
          "\n10 to 19:  " + str(get_percentage(d, "10-19")) + "%" +
          "\n20 to 29:  " + str(get_percentage(d, "20-29")) + "%" +
          "\n30 to 39:  " + str(get_percentage(d, "30-39")) + "%" +
          "\n40 to 49:  " + str(get_percentage(d, "40-49")) + "%" +
          "\n50 to 59:  " + str(get_percentage(d, "50-59")) + "%" +
          "\n60 to 69:  " + str(get_percentage(d, "60-69")) + "%" +
          "\n70 to 79:  " + str(get_percentage(d, "70-79")) + "%" +
          "\n80 to 89:  " + str(get_percentage(d, "80-89")) + "%" +
          "\n90 and up:  " + str(get_percentage(d, "90-")) + "%")
