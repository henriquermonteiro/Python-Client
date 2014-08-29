import model

class DataManager:
    def __init__(self):
        self.companies = {}

    def addcompany(self, empresa):
        if isinstance(empresa, model.Empresa):
            self.companies[str(empresa.getid())] = empresa

    
    def getcompanie_id(self, identifier):
        try:
            return self.companies[str(identifier)]
        except:
            return None
    
