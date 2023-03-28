import csv
import json


class Student:

    def __init__(self, name, gender, age, university):
        self.name = name
        self.gender = gender
        self.age = age
        self.university = university

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and \
                self.gender == other.gender and \
                self.age == other.age and \
                self.university == other.university
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_differences(self, other):
        differences = []
        if self.name != other.name:
            differences.append("ПІБ: \t\t" + self.name + " | " + other.name)
        if self.gender != other.gender:
            differences.append("Стать: \t\t" + self.gender + " | " + other.gender)
        if self.age != other.age:
            differences.append("Вік: \t\t" + str(self.age) + " | " + str(other.age))
        if self.university != other.university:
            differences.append("Унівеситет: " + self.university + " | " + other.university)
        return differences


s1 = Student("Коршун Дмитро Андрійович", "чол.", 18, "ХДУ")
s2 = Student('Анастасія Козанцева Олександрівна', 'жін.', 17, 'КПІ')

if s1 == s2:
    print("Студенти однакові")
else:
    print("Студенти мають наступні відміності: ")
    differences = s1.get_differences(s2)
    for i in range(len(differences)):
        print(differences[i])
