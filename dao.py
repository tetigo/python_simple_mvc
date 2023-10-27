from models import *

class CategoriaDAO:
    @classmethod
    def salvar(cls, categoria:Categoria):
        with open("categoria.txt", "a") as arq:
            arq.writelines(f'{categoria.categoria}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open('categoria.txt','r') as arq:
            linhas=arq.readlines()
            for info in linhas:
                categoria=info.split('\n')[0]
                categ1=Categoria(categoria=categoria)
                temp.append(categ1)
        cls.categoria=temp
        return cls.categoria
    
    @classmethod
    def remover(cls, novaLista):
        with open("categoria.txt","w") as arq:
            for cada in novaLista:
                arq.writelines(f'{cada.categoria}')
                arq.writelines('\n')
        cls.categoria = novaLista
        return cls.categoria
        
    @classmethod
    def atualizar(cls, velho, novo):
        lista = CategoriaDAO.ler()
        result = list(map(lambda cada: Categoria(novo) if cada.categoria == velho else cada,lista))    
        with open("categoria.txt","w") as arq:
            for cada in result:
                arq.writelines(f'{cada.categoria}')
                arq.writelines('\n')
        cls.categoria = result
        return cls.categoria
        
# c1=Categoria("Frutas")
# CategoriaDAO.salvar(c1.categoria)
# CategoriaDAO.salvar(Categoria("Verduras"))
# CategoriaDAO.salvar(Categoria("Legumes"))
# test=CategoriaDAO.ler()
# print(">>",test)
# print(CategoriaDAO.categoria)


class VendaDAO:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("venda.txt","a") as arq:
            arq.writelines(f'{venda.item_vendido.nome}|{venda.item_vendido.preco}|{venda.item_vendido.categoria}*{venda.vendedor.clt}|{venda.vendedor.nome}|{venda.vendedor.telefone}|{venda.vendedor.email}|{venda.vendedor.endereco}|{venda.vendedor.cpf}*{venda.comprador.nome}|{venda.comprador.telefone}|{venda.comprador.email}|{venda.comprador.endereco}|{venda.comprador.cpf}*{venda.quantidade_vendida}*{venda.data}')
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        temp=[]
        with open("venda.txt","r") as arq:
            linhas = arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info =  info.split("*")
                produto=info[0]
                vendedor=info[1]
                cliente=info[2]
                quantidade=info[3]
                data=info[4]
                
                produto=produto.split("|")
                nome=produto[0]
                preco=produto[1]
                categoria=produto[2]
                prod1=Produto(nome=nome, preco=preco,categoria=categoria)
                
                vendedor=vendedor.split("|")
                clt=vendedor[0]
                nome=vendedor[1]
                telefone=vendedor[2]
                email=vendedor[3]
                endereco=vendedor[4]
                cpf=vendedor[5]
                vendedor1=Funcionario(clt=clt, nome=nome, telefone=telefone, email=email, endereco=endereco,cpf=cpf)
                
                cliente=cliente.split("|")
                nome=cliente[0]
                telefone=cliente[1]
                email=cliente[2]
                endereco=cliente[3]
                cpf=cliente[4]
                cli1=Pessoa(nome=nome,telefone=telefone,email=email,endereco=endereco,cpf=cpf)
                
                temp.append(Venda(item_vendido=prod1, vendedor=vendedor1, comprador=cli1, quantidade_vendida=quantidade, data=data))
        cls.venda=temp
        return cls.venda

# prod1= Produto('caneta',5.99, 'papelaria')
# cli1=Pessoa('tiago','123-456','tiago@email.com','rua dos vencedores,1000','123123123123')
# func1= Funcionario('12345', 'jose', '123-123', 'jose@email.com', 'rua caracas, 123','5656565656')
# venda1 = Venda(item_vendido=prod1,vendedor=func1, comprador=cli1,quantidade_vendida=1)

# VendaDAO.salvar(venda1)
# VendaDAO.ler()
# for cada_venda in VendaDAO.venda:
#     print(cada_venda.vendedor)
# print("$$",VendaDAO.venda[0].vendedor.nome)

class EstoqueDAO:
    @classmethod
    def salvar(cls, produto:Produto, quantidade: int):
        with open("estoque.txt","a") as arq:
            arq.writelines(f'{produto.nome}|{produto.preco}|{produto.categoria}*{quantidade}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open("estoque.txt","r") as arq:
            linhas=arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info = info.split("*")
                produto=info[0]
                quantidade = info[1]
                
                produto=produto.split("|")
                nome=produto[0]
                preco=produto[1]
                categoria=produto[2]
                prod1=Produto(nome=nome, preco=preco, categoria=categoria)
                temp.append(Estoque(produto=prod1, quantidade=quantidade))
        cls.estoque=temp
        return cls.estoque

    @classmethod
    def remover(cls, lista):
        with open("estoque.txt","w") as arq:
            for estoque in lista:
                arq.writelines(f'{estoque.produto.nome}|{estoque.produto.preco}|{estoque.produto.categoria}*{estoque.quantidade}')
                arq.writelines('\n')
        cls.estoque=lista
        return cls.estoque        

    @classmethod
    def atualizar(cls, op, **kwargs):
        estoqueFull = cls.ler()
        if op == 1:
            for cada in estoqueFull:
                if cada.produto.categoria == kwargs.get('categoria'):
                    cada.produto.categoria = 'sem categoria'
            with open("estoque.txt","w") as arq:
                for estoque in estoqueFull:
                    arq.writelines(f'{estoque.produto.nome}|{estoque.produto.preco}|{estoque.produto.categoria}*{estoque.quantidade}')
                    arq.writelines('\n')
            cls.estoque=estoqueFull
            return cls.estoque
        if op == 2:
            for cada in estoqueFull:
                if cada.produto.nome == kwargs.get('nome'):
                    cada.produto.nome = kwargs.get('novoNome', cada.produto.nome)
                    cada.produto.preco = kwargs.get('preco', cada.produto.preco)
                    cada.produto.categoria = kwargs.get('categoria', cada.produto.categoria)
                    cada.quantidade = kwargs.get('quantidade', cada.quantidade)
            with open("estoque.txt","w") as arq:
                for estoque in estoqueFull:
                    arq.writelines(f'{estoque.produto.nome}|{estoque.produto.preco}|{estoque.produto.categoria}*{estoque.quantidade}')
                    arq.writelines('\n')
            cls.estoque=estoque
            return cls.estoque
        if op == 3:
            for cada in estoqueFull:
                if cada.produto.categoria == kwargs.get('velho'):
                    cada.produto.categoria = kwargs.get('novo')
            with open("estoque.txt","w") as arq:
                for estoque in estoqueFull:
                    arq.writelines(f'{estoque.produto.nome}|{estoque.produto.preco}|{estoque.produto.categoria}*{estoque.quantidade}')
                    arq.writelines('\n')
            cls.estoque=estoqueFull
            return cls.estoque
        if op == 4:
            for cada in estoqueFull:
                if cada.produto.nome == kwargs.get('produto'):
                    cada.quantidade = int(cada.quantidade) - int(kwargs.get('quantidade'))
            with open("estoque.txt","w") as arq:
                for estoque in estoqueFull:
                    arq.writelines(f'{estoque.produto.nome}|{estoque.produto.preco}|{estoque.produto.categoria}*{estoque.quantidade}')
                    arq.writelines('\n')
            cls.estoque=estoqueFull
            return cls.estoque

        if 1<op>4:
            print("opção não reconhecida")

# prod1= Produto('caneta',5.99, 'papelaria')
# quantidade = 3
# estoque=Estoque(produto=prod1, quantidade=quantidade)
# EstoqueDAO.salvar(estoque=estoque)
# EstoqueDAO.ler()
# print(">>>estoque", EstoqueDAO.estoque[0].produto.nome)

class ProdutoDAO:
    @classmethod
    def salvar(cls, produto:Produto):
        with open("produto.txt","a") as arq:
            arq.writelines(f'{produto.nome}|{produto.preco}|{produto.categoria}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open("produto.txt","r") as arq:
            linhas = arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info = info.split("|")
                nome=info[0]
                preco=info[1]
                categoria=info[2]
                prod1=Produto(nome=nome,preco=preco,categoria=categoria)
                temp.append(prod1)
        cls.produto=temp
        return cls.produto
    
    @classmethod
    def atualizar(cls, produto: Produto, preco):
        lista=ProdutoDAO.ler()
        result = [cada for cada in lista if cada.nome != produto.nome]
        produto.preco=preco
        result.append(produto)
        with open("produto.txt","w") as arq:
            for produto in result:
                arq.writelines(f'{produto.nome}|{produto.preco}|{produto.categoria}')
                arq.writelines('\n')
        ProdutoDAO.produto=result
        return ProdutoDAO.produto
        

class PessoaDAO:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoa.txt","a") as arq:
            arq.writelines(f'{pessoa.nome}|{pessoa.cpf}|{pessoa.endereco}|{pessoa.telefone}|{pessoa.email}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open("pessoa.txt","r") as arq:
            linhas = arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info=info.split("|")
                nome=info[0]
                cpf=info[1]
                endereco=info[2]
                telefone=info[3]
                email=info[4]
                pessoa1=Pessoa(nome=nome, cpf=cpf, email=email, endereco=endereco, telefone=telefone)
                temp.append(pessoa1)
        cls.pessoa=temp
        return cls.pessoa

# PessoaDAO.salvar(pessoa=cli1)

class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario:Funcionario):
        with open("funcionario.txt","a") as arq:
            arq.writelines(f'{funcionario.clt}|{funcionario.nome}|{funcionario.cpf}|{funcionario.endereco}|{funcionario.telefone}|{funcionario.email}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open("funcionario.txt","r") as arq:
            linhas = arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info=info.split("|")
                clt=info[0]
                nome=info[1]
                cpf=info[2]
                endereco=info[3]
                telefone=info[4]
                email=info[5]
                func1=Funcionario(clt=clt,nome=nome, cpf=cpf, email=email, endereco=endereco, telefone=telefone)
                temp.append(func1)
        cls.funcionario=temp
        return cls.funcionario


# a=FuncionarioDAO.salvar(func1)

class FornecedorDAO:
    def salvar(cls, fornecedor:Fornecedor):
        with open("fornecedor.txt","a") as arq:
            arq.writelines(f'{fornecedor.nome}|{fornecedor.cnpj}|{fornecedor.telefone}|{fornecedor.categoria}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        temp=[]
        with open("fornecedor.txt","r") as arq:
            linhas = arq.readlines()
            for info in linhas:
                info = info.split('\n')[0]
                info=info.split("|")
                nome=info[0]
                cnpj=info[1]
                telefone=info[2]
                categoria=info[3]
                func1=Fornecedor(nome=nome, cnpj=cnpj, telefone=telefone, categoria=categoria)
                temp.append(func1)
        cls.fornecedor=temp
        return cls.fornecedor
    

