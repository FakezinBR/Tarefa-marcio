estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}
#Foi adicionada uma biblioteca
total = 0
print("vendas:\n") #mostra a palavra vendas
while True:
    produto = input("nome do produto(fim para sair):")
    # mostra a a pergunta do nome do produto e da a escolha de sair
    if produto == "fim":
        break
    #caso a pessoa digite fim o programa para
    if produto in estoque:
    #se o produto está no estoque
        quantidade = int(input("quantidade:"))
        #A variavel quantidade recebe a quanidade de produtos
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            #caso a quantidade pedida seja menor ou igual a quantidade no estoque é calculado o custo do produto
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f}) = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
            #é imprimido o resultado  dos calculos

        else:
            print("Quantidade solicitada não disponivel")
        #se não tem a quantidade no estoque printa que nao possui produtos

    else:
        print("Nome de produto inválido")
        print(f" Custo total: {total:21.2f}\n")
        print("Estoque:\n")
        #caso o nome do produto seja digitado errado

    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
        #printa quantidade a descrição e o preço dos produtos
