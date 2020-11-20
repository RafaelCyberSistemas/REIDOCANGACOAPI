class Venda(object):

    id_venda = None
    id_pedido = None
    dataVenda = None
    statusVenda = None
    valorTotalVenda = None

    def __init__(self, id_pedido, dataVenda, statusVenda, valorTotalVenda):
        self.id_pedido = id_pedido
        self.dataVenda = dataVenda
        self.statusVenda = statusVenda
        self.valorTotalVenda = valorTotalVenda

     def getIdVenda(self):
        return self.id_venda

    def setIdVenda(self, id_venda):
        self.id_venda = id_venda
    
    
    def getIdPedido(self):
        return self.Id_pedido

    def setCodPedido(self, id_pedido):
        self.id_pedido = id_pedido

    def getDataVenda(self):
        return self.dataVenda

    def setDataVenda(self, dataVenda):
        self.dataVenda = dataVenda

    def getStatusVenda(self):
        return self.statusVenda

    def setStatusVenda(self, statusVenda):
        self.statusVenda = statusVenda

    def getValorTotalVenda(self):
        return self.valorTotalVenda

    def setValorTotalVenda(self, valorTotalVenda):
        self.valorTotalVenda = valorTotalVenda