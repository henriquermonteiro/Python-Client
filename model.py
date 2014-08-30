
# Classe Empresa
class Empresa:
    def __init__(self, name, id_string, price = 0, quantity = 0):
        self.name = name
        self.ref_id = id_string
        self.price = MutableValue(price)
        self.quantity = MutableValue(quantity)

    def setprice(self, new_price):
        self.price.val = new_price

    def setquantity(self, quantity):
        self.quantity.val = quantity

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
        return self.price.val

    def getquantity(self):
        return self.quantity.bal
    
    def encodexml(self):
        enc = '<empresa><name>' + self.name + '</name><ID>' + self.ref_id + '</ID><value>' + str(self.price) + '</value></empresa>'
        
        return enc


# Classe Operacao        
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
        
    def encodexml(self):
        enc = '<operacao><companyID>' + self.ref_id + '</companyID><isCompra>' + str(self.compra) + '</isCompra><quantidade>' + str(self.quantity) + '</quantidade>'
        enc += '<precoUnitarioDesejado>' + str(self.price) + '</precoUnitarioDesejado><IP>' + self.ip + '</IP><porta>' + str(self.port) + '</porta>'
        enc += '</operacao>'
        
        return enc


# Classe para manipular atualizacao dos valores
class MutableValue:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return str(self.val)