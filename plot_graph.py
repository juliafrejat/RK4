import matplotlib.pyplot as plt
import numpy as np 

def plot(x, Y, labels, title):
    """
    Plota curvas com 
    x : array        - valores para o eixo x 
    Y : array        - arrays contendo valores para o eixo y
    labels : array   - lista de legendas para curvas
    title : string   - título do gráfico
    Retorna um vetor com os valores das iterações (intermediárias e valor final)
    """

    for i in range(len(Y)):
        # Plotagem dos dados de cada variável
        plt.plot(x, Y[i], label = labels[i])
    plt.ylabel('Variáveis')
    plt.xlabel('Tempo [s]')
    plt.title(title)
    plt.legend(labels)
    plt.show()