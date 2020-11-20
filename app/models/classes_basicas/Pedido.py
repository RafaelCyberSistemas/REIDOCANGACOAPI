class Pedido(object):

    id_pedido = None
    dataPedido = None
    statusPedido = None

    id_user = None
    listaProdutos = []

    def __init__(self, id_user):
        self.id_user = id_user

    def add_produto_in_pedido(self, produto):
        self.listaProdutos.append(produto)
        

    def getIdPedido(self):
        return self.id_pedido

    def setIdPedido(self, id_pedido):
        self.id_pedido = id_pedido
 
    def getDataPedido(self):
        return self.dataPedido

    def setDataPedido(self, dataPedido):
        self.dataPedido = dataPedido
  
    def getStatusPedido(self):
        return self.statusPedido

    def setStatusPedido(self, statusPedido):
        self.statusPedido = statusPedido
  
    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = id_user  