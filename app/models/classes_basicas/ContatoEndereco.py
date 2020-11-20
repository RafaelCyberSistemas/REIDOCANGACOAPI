class ContatoEndereco(object):

    telefone = None
    celular = None
    email = None
    endereco = None
    complemento = None
    bairro = None
    cep = None
    cidade = None
    estado = None
    pais = None

    def __init__(self, celular, email, endereco, bairro, cidade, estado, pais):
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCelular(self):
        return self.celular

    def setCelular(self, celular):
        self.celular = celular

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getComplemento(self):
        return self.complemento

    def setComplemento(self, complemento):
        self.complemento = complemento

    def getBairro(self):
        return self.bairro

    def setBairro(self, bairro):
        self.bairro = bairro

    def getCep(self):
        return self.cep

    def setCep(self, cep):
        self.cep = cep

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais