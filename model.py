class Empresa:
    def __init__(self, name, id_string, price = 0, quantity = 0):
        self.name = name
        self.ref_id = id_string
        self.price = price
        self.quantity = quantity

    def setprice(self, new_price):
        self.price = new_price

    def setquantity(self, quantity):
        self.quantity = quantity

    def incquantity(self, increment):
        self.quantity += increment

        if(self.quantity < 0):
            self.quantity = 0 - self.quantity

    def incprice(self, increment):
        self.price += increment

        if(self.price < 0):
            self.price = 0 - self.price

    def getname(self):
        return self.name

    def getid(self):
        return self.ref_id

    def getprice(self):
        return self.price

    def getquantity(self):
        return self.quantity
        
class Operacao:
    def __init__(self, id_string, compra, desiredprice, desiredquantity, ip = "127.0.0.1", port = 8080):
        self.ref_id = id_string
        self.compra = compra
        self.price = desiredprice
        self.quantity = desiredquantity
        self.ip = ip
        self.port = port
    
    def setprice(self, new_price):
        self.price = new_price

    def setquantity(self, new_quantity):
        self.quantity = new_quantity
    
    def getcompra(self):
        return self.compra
        
    def setcompra(self, compra):
        self.compra = compra

    
