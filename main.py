print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = 0
valor_total = 0

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")

# Solicita o tamanho em metros quadrados da área a ser pintada
area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calcula a quantidade de latas de tinta necessárias
litros_tinta = area_pintada / 3  # 1 litro de tinta cobre 3 metros quadrados
latas_tinta = int(litros_tinta / 18) + (1 if litros_tinta % 18 != 0 else 0)  # Cada lata contém 18 litros de tinta

# Calcula o preço total das latas de tinta
preco_total = latas_tinta * 80  # Cada lata de tinta custa R$ 80,00

# Exibe a quantidade de latas de tinta a serem compradas e o preço total
print(f"Serão necessárias {latas_tinta} latas totalizando R$ {preco_total}")

