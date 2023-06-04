import csv
import json


class Student:

    def __init__(self, name, gender, age, university):
        self.name = name
        self.gender = gender
        self.age = age
        self.university = university

    def this_dict(self):
        this = {
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'university': self.university
        }
        return this

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
            differences.append("Університет: " + self.university + " | " + other.university)
        return differences

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(Student.this_dict(self), file)

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return Student(data['name'], data['gender'], data['age'], data['university'])

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.gender, self.age, self.university])

    @staticmethod
    def load_from_csv(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = next(reader)
            return Student(data[0], data[1], int(data[2]), data[3])


s1 = Student("Коршун Дмитро Андрійович", "чол.", 18, "ХДУ")
s2 = Student('Анастасія Козанцева Олександрівна', 'жін.', 17, 'КПІ')

if s1 == s2:
    print("Студенти однакові")
else:
    print("Студенти мають наступні відмінності: ")
    differences = s1.get_differences(s2)
    for i in range(len(differences)):
        print(differences[i])

print("Створення нового об'єкта на основі іншого через json")
s1.save_to_json('s1.json')
s3 = Student.load_from_json('s1.json')
print(s3.__dict__)

print("Створення нового об'єкта на основі іншого через csv")
s2.save_to_csv('s2.csv')
s4 = Student.load_from_csv('s2.csv')
print(s4.__dict__)
