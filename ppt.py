import random

def jogar():
    opcoes = ("pedra", "papel", "tesoura")
    vitorias = 0
    derrotas = 0
    empates = 0

    print("\nBem vindo ao jogo de Pedra, Papel ou Tesoura!")

    while True:
        escolhaJogador = input("Escolha (Pedra, Papel, Tesoura ou Sair): ").lower().strip()
        if escolhaJogador == "sair":
            print("\nObrigado por jogar! Até a próxima!")
            break
    
        if escolhaJogador not in opcoes:
            print("Escolha inválida! Tente novamente.\n")
            continue

        escolhaMaquina = random.choice(opcoes)
        print(f"\nA máquina escolheu: {escolhaMaquina}\n")

        if escolhaJogador == escolhaMaquina:
            print("Empate!")
            empates += 1
        elif (
            (escolhaJogador == "pedra" and escolhaMaquina == "tesoura") or
            (escolhaJogador == "papel" and escolhaMaquina == "pedra") or(escolhaJogador == "tesoura" and escolhaMaquina == "papel")
        ):
            print("Parábens! Você venceu!\n")
            vitorias += 1
        else:
            print("Você perdeu!\n")
            derrotas += 1

        print(f"Placar atual:\nVitórias: {vitorias}\nDerrotas: {derrotas}\nEmpates: {empates}\n")

if __name__ == "__main__":
    jogar()