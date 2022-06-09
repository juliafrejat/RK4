import math
import numpy as np
import matplotlib.pyplot as plt

# Discretização
# delta_phi = 10
# delta_r = 0.01
delta_phi = 2
delta_r = 0.005

def resolve_malha(delta_phi, delta_r, tx_sobrerelaxacao, tolerancia):

    # Variáveis que definem o tamanho da matriz que representa a malha (m = no. linhas, n = no. colunas)
    m = int(40/delta_phi) + 1
    n = int(0.08/delta_r) + 1

    # Matriz que representa a malha inicializada com zeros 
    malha = np.zeros((m, n))

    # V conhecido nas bordas esquerda e direita do material A (particularidade azul)
    malha[:, 0] = 100
    malha[:, n-1] = 0

    # Variável que mede a diferença dos valores de V para checar a tolerância de convergência
    maior_diferenca = 0

    while ((maior_diferenca > tolerancia) or maior_diferenca == 0):
        
        maior_diferenca = 0 

        # Método de Liebmann
        for i in list(range(0, m)):       
            for j in list(range(1, n-1)): # A iteração das colunas não precisa passar na primeira e na última (condições de contorno)  
                
                # Potencial na iteração anterior
                V_velho = malha[i, j]

                # Valor do raio na iteração j
                r = 0.03 + j*delta_r

                # Particularidades para método
                if ((1 <= i <= m-1) and (1 <= j <= n-1)):     # Particularidade cor: pontos no centro da matriz -> esse é o caso genérico
                    V_novo = (malha[i,j+1] + malha[i, j-1])/2 # Coloquei qualquer coisa: isso é uma média na linha
                    
                elif (i == 0):                                # Particularidade cor: pontos na primeira linha
                    V_novo = malha[i+1, j]*r                  # Coloquei qualquer coisa: esse tem um fator de posição

                elif ((i == m)):
                    V_novo = malha[i-1, j]                    # Coloquei qualquer coisa
                
                # Sobre-relaxação
                malha[i, j] = tx_sobrerelaxacao*V_novo + (1-tx_sobrerelaxacao)*V_velho

                # Checagem da convergência
                if abs(malha[i, j] - V_velho) > maior_diferenca:
                     maior_diferenca = abs(malha[i, j] - V_velho)

    return malha

def plota_malha(delta_phi, delta_r, malha, linha_de_grade=True):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Contorno do material A
    ax.plot([0]*50, np.linspace(0.03, 0.11), color='k')
    ax.plot([np.deg2rad(40)]*50, np.linspace(0.03, 0.11), color='k')
    ax.plot(np.linspace(0, np.deg2rad(40)), [0.03]*50, color='k')
    ax.plot(np.linspace(0, np.deg2rad(40)), [0.11]*50, color='k',linewidth=1.3)
    
    # Contorno do material B
    ax.plot([0]*50, np.linspace(0.05, 0.08), color='b')
    ax.plot([np.deg2rad(18)]*50, np.linspace(0.05, 0.08), color='b')
    ax.plot(np.linspace(0, np.deg2rad(18)), [0.05]*50, color='b')
    ax.plot(np.linspace(0, np.deg2rad(18)), [0.08]*50, color='b',linewidth=1.3)

    # Parâmetros da grade
    r = np.arange(0.03, 0.12, delta_r)
    theta = np.arange(0, 40, delta_phi)

    # Linhas de grade
    if linha_de_grade:
        ax.set_rticks(r) 
        ax.set_thetagrids(theta)
        ax.grid(True)
    if (not linha_de_grade):
        ax.set_rticks([]) 
        ax.set_thetagrids([])

    # Plotagem dos valores da malha
    r = np.linspace(0.03, 0.11, int(0.08/delta_r) + 1)
    p = np.linspace(np.deg2rad(40), 0, int(40/delta_phi) + 1)
    R, P = np.meshgrid(r, p)

    cp = ax.contourf(P, R, malha)
    fig.colorbar(cp)

    # Limites do gráfico
    ax.set_thetamin(0)
    ax.set_thetamax(40)
    ax.set_rmax(0.11)

    # Offset
    ax.set_rmin(0.03)
    ax.set_rorigin(-0.03)

    # Remover labels 
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    #ax.set_title("A line plot on a polar axis", va='bottom')
    plt.show()

malha = resolve_malha(delta_phi, delta_r, 1.5, 0.01)
print(malha)
plota_malha(delta_phi, delta_r, malha, linha_de_grade=True)