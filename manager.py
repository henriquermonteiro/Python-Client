import model

class DataManager:
    def __init__(self):
        self.companies = {}

    def addcompanie(self, empresa):
        if isinstance(empresa, model.Empresa):
            self.companies[str(empresa.getid())] = empresa

    
    def getcompanie_id(self, identifier):
        return self.companies[str(identifier)]

    
