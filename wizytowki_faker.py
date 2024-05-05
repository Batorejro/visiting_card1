from faker import Faker
fake = Faker("it_IT")


class BaseContact:
    def __init__(self, first_name, last_name, email, home_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.home_number = home_number
       
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.company} {self.job} {self.home_number} "
        
    def __repr__(self):
        return f"Card(f_name={self.first_name} l_name={self.last_name}, email={self.email})"
    
    def contact(self):
        return f"Wybieram numer : {self.home_number} i dzwonię do {self.first_name} {self.last_name}"

    def workcontact(self):
        return f"Wybieram numer : {self.work_number} i dzwonię do {self.first_name} {self.last_name} "
    
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), +1])
    

class BussinessContact(BaseContact):
    def __init__(self, work_number, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_number = work_number
        self.company = company
        self.job = job


person_1 = BussinessContact(first_name=fake.first_name(),
                            last_name=fake.last_name(), 
                            company=fake.company(), 
                            job=fake.job(), 
                            email=fake.email(),
                            home_number=fake.phone_number(), 
                            work_number=fake.phone_number())

print(person_1)    
print(person_1.contact()) 
print(person_1.workcontact()) 
print(person_1.label_length) 
#print()     


def create_contacts(rodzaj, ilosc):
    contacts = []
    for i in range(ilosc):
        if rodzaj == 'B':
            ilosc.append(BussinessContact)
        elif rodzaj == 'H':
            ilosc.append(BaseContact)
    return contacts
        

if __name__ == "__main__":
    rodzaj = input("Jaką wizytówke mam utworzyć? B - biznesowa, H - domowa: ")
    ilosc = int(input("Podaj liczbę wizytówek do utworzenia"))
    contacts = create_contacts(rodzaj, ilosc)
    print(contacts)

