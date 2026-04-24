import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tentativas = 5

    print("🎲 Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 10.")
    print(f"Você tem {max_tentativas} tentativas.\n")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.")
            continue

        tentativas += 1

        # Comentários narrativos
        if tentativas == 1:
            print("📢 Primeira tentativa! Vamos ver se você tem sorte logo de cara...")
        elif tentativas == max_tentativas - 1:
            print("😬 Penúltima chance! Concentre-se!")
        elif tentativas == max_tentativas:
            print("🔥 Última tentativa! É tudo ou nada!")

        # Verifica o palpite
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            print("👏 Que desempenho incrível!")
            break
        elif palpite < numero_secreto:
            print("🔼 Quase lá! Tente um número maior.")
        else:
            print("🔽 Quase lá! Tente um número menor.")

        if tentativas < max_tentativas:
            print(f"Você ainda tem {max_tentativas - tentativas} tentativa(s).\n")

    else:
        print(f"😢 Infelizmente, você não acertou. O número era {numero_secreto}.")
        print("🎤 Comentário final: foi uma boa disputa, mas o número te venceu desta vez!")
        print("Fim do jogo!")

# Executa o jogo
if __name__ == "__main__":
    jogo_adivinhacao()
