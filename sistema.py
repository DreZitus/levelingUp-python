from abc import ABC, abstractmethod
import math

class atr_jogador(ABC): #classe base abstrata

    def __init__(self, nome, nivel, xp):  
        self.nome = nome
        self.nivel = nivel
        self.xp = xp

    
class sistema_Niveis(ABC):

    def __init__(self):
        pass


















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
