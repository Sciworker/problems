class Bank:
    def __init__ (self, title, address, course_of_money):
        self.title=title
        self.address=address
        self.course_of_money=course_of_money
    def __get_info_about_bank(self):
        print(self.title, self.address)

class Client:
    def __init__(self, name, address, vozrast):
        self.name =name
        address=address
        vozrast=vozrast
    __passport=''
    def __set_passport(self, seria, number):
        self.__passport=seria + number
       

bank1 = Bank('sber', ['Piskunova','49'], ['TUGRIKI','KLUGERANDY'])
client1 = Client('Ivan Ivanov', ['vaneeva','25'], '25')
client1._Client__set_passport('4509' , '120978')
print(client1._Client__passport)



    

    

