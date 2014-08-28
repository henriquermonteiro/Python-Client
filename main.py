import model
import manager
import comunic
import view

class Controller:
    def __init__(self):
        self.manager = manager.DataManager(self)
        self.comunic = comunic.Comunicacao(self)
        self.view = view.View(self)

#view chama o main para repassar para comunic
  #   def addoperation(self, operation):
  #      self.comunic.

#    def listento(self, identifier):

    def updatedlist(self):
        return self.comunic.request_companieslist()


#Sei lá ....
#    def updateview(self):


#Comunic chama o main para repassar para a view
#    def notifyupdate(self, identifier, value):


#    def notifycompletion(self, operation):


    
if __name__ == "__main__":
    Controller()