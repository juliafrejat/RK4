import math
import numpy as np
from rk4 import rk4
from plot_graph import plot

# Parâmetros gerais
lb = 0.5
rb = 20
c = 0.002
e = lambda t: np.cos(t*600)/la

# Montagem do sistema de equações
f = lambda x, y : np.array([(e(x)-(y[2]/c)-ra*(y[0]-y[1]))/la, 
                            (-rb*y[1]+(y[2]/c)+ra*(y[0]-y[1]))/lb,
                            y[0]-y[1]])
x0 = 0
y0 = np.array([0, 0, 0])
xn = 0.03

def solve_q(H, titles):
    """
    Solução as questões da Parte 1: resolução e plotagem de um sistema de EDOs usando Runge-Kutta de 4ª ordem
    H : array      - vetor com valores de passo
    titles: array  - vetor com títulos do gráficos
    Faz a plotagem de um gráfico com as variáveis das equações (i1, 12, q, i1', 12') para cada valor de passo
    definido.
    """

    for i in range(len(H)):
        # Passo da iteração
        h = H[i]

        # Chamada da função que executa o método RK4
        Y, dY, t = rk4(f,x0,y0,xn,h)

        # Transposição dos arrays de variáveis
        # Resulta em arrays de vetores com valores cada variável ao longo das iterações
        Y = np.transpose(Y)
        print(Y)
        dY = np.transpose(dY)

        # Vetor com todas as variáveis na ordem: i1, i2, q, i1', i2'
        vars = np.vstack([Y, dY[0], dY[1]])

        # Ajuste de escala para plotagem [p, r, z, q, s]
        scales = np.array([1])

        # Vetor com legendas para cada variável plotada
        labels = ["i1", "i2", "q", "i1'", "i2'"]

        # Cálculo da diferença de ordem de grandeza entre i1 e as outras variáveis
        for j in range(1,len(vars)):

            # Uso dos valores máximos
            value = max(vars[0], key=abs)/max(vars[j], key=abs)

            if value < 0:
                order = math.floor(math.log(-value, 10))
                scales = np.append(scales,10**order)
            else:
                order = math.floor(math.log(value, 10))
                scales = np.append(scales,10**order)

            # Atualiza vetor de legendas com escalas
            if order:
                labels[j] += " x $10^{" + str(order) + "}$"
        # Multiplicação dos vetores pelas escalas
        vars *= scales[:, None]

        # Chamada da função que plota o gráfico das variáveis e derivadas
        plot(t, vars, labels, titles[i])


### LETRA A ###

# Parâmetros 
la = 0.01
ra = 200

# Escolha dos valores de h 
H = [0.01, 0.0001, 0.000001]

# Título para plotagem do gráfico
titles = ["Obtenção dos parâmetros $i_1$, $i_2$, $q$, $i_1'$, $i_2'$ com passo h = "]*3
titles[0] += str(H[0])
titles[1] += str(H[1])
titles[2] += str(H[2])

# Chamada da função que resolve a questão
solve_q(H, titles)


### LETRA B ###

# Atualiza parâmetros
la = 0.1
ra = 2000

# Atualiza escolha dos valores de h 
H = [0.0001]

# Título para plotagem do gráfico
titles = ["Obtenção dos parâmetros $i_1$, $i_2$, $q$, $i_1'$, $i_2'$ com passo h = "]
titles[0] += str(H[0])

# Chamada da função que resolve a questão
solve_q(H, titles)