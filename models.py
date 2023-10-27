from datetime import datetime

class Categoria:
    def __init__(self, categoria) -> None:
        self.categoria=categoria

class Produto:
    def __init__(self,nome,preco, categoria) -> None:
        self.nome=nome
        self.preco=preco
        self.categoria=categoria


class Estoque:
    def __init__(self,produto: Produto, quantidade) -> None:
        self.produto=produto
        self.quantidade=quantidade
    

class Pessoa:    
    def __init__(self, nome, telefone, email, endereco, cpf) -> None:
        self.nome=nome
        self.cpf=cpf
        self.endereco=endereco
        self.telefone=telefone
        self.email=email
        
    # def __str__(self) -> str:
    #     return f'{self.nome} {self.cpf} {self.endereco} {self.telefone} {self.email}'


class Funcionario(Pessoa):
        def __init__(self, clt, nome, telefone, email, endereco, cpf) -> None:
            super().__init__(nome, telefone, email, endereco, cpf)
            self.clt=clt
        
        # def __str__(self) -> str:
        #     return f'{self.clt} {super().__str__()}'


class Venda:
    def __init__(self, item_vendido: Produto, vendedor:Funcionario, comprador:Pessoa, quantidade_vendida: int, data=datetime.now()) -> None:
        self.item_vendido=item_vendido
        self.vendedor=vendedor
        self.comprador=comprador
        self.quantidade_vendida=quantidade_vendida
        self.data=data
    
    def __str__(self) -> str:
        return f'{self.vendedor}'

class Fornecedor:
    def __init__(self,nome,cnpj,telefone,categoria) -> None:
        self.nome=nome
        self.cnpj=cnpj
        self.telefone=telefone
        self.categoria=categoria
    
