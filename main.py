import model
import random as rd
import _thread
import server
import manager
import comunic
import view

# Classe de inicializa��o da aplica��o
class Controller:
    def __init__(self):
        self.manager = manager.DataManager()
        self.comunic = comunic.Comunicacao()
        print('start thread')
        self.server = server.Server(self)
        print('Server Started')
        print(self.server.host,' - ',self.server.port)
        self.view_ = view.View(self)
        self.simulate()
        self.view_.refreshgeral()
        self.view_.start()
        
    # Adicionar a��es iniciais
    # Uma quantidade randomica eh gerada
    def simulate(self):
        lista = self.updatedlist()
        
        el = rd.randint(0, len(lista))
        c = 0
        
        for v in lista.values():
            if c == el:
                self.manager.addcompany(v)
                self.manager.getcompanie_id(v.ref_id).setquantity(rd.randint(2, 10))
                self.view_.requestlistener_(v)
                self.listento(v.ref_id)
                break
            c = c + 1
        

    # Comunicar um pedido de opera��o para o Servidor
    # operation: Objeto Operacao criado na View
    def addoperation(self, operation):
        operation.ip = self.server.host
        operation.port = self.server.port
        
        if not operation.compra and self.manager.getcompanie_id(operation.ref_id).quantity.val < int(operation.quantity):
            return False
        
        _thread.start_new_thread(self.comunic.request_addoperation , (operation, ))
        
        return True
    
    # Comunicar que deseja receber atualiza��es de uma empresa
    def listento(self, identifier):
        emp = self.manager.getcompanie_id(identifier)
        if(emp is None):
            emp = self.comunic.getcompany_id(identifier)
            
            self.manager.addcompany(emp)
            
        self.comunic.request_listento(emp, self.server.host, self.server.port)
        
        print(identifier)
        return emp

    # Comunicar um pedido de lista das empresas do Servidor
    def updatedlist(self):
        return self.comunic.request_companieslist()

    # Recebe notifica��o de mudan�a no valor de uma a��o ouvida
    def notifyupdate(self, identifier, value):
        print(identifier + " updated!!")
        self.manager.getcompanie_id(identifier).price = value
        self.view_.updatevalues(identifier, value)

    # Recebe notifica��o da transa��o efetuada
    def notifycompletion(self, operation):
        print('Notify completion')
        
        if operation.compra == 'true':
            self.manager.getcompanie_id(operation.ref_id).incquantity(operation.quantity)
        else:
            self.manager.getcompanie_id(operation.ref_id).incquantity(int(operation.quantity) * (-1))
            
        self.view_.notifycompletion(operation)
        
        print(self.manager.getcompanie_id(operation.ref_id).quantity)
    
# Inicializa��o da aplica��o
if __name__ == "__main__":
    Controller()
