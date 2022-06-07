import math
import numpy as np
import matplotlib.pyplot as plt

# Discretização
delta_phi = 2
delta_r = 0.005

# Highlight
pos = 'top_a'
cor = 'g'

def plota_malha_aux(delta_phi, delta_r, pos, cor):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Contorno do material A
    ax.plot([0]*50, np.linspace(0.03, 0.11), color='k')
    ax.plot([np.deg2rad(40)]*50, np.linspace(0.03, 0.11), color='k')
    ax.plot(np.linspace(0, np.deg2rad(40)), [0.03]*50, color='k')
    ax.plot(np.linspace(0, np.deg2rad(40)), [0.11]*50, color='k',linewidth=1.3)
    
    # Contorno do material B
    ax.plot([0]*50, np.linspace(0.05, 0.08), color='k')
    ax.plot([np.deg2rad(18)]*50, np.linspace(0.05, 0.08), color='k')
    ax.plot(np.linspace(0, np.deg2rad(18)), [0.05]*50, color='k')
    ax.plot(np.linspace(0, np.deg2rad(18)), [0.08]*50, color='k',linewidth=1.3)

    # Highlight A
    if pos == 'top_a':
        ax.plot([np.deg2rad(40)]*50, np.linspace(0.03+delta_r, 0.11-delta_r), color=cor, linewidth=4)
        ax.plot(np.deg2rad(40), 0.03+delta_r, color=cor, markersize=10, marker=".")
        ax.plot(np.deg2rad(40), 0.11-delta_r, color=cor, markersize=10, marker=".")
    if pos == 'bottom_a':
        ax.plot([0]*50, np.linspace(0.03+delta_r, 0.05-delta_r), color=cor, linewidth=4)
        ax.plot([0]*50, np.linspace(0.08+delta_r, 0.11-delta_r), color=cor, linewidth=4)
        ax.plot(0, 0.03+delta_r, color=cor, markersize=10, marker=".")
        ax.plot(0, 0.05-delta_r, color=cor, markersize=10, marker=".")
        ax.plot(0, 0.08+delta_r, color=cor, markersize=10, marker=".")
        ax.plot(0, 0.11-delta_r, color=cor, markersize=10, marker=".")
    if pos == 'left_a':
        ax.plot(np.linspace(0, np.deg2rad(40)), [0.03]*50, color=cor, linewidth=4)
        ax.plot(np.deg2rad(0), 0.03, color=cor, markersize=10, marker=".")
        ax.plot(np.deg2rad(40), 0.03, color=cor, markersize=10, marker=".")
    if pos == 'right_a':
        ax.plot(np.linspace(0, np.deg2rad(40)), [0.11]*50, color=cor, linewidth=4)
        ax.plot(np.deg2rad(0), 0.11, color=cor, markersize=10, marker=".")
        ax.plot(np.deg2rad(40), 0.11, color=cor, markersize=10, marker=".")

    # Highlight B
    if pos == 'top_b':
        ax.plot([np.deg2rad(18)]*50, np.linspace(0.05+delta_r, 0.08-delta_r), color=cor, linewidth=2)
        ax.plot(np.deg2rad(18), 0.05+delta_r, color=cor, markersize=5, marker=".")
        ax.plot(np.deg2rad(18), 0.08-delta_r, color=cor, markersize=5, marker=".")
    if pos == 'bottom_b':
        ax.plot([np.deg2rad(0)]*50, np.linspace(0.05+delta_r, 0.08-delta_r), color=cor, linewidth=4)
        ax.plot(np.deg2rad(0), 0.05+delta_r, color=cor, markersize=10, marker=".")
        ax.plot(np.deg2rad(0), 0.08-delta_r, color=cor, markersize=10, marker=".")
    if pos == 'left_b':
        ax.plot(np.linspace(np.deg2rad(0+delta_phi), np.deg2rad(18-delta_phi)), [0.05]*50, color=cor, linewidth=2)
        ax.plot(np.deg2rad(0+delta_phi), 0.05, color=cor, markersize=5, marker=".")
        ax.plot(np.deg2rad(18-delta_phi), 0.05, color=cor, markersize=5, marker=".")
    if pos == 'right_b':
        ax.plot(np.linspace(np.deg2rad(0+delta_phi), np.deg2rad(18-delta_phi)), [0.08]*50, color=cor, linewidth=2)
        ax.plot(np.deg2rad(0+delta_phi), 0.08, color=cor, markersize=5, marker=".")
        ax.plot(np.deg2rad(18-delta_phi), 0.08, color=cor, markersize=5, marker=".")
    if pos == 'corner_b':
        ax.plot(np.deg2rad(0), 0.05, color=cor, markersize=10, marker=".")
        ax.plot(np.deg2rad(0), 0.08, color=cor, markersize=10, marker=".")


    # Linhas da malha
    ax.set_rticks(np.arange(0.03, 0.12, delta_r)) 
    ax.set_thetagrids(np.arange(0, 40, delta_phi))

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
    
    ax.grid(True)

    #ax.set_title("A line plot on a polar axis", va='bottom')
    plt.show()

plota_malha_aux(delta_phi, delta_r, pos, cor)