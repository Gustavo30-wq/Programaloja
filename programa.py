Nome = input("Digite seu nome: ")
XX1 = "Coxinha"
C2 = "XX1"
Salgadovalor = float(5)
conta = 0
desconto5 = 0.05
desconto10 = 0.10
desconto15 = 0.15

XX2 = "Kibi"
K2 = "XX2"

XX3 = "Empada"
E2 = "XX3"

XX4 = "Páo de Queijo"
P2 = "XX4"

XX5 = "Torresmo"
T2 = "XX5"

print("Olá", Nome, "seja bem-vindo(a) ao nosso cardápio!")
print("Produto, Código, Preço")
print(XX1, C2, Salgadovalor)
print(XX2, K2, Salgadovalor)
print(XX3, E2, Salgadovalor)
print(XX4, P2, Salgadovalor)
print(XX5, T2, Salgadovalor)

while True:
    escolha = input("Digite o código do produto que deseja comprar (e 'concluir' para se encaminhar ao pagamento): ")
    
    if escolha.lower() == 'concluir':
        print("o valor total da sua compra é R$", conta)
        break
    elif escolha == C2:
        print("Você escolheu", XX1, "no valor de R$", Salgadovalor)
        quantidade = int(input("Digite a quantidade: "))
        conta += quantidade * Salgadovalor
    elif escolha == K2:
        print("Você escolheu", XX2, "no valor de R$", Salgadovalor)
        quantidade = int(input("Digite a quantidade: "))
        conta += quantidade * Salgadovalor
    elif escolha == E2:
        print("Você escolheu", XX3, "no valor de R$", Salgadovalor)
        quantidade = int(input("Digite a quantidade: "))
        conta += quantidade * Salgadovalor
    elif escolha == P2:
        print("Você escolheu", XX4, "no valor de R$", Salgadovalor)
        quantidade = int(input("Digite a quantidade: "))
        conta += quantidade * Salgadovalor
    elif escolha == T2:
        print("Você escolheu", XX5, "no valor de R$", Salgadovalor)
        quantidade = int(input("Digite a quantidade: "))
        conta += quantidade * Salgadovalor
    else:
        print("Código inválido. Por favor, tente novamente.")

if conta <= 49:
        print("Você não tem direito a desconto.")
elif conta > 50 and conta <= 100:
        print("Você tem direito a 5% de desconto.")
elif conta > 100 and conta <= 200:
        print("Você tem direito a 10% de desconto.")
elif conta > 200:
        print("Você tem direito a 15% de desconto.")


print(f"o valor original da compra sem desconto é R$ {conta}")

print(f"O desconto aplicado foi de R$ {conta * (desconto5 if conta <= 100 else desconto10 if conta <= 200 else desconto15)}")

print(f"seu valor final da compra é R$ {conta}")

Escolha = input("Qual forma de pagamento você deseja utilizar? (Dinheiro, Cartão ou Pix): ")
if Escolha.lower() == "dinheiro":
    print("Você escolheu pagar em dinheiro. Obrigado pela compra!")
elif Escolha.lower() == "cartão":
    print("Você escolheu pagar com cartão. Obrigado pela compra!")
elif Escolha.lower() == "pix":
    print("Você escolheu pagar via PIX. Obrigado pela compra!")
else:
    print("Forma de pagamento inválida. Obrigado pela compra!")