from abc import ABC, abstractmethod
import math

class atr_jogador(ABC): #classe base abstrata

    def __init__(self, nome, nivel, xp):  
        self.nome = nome
        self.nivel = nivel
        self.xp = xp
    
    def quest_completa(self, xp_ganha):
        self.xp += xp_ganha
        self.verifica_nivel()


dados_jogador = atr_jogador('André', 0, 0)

print(dados_jogador.nome, dados_jogador.nivel, dados_jogador.xp)


















jogador = {
    'nome': 'André',
    'nivel': 0,
    'xp': 0
}


nivel = 0
xp = 1
questcomplete = False

if questcomplete == True:
    xp = xp * 2
