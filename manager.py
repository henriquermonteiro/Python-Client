import model

# Controladora das empresas do cliente
class DataManager:
    def __init__(self):
        self.companies = {}

    # adicao de empresa na lista
    def addcompany(self, empresa):
        if isinstance(empresa, model.Empresa):
            self.companies[str(empresa.getid())] = empresa

    # retorno de uma empresa da lista
    def getcompanie_id(self, identifier):
        try:
            return self.companies[str(identifier)]
        except:
            return None
    
