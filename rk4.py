import numpy as np

def rk4(f, x0, y0, xn, h):
    """
    Aproxima a solução de um sistema de EDOs usando Runge-Kutta de 4ª ordem
    f  : function - sistema de EDOs
    x0 : float    - condição inicial (variável independente)
    y0 : array    - vetor condição inicial (variáveis dependentes)
    xn : float    - ponto final 
    h  : int      - tamanho do passo
    Retorna um vetor com os valores das iterações das variáveis independentes (intermediárias e valor final),
    um vetor com os valores das iterações das derivadas das variáveis independentes
    e um vetor com os valores de x de cada iteração.
    """
    # Primeiro passo feito com y0
    y_i = y0

    # Inicialização de x em x0
    x = x0

    # Vetor para armazenar variáveis dependentes nas iterações intermediárias
    Y = np.array([y0])

    # Vetor com valores de x nas iterações intermediárias
    t = [x]

    # Cálculo do número de iterações
    n = (xn-x0)/h

    # Iteração com n passos
    for i in range(int(n)):
        # Cálculo das constantes ks do método RK4
        k1 = f(x, y_i)
        k2 = f(x + h/2, y_i + k1*h/2)
        k3 = f(x + h/2, y_i + k2*h/2)
        k4 = f(x + h, y_i + k3*h)

        # Aproximação usando as inclinações ks
        y_ii = y_i + h/6*(k1 + 2*k2 + 2*k3 + k4)

        # Atualização do vetor para próxima iteração
        y_i = y_ii

        # Armazenamento do resultado da iteração i
        Y = np.vstack([Y, y_ii])

        if not i:
            # Vetor para armazenar derivadas das variáveis nas iterações intermediárias
            dY = np.array([k1])
        else:
            # Armazenamento do resultado da iteração i
            dY = np.vstack([dY, k1])

        # Atualização de x
        x += h

        # Armazenamento do valor de x
        t.append(x)

    # Cálculo das derivadas em xn
    k1 = f(x, y_i)
    # Armazenamento do resultado
    dY = np.vstack([dY, k1])

    return Y, dY, t
