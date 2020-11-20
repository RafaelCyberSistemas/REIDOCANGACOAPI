from app.models.classes_basicas.ContatoEndereco import ContatoEndereco

class Pessoa(object):

    nome = None
    nickName = None
    cpf = None
    sexo = None
    dataNascimento = None
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
    status = None


    def __init__(self, nome, cpf, sexo, dataNascimento, celular, email, endereco, bairro, cidade, estado, pais, status):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.status = status

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getNickName(self):
        return self.nickName

    def setNickName(self, nickName):
        self.nickName = nickName

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo

    def getDataNascimento(self):
        return self.dataNascimento

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

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

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status 