from abc import ABC, abstractmethod
import math

class atr_jogador(ABC): #classe base abstrata

    def __init__(self, nome, nivel, xp):  
        self.nome = nome
        self.nivel = nivel
        self.xp = xp


    def ganhar_XP(self, pontos):
        novo_xp = self.xp + pontos
        return self.verifica_Nivel(novo_xp)

    
    def verifica_Nivel(self, xp):
        if xp >= 100:
            self.nivel += 1
            self.xp = xp - 100
        else:
            self.xp = xp

            return f"{self.nome} está no nível {self.nivel} com {self.xp} XP."
