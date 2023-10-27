import os
import controller

def criarArquivos(*args):
    for cada in args:
        if not os.path.exists(cada):
            with open(cada, "w") as arq:
                arq.write("")

arquivos = (
    "categoria.txt",
    "estoque.txt",
    "funcionario.txt",
    "pessoa.txt",
    "venda.txt",
)

criarArquivos(arquivos)

if __name__ == '__main__':
    while True:
        local = int(input('''
                          1 - Categorias
                          2 - Estoque
                          3 - Fornecedor
                          4 - Cliente
                          5 - Funcionario
                          6 - Vendas
                          7 - Produtos mais vendidos
                          8 - Sair\n
                          '''))
        if local == 1:
            cat = controller.CategoriaController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Remover
                               3 - Atualizar
                               4 - Mostrar
                               5 - Sair\n
                               '''))
                if op == 1:
                    categoria = input("Digite categoria para cadastrar ")
                    cat.cadastrarCategoria(categoria=categoria)
                elif op == 2:
                    categoria = input("Digite categoria para remover ")
                    cat.removerCategoria(categoriaRemover=categoria)
                elif op == 3:
                    velho = input("Digite categoria que deseja atualizar")
                    novo = input("Digite a nova categoria")
                    cat.atualizarCategoria(velho=velho, novo=novo)
                elif op == 4:
                    cat.mostrarCategoria()
                elif op == 5:
                    break
        if local == 2:
            estoque = controller.EstoqueController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Remover
                               3 - Atualizar
                               4 - Mostrar
                               5 - Sair\n
                               '''))
                if op == 1:
                    nome = input("Digite nome do produto ")
                    preco = input("Digite preço ")
                    categoria = input("Digite categoria ")
                    quantidade = input("Digite quantidade ")
                    estoque.cadastrarEstoque(nome=nome, preco=preco, categoria=categoria, quantidade=quantidade)
                elif op == 2:
                    produto = input("Digite produto para remover ")
                    estoque.removerEstoque(produtoRemover=produto)
                elif op == 3:
                    nome = input("Digite nome do produto ")
                    categoria = input("Digite categoria ")
                    preco = input("Digite preço ")
                    quantidade = input("Digite quantidade ")
                    estoque.alterarEstoque(nome=nome, categoria=categoria, preco=preco, quantidade=quantidade)
                elif op == 4:
                    estoque.mostrarEstoque()
                elif op == 5:
                    break
        if local == 3:
            fornec = controller.FornecedorController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Sair\n
                               '''))
                if op == 1:
                    nome = input("Digite nome ")
                    cnpj = input("Digite cnpj ")
                    telefone = input("Digite telefone ")
                    categoria = input("Digite categoria ")
                    fornec.cadastrarFornecedor(nome=nome, cnpj=cnpj, telefone=telefone, categoria=categoria)
                if op == 2:
                    break
        if local == 4: 
            cliente = controller.PessoaController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Sair\n
                               '''))
                if op == 1:
                    nome = input("Digite nome ")
                    telefone = input("Digite telefone ")
                    cpf = input("Digite cpf ")
                    email = input("Digite email ")
                    endereco = input("Digite endereco ")
                    cliente.cadastrarCliente(nome=nome, telefone=telefone, cpf=cpf, email=email, endereco=endereco)
                if op == 2:
                    break
        if local == 5:
            func = controller.FuncionarioController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Sair\n
                               '''))
                if op == 1:
                    clt= input("Digite clt ")
                    nome = input("Digite nome ")
                    telefone = input("Digite telefone ")
                    cpf = input("Digite cpf ")
                    email = input("Digite email ")
                    endereco = input("Digite endereco ")
                    func.cadastrarFuncionario(clt=clt, nome=nome, telefone=telefone, cpf=cpf, email=email, endereco=endereco)
                if op == 2:
                    break
        if local == 6:
            venda = controller.VendaController()
            while True:
                op = int(input('''
                               1 - Cadastrar nova
                               2 - Mostrar relatorio
                               3 - Sair\n
                               '''))
                if op == 1:
                    produto = input("Digite produto ")
                    vendedor = input("Digite vendedor ")
                    comprador = input("Digite comprador ")
                    quantidade = int(input("Digite quantidade "))
                    venda.cadastrarVenda(produto=produto, vendedor=vendedor, comprador=comprador, quantidade=quantidade)
                elif op == 2:
                    venda.relatorioVenda()
                elif op == 3:
                    break
        if local == 7:
            venda = controller.VendaController()
            dataInicio = input("Digite data inicio no format (2023-10-23) ")
            dataFim = input("Digite data fim no format (2023-10-23) ")
            venda.mostrarVenda(dataInicio=dataInicio, dataFim=dataFim)
        if local == 8:
            break
        

