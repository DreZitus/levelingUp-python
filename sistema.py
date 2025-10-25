jogador = {
    'nome': 'André',
    'nivel': 0,
    'xp': 0
}


nivel = 0
xp = 1
quest = False

if quest == True:
    xp = xp * 2

jogador['xp'] += xp 

print(f"XP Atual: {jogador['xp']}")s