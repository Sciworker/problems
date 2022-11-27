class magazin:
    type =''
    size =''
    class_magazin=''
    products = []

    def __init__(self, type, size, class_magazin, products):
        self.type = type
        self.size=size
        self.class_magazin = class_magazin
        self.products = products
    def bay(self, client):
        if client.vozrast >= 18 and client.den_sredstva >= 22:
            print('bay and drink')
        else:
            print('idi_gulyi')

class products:
      
     title=''
     sostav =[]
     price = 0
     srok_godnosti=0

     def __init__(self, title, sostav, price, srok_godnosti):
        self.title=title
        self.sostav=sostav
        self.price=price
        self.srok_godnosti = srok_godnosti

class client:
    vozrast=0
    den_sredstva=0

    def __init__(self, vozrast, den_sredstva):
        self.vozrast=vozrast
        self.den_sredstva=den_sredstva
    

magazin1=magazin('food','supermarket','sozial',['vodka', 'vodka_s_perzem','vodka_bez_perza'])
client1=client(14,1000)
products1=products('vodka',['spirt', 'drozzi', 'natural'], 22, 90)
    
magazin1.bay(client1)



     




