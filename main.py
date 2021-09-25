import math


def main():
    # Cabeçalho do programa
    print('='*100)
    print("Calculadora de Drops".center(100))
    print('='*100)

    # PEDINDO OS DADOS AO USUÁRIO
    denominador = int(input("Qual a probabilidade do item ser obtido? Uma em: "))
    inimigos_derrotados = int(input("Quantas vezes você derrotou o inimigo para tentar conseguir o item? "))

    # Cálculos
    chance = 1 / denominador  # Convertendo a probabilidade do item ser obtida (primeiro input)
    probabilidade = (1 - ((1 - chance) ** inimigos_derrotados)) * 100  # Cálculo para o segundo input

    # Função para calcular a quantidade de inimigos para se conseguir o item.
    def calcular_quantidade_inimigos(value):
        convertido = value / 100  # Transformando o valor em decimal/porcentagem.

        # Cálculo do quantidade de inimigos necessários, arredondado acima.
        resultado = math.ceil(math.log(1 - convertido) / math.log(1 - chance))

        return resultado  # A função retorna o resultado do cálculo

    # IMPRIMINDO O RESULTADO DO PROGRAMA #

    print('='*100)
    print(f'Após você eliminar {inimigos_derrotados} inimigo(s), a chance de você dropar o item é'
          f' de aproximadamente {probabilidade:.2f}%.')

    # === Imprimindo o resultado do programa por meio de um laço de repetição === #
    # Setando as variáveis/porcentagens desejadas para o programa imprimir o resultado.
    probabilidades_desejadas = [30, 40, 50, 60, 70, 80, 90, 95, 97]

    # A cada porcentagem/valor definida no list acima, o programa ira imprimir o resultado através do for.
    for each in probabilidades_desejadas:
        print(f'Para você ter {each}% de chances de conseguir o item você deverá matar '
              f'{calcular_quantidade_inimigos(each)} inimigos no jogo.')

    # Finalização do programa
    print('='*100)
    print('Fim do programa. :)')


if(__name__ == "__main__"):
    main()
