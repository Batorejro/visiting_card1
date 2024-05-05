from faker import Faker
fake = Faker()


def input_data(x):

    mates_data = {}
    for i in range(0, x):
        mates_data[i] = {}
        mates_data[i]['name'] = fake.name()
        mates_data[i]['address'] = fake.address()
        mates_data[i]['company'] = fake.company()
        mates_data[i]['email'] = fake.email()
    print(mates_data)


def main():  
    number_of_crew = 3
    input_data(number_of_crew)  


main()

"""
from faker import Faker
from faker import Factory
fake1 = Factory.create('it_IT')
fake = Faker(['pl_PL'])
#fake2 = 
for _ in range(0, 5):
    print(fake.name())
print(fake1.name())

for _ in range(0, 5):
    print(fake.email())
print(fake.email())

"""
print(12*"ołeło")


class visitingc:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f'visitingc: {self.name} {self.surname} {self.company} {self.position} {self.email}'
    

    def __repr__(self):
        return f" visitingc(name={self.name} surname={self.surname}, company={self.company}, email={self.email})"


visit1 = visitingc(name="Sara", surname="Mitera", company="Zołczan_COMP", position="manager", email="gulsusakarya@example.com")
visit2 = visitingc(name="Richard", surname="Cooc", company="Staman_IND", position="engineer", email="kguichard@example.net")
visit3 = visitingc(name="Adolfino", surname="Zamtuziga", company="Getix", position="boss", email="dmaury@example.org")
wizytowki = [visit1, visit2, visit3]

print(wizytowki)

by_name = sorted(wizytowki, key=lambda visitingc: visitingc.name)
by_surname = sorted(wizytowki, key=lambda visitingc: visitingc.surname)
by_email = sorted(wizytowki, key=lambda visitingc: visitingc.email)


print(12*"ołeło")
print(by_surname)
print(by_email)
print(by_email)

