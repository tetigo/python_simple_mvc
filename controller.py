from models import *
from dao import *
from datetime import datetime

class CategoriaController:
    def cadastrarCategoria(self, categoria):
        categ1=Categoria(categoria)
        existe=False
        for cada in CategoriaDAO.ler():
            if cada.categoria == categ1.categoria:
                existe=True
                break
        if not existe:
            CategoriaDAO.salvar(categ1)
            print("Categoria cadastrada com sucesso")
        else:
            print("Categoria já existe")
    def removerCategoria(self, categoriaRemover):
        lista=CategoriaDAO.ler()
        result = [item for item in lista if item.categoria == categoriaRemover]
        if len(result) <=0:
            print('Categoria não encontrada')
        else:
            result = [item for item in lista if item.categoria != categoriaRemover]
            CategoriaDAO.categoria = result
            CategoriaDAO.remover(result)
            print("Categoria removida com sucesso")
            EstoqueDAO.atualizar(1,categoria=categoriaRemover)
            print("Estoque atualizado com sucesso")
    
    def atualizarCategoria(self, velho, novo):
        lista=CategoriaDAO.ler()
        result = [cada for cada in lista if cada.categoria == velho]    
        if len(result) == 0:
            print('Categoria antiga não encontrada')
        else:
            result = [cada for cada in lista if cada.categoria == novo]
            if len(result) > 0:
                print("Categoria nova já existe")
            CategoriaDAO.atualizar(velho=velho, novo=novo)
            print("Categoria atualizada com sucesso")
            EstoqueDAO.atualizar(3,velho=velho, novo=novo)
            print("Estoque atualizado com sucesso")
    
    def mostrarCategoria(self):
        lista=CategoriaDAO.ler()
        if len(lista) ==0:
            print("Lista de categorias vazia")
        else:
            for cada in lista:
                print( f'Categoria: {cada.categoria}')
                
# a=CategoriaController()
# # a.cadastrarCategoria("papelaria")
# a.atualizarCategoria("papelaria","UAUAAAAAA")
# a.mostrarCategoria()


class EstoqueController:
    def cadastrarEstoque(self, nome, preco, categoria, quantidade):
        listaProd = EstoqueDAO.ler()
        prodFound = [cada for cada in listaProd if cada.produto.nome == nome ]
        if(len(prodFound)) > 0:
            print('Produto já cadastrado no estoque')
            return
        listaCateg= CategoriaDAO.ler()
        categFound = [cada for cada in listaCateg if cada.categoria == categoria]
        if (len(categFound)) == 0:
            print("Categoria não encontrada")
            return
        prod1=Produto(nome=nome, preco=preco, categoria=categoria)
        EstoqueDAO.salvar(prod1, quantidade)
        
        
    def removerEstoque(self, produtoRemover):
        lista=EstoqueDAO.ler()
        result = [item for item in lista if item.produto.nome == produtoRemover]
        if len(result) <=0:
            print('Produto não encontrado no estoque')
        else:
            result = [item for item in lista if item.produto.nome != produtoRemover]
            EstoqueDAO.remover(result)
            print("Estoque removida com sucesso")
            
    def alterarEstoque(self,nome, categoria, **kwargs):
        lista=EstoqueDAO.ler()
        prodFound= [cada for cada in lista if cada.produto.nome == nome]
        if len(prodFound) == 0:
            print('Produto não existe no estoque')
            return
        listaCateg= CategoriaDAO.ler()
        categFound = [cada for cada in listaCateg if cada.categoria == categoria]
        if (len(categFound)) == 0:
            print("Categoria não encontrada")
            return
        EstoqueDAO.atualizar(
            2,
            nome=nome, 
            categoria=categoria, 
            novoNome=kwargs.get('novoNome', prodFound[0].produto.nome), 
            preco=kwargs.get('preco',prodFound[0].produto.preco),  
            quantidade=kwargs.get('quantidade',prodFound[0].quantidade)
        )
        print("Estoque produto atualizado com sucesso")
        
    def mostrarEstoque(self):
        lista = EstoqueDAO.ler()
        if len(lista) == 0:
            print('Estoque vazio')
        else:
            for cada in lista:
                print(f'Produto....: {cada.produto.nome}')
                print(f'Preço......: {cada.produto.preco}')
                print(f'Categoria..: {cada.produto.categoria}')
                print(f'Quantidade.: {cada.quantidade}\n')
                
                
                
                
# a=EstoqueController()
# a.cadastrarEstoque('banana', 6.78 ,'Frutas', 200)
# a.cadastrarEstoque('uva', 6.78 ,'Frutas', 200)
# a.removerEstoque('nanica')
# a.alterarEstoque(nome='banana', novoNome='nanica', preco=3.49, categoria='Frutas', quantidade=10)
# a.alterarEstoque(nome='banana', categoria='Frutas', preco=2.49, quantidade=5)
# a.mostrarEstoque()

