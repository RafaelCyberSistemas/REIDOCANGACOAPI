class Produto(object):

    id_produto = None
    descProduto = None
    tipoVolume = None
    preco = None
    id_fornecedorPJ = None
    id_fornecedorPF = None
    status = None

    quantidade = None
    

    def __init__(self, descProduto, tipoVolume, preco, id_fornecedorPJ, id_fornecedorPF, status):
        self.descProduto = descProduto
        self.tipoVolume = tipoVolume
        self.preco = preco
        self.status = status
        self.id_fornecedorPJ = id_fornecedorPJ
        self.id_fornecedorPF = id_fornecedorPF
 
    def getIdProduto(self):
        return self.id_produto

    def setIdProduto(self, id_produto):
        self.id_produto = id_produto

    def getDescProduto(self):
        return self.descProduto

    def setDescProduto(self, descProduto):
        self.descProduto = descProduto

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
    
    def getTipoVolume(self):
        return self.tipoVolume

    def setTipoVolume(self, tipoVolume):
        self.tipoVolume = tipoVolume

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getIdFornecedorPJ(self):
        return self.id_fornecedorPJ

    def setIdFornecedorPJ(self, id_fornecedorPJ):
        self.id_fornecedorPJ = id_fornecedorPJ

    def getIdFornecedorPF(self):
        return self.id_fornecedorPF

    def setIdFornecedorPF(self, id_fornecedorPF):
        self.id_fornecedorPF = id_fornecedorPF

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

