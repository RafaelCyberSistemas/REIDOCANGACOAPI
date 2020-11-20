class User(object):

    id_user = None
    username = None
    senha = None
    tipo = None
    id_empregado = None
    status = None

    def __init__(self, username, senha, tipo, id_empregado, status):
        self.username = username
        self.senha = senha
        self.tipo = tipo
        self.id_empregado = id_empregado
        self.status = status

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = id_user

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getIdEmpregado(self):
        return self.id_empregado

    def setIdEmpregado(self, id_empregado):
        self.id_empregado = id_empregado

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status