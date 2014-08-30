import model

# Classe para gerencia das empresas
class DataManager:
    # Inicia lista de empresas
    def __init__(self):
        self.companies = {}

    # Adiciona a empresa na lista
    def addcompany(self, empresa):
        if isinstance(empresa, model.Empresa):
            self.companies[str(empresa.getid())] = empresa

    # Retorna uma determinada empresa atraves do ID
    def getcompanie_id(self, identifier):
        try:
            return self.companies[str(identifier)]
        except:
            return None
    
