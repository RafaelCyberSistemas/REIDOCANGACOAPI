from app.models.classes_basicas.Pessoa import Pessoa

class FornecedorPF(Pessoa):

    id_fornecedorpf = None

    def getIdFornecedorPF(self):
        return self.id_fornecedorpf
        
    def setIdFornecedorPF(self, id_fornecedorpf):
        self.id_fornecedorpf = id_fornecedorpf