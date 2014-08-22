class Empresa:
    def __init__(self, name, id_string, price = 0, quantity = 0, compra = false):
        self.name = name
        self.ref_id = id_string
        self.price = price
        self.quantity = quantity
        self.compra = compra

    def setprice(self, new_price):
        self.price = new_price

    def setquantity(self, quantity):
        self.quantity = quantity
        
    def setcompra(self, compra):
        self.compra = compra

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
    
    def getcompra(self):
        return self.compra
        
class Operacao:
    def __init__(self, id_string, desiredprice, desiredquantity, ip = "127.0.0.1", port = 8080):
        self.ref_id = id_string
        self.price = desiredprice
        self.quantity = desiredquantity
        self.ip = ip
        self.port = port
    
    def setprice(self, new_price):
        self.price = new_price

    def setquantity(self, new_quantity):
        self.quantity = new_quantity

    
