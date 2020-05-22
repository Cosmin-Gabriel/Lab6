class ContactList(list):
    def search(self,name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.phone = ''


    def __repr__(self):
        if(self.phone == ''):
            return "Contact({}, {})".format(self.name,self.email)
        return "Contact({}, {}, {})".format(self.name,self.email,self.phone)


class Agenda:
    all_contacts = ContactList()

    def add_contact(self,contact):
        self.all_contacts.append(contact)

    def print_agenda(self):
        for contact in self.all_contacts:
            print(contact)


class Friend(Contact):
    def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone = phone

if __name__ == '__main__':
    agenda = Agenda()
    agenda.add_contact(Contact('Ion Popescu','ion_popescu@gmail.com'))
    agenda.add_contact(Friend('Adrian Mircea','mirceaadrian@gmail.com','1234567890'))
    agenda.add_contact(Contact('Ion Ionescu','ion_ionesc@gmail.com'))
    agenda.add_contact(Contact('Alex Apetroaiei', 'alex_apet@gmail.com'))
    agenda.add_contact(Friend('Andrei Ioan','andrei_ioan@gmail.com','0987654321'))
    agenda.print_agenda()