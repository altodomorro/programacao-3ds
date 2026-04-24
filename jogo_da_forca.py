# Exemplo de game loop no Python para jogo da forca
palavra_secreta = "girafa"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
tentativas = 6

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        index = 0
        for letra in palavra_secreta:
            if palpite == letra:
                letras_acertadas[index] = letra
            index += 1
    else:
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")
    
    print(" ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu. A palavra era:", palavra_secreta)

""" Este código ilustra um game loop básico para o jogo da forca, 
onde o jogador tem um número limitado de tentativas para adivinhar
a palavra secreta. O loop continua até que o jogador acerte a 
palavra ou esgote suas tentativas. """

# Declara as variáveis numéricas
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Configura a lógica das operações
soma = num1 + num2
subtracao = num1 - num2

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")

# Solicita ao usuário que digite um número inteiro
numero = int(input("__________________________: "))

# Verifica se o número é par
if numero % 2 == 0:
    # Se for par, imprime a mensagem
    print(f"{numero} é par.")
else:
    # Se for ímpar, imprime a mensagem
    print(f"{numero} é ______________.")

# Solicita temperatura em graus Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Calcula a temperatura em graus Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Solicita um número ao usuário
numero = float(input("__________________________"))

# Verifica se o número é positivo
if numero > 0:
    # Se for positivo, imprime a mensagem
    print("O número é _________________.")
# Verifica se o número é negativo
elif numero < 0:
    # Se for negativo, imprime a mensagem
    print("_______________________________________")
# Se não for positivo nem negativo, é zero
else:
    # Imprime a mensagem para zero
    print("__________________________________")

# Solicita o peso do usuário em kg
peso = float(input("Digite o peso em kg: "))

# Solicita a altura do usuário em metros
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Classifica o IMC e exibe a mensagem
___ imc < 18.5:
    print("Abaixo do peso.")
_______ imc < 25:
    print("Peso normal.")
_______ imc < 30:
    print("Sobrepeso.")
_____:
    print("Obesidade.")

# Solicita letra ao usuário e converte em minúscula
______ = input("Digite uma letra: ").lower()

# Verifica se a letra é uma vogal
if letra in "aeiou":
    # Se for vogal, imprime "Vogal."
    print("______")
else:
    # Se não for vogal, imprime "Consoante."
    print("___________")

# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))

# Solicita o código de desconto
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Define os descontos correspond