class VendaController:
    def cadastrarVenda(self, produto, vendedor, comprador, quantidade):
        estoque = EstoqueDAO.ler()
        prodFound = [cada for cada in estoque if cada.produto.nome == produto]
        if len(prodFound) == 0:
            print("Produto não consta no estoque")
            return
        if int(prodFound[0].quantidade) < int(quantidade):
            print(f'Total de itens disponíveis em estoque: {prodFound[0].quantidade}')
            return
        vendList = FuncionarioDAO.ler()
        vendedor = [cada for cada in vendList if cada.nome == vendedor]
        if len(vendedor) == 0:
            print("Funcionário não localizado")
            return
        cliList = PessoaDAO.ler()
        cliente = [cada for cada in cliList if cada.nome == comprador]
        if len(cliente) == 0:
            print("Cliente não encontrado")
            return
        venda1 = Venda(
            item_vendido=Produto(nome=prodFound[0].produto.nome,preco=prodFound[0].produto.preco,categoria=prodFound[0].produto.categoria),
            vendedor=Funcionario(clt=vendedor[0].clt,nome=vendedor[0].nome,telefone=vendedor[0].telefone, email=vendedor[0].email, endereco=vendedor[0].endereco, cpf=vendedor[0].cpf),
            comprador=Pessoa(nome=cliente[0].nome, telefone=cliente[0].telefone, email=cliente[0].email, endereco=cliente[0].endereco, cpf=cliente[0].cpf),
            quantidade_vendida=1
        )
        VendaDAO.salvar(venda1)
        EstoqueDAO.atualizar(4, produto=venda1.item_vendido.nome, quantidade=venda1.quantidade_vendida)

    
    def relatorioVenda(self):
        lista = VendaDAO.ler()
        obj={}
        for cada in lista:
            if obj.get(cada.item_vendido.nome):
                obj[cada.item_vendido.nome]+=int(cada.quantidade_vendida)
            else:
                obj.__setitem__(cada.item_vendido.nome, int(cada.quantidade_vendida))
        lista2=[]
        for k,v in obj.items():
            temp={}
            temp['nome']=k
            temp['quantidade']=v
            lista2.append(temp)
        listaOrdenada=sorted(lista2, key=lambda cada: cada['quantidade'], reverse=True)
        print(listaOrdenada)
    
    def mostrarVenda(self, dataInicio, dataFim):
        lista = VendaDAO.ler()
        resultado = list(filter(lambda cada: cada if datetime.fromisoformat(dataFim) >= datetime.fromisoformat(cada.data) >= datetime.fromisoformat(dataInicio) else None,lista))
        for cada in resultado:
            print(f'Produto.....: {cada.item_vendido.nome}')
            print(f'Preço.......: {cada.item_vendido.preco}')
            print(f'Categoria...: {cada.item_vendido.categoria}')
            print(f'Funcionario.: {cada.vendedor.nome}')
            print(f'Cliente.....: {cada.comprador.nome}')
            print(f'Quantidade..: {cada.quantidade_vendida}')
            print(f'Total.......: R$ {int(cada.quantidade_vendida) * float(cada.item_vendido.preco)}')
            print(f'Data........: {cada.data}\n')
            

# a=VendaController()
# a.cadastrarVenda('uva', 'jose', 'tiago', 1)
# a.relatorioVenda()
# a.mostrarVenda('2023-10-23', '2023-10-27')


class FornecedorController:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        lista = FornecedorDAO.ler()
        resultCnpj = [cada for cada in lista if cada.cnpj == cnpj]
        if len(resultCnpj) > 0:
            print("Fornecedor já cadastrado")
            return
        resultTel = [cada for cada in lista if cada.telefone == telefone]
        if len(resultTel) > 0:
            print("Telefone já cadastrado")
            return
        fornec1 = Fornecedor(nome=nome, cnpj=cnpj, telefone=telefone, categoria=categoria)
        FornecedorDAO.salvar(fornec1)
        print("Fornecedor cadastrado com sucesso")
    
class PessoaController:
    def cadastrarCliente(self, nome, telefone, cpf ,email, endereco):
        lista = PessoaDAO.ler()
        resultCli = [cada for cada in lista if cada.cpf == cpf]
        if len(resultCli) > 0:
            print("Cliente já cadastrado")
            return
        resultTel = [cada for cada in lista if cada.telefone == telefone]
        if len(resultTel) > 0:
            print("Telefone já cadastrado")
            return
        cli1 = Pessoa(nome=nome, telefone=telefone, cpf=cpf, email=email, endereco=endereco)
        PessoaDAO.salvar(cli1)
        print("Cliente cadastrado com sucesso")

class ProdutoController:
    def cadastrarProduto(self, nome, preco, categoria):
        lista = ProdutoDAO.ler()
        resultPro = [cada for cada in lista if cada.nome == nome]
        if len(resultPro) > 0:
            print("Produto já cadastrado")
            return
        cli1 = Produto(nome=nome, preco=preco, categoria=categoria)
        ProdutoDAO.salvar(cli1)
        print("Produto cadastrado com sucesso")
    
class FuncionarioController:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf ,email, endereco):
        lista = PessoaDAO.ler()
        resultCli = [cada for cada in lista if cada.cpf == cpf]
        if len(resultCli) > 0:
            print("Cliente já cadastrado")
            return
        resultTel = [cada for cada in lista if cada.telefone == telefone]
        if len(resultTel) > 0:
            print("Telefone já cadastrado")
            return
        resultCLT = [cada for cada in lista if cada.clt == clt]
        if len(resultCLT) > 0:
            print("CLT já cadastrado")
            return
        func1 = Funcionario(clt=clt, nome=nome, telefone=telefone, cpf=cpf, email=email, endereco=endereco)
        FuncionarioDAO.salvar(func1)
        print("Funcionario cadastrado com sucesso")
