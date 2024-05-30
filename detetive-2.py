def pode_ter_roubado_150(notas):
    alvo = 150
    n = len(notas)
    
    dp = [False] * (alvo + 1)
    dp[0] = True 
    
    for nota in notas:
        for i in range(alvo, nota - 1, -1):
            if dp[i - nota]:
                dp[i] = True
                
    return dp[alvo]

def ler_notas_usuario():
    entrada = input("Digite as notas, separadas por espaços ou vírgulas: ")
    notas_str = entrada.replace(',', ' ').split()
    notas = [int(nota) for nota in notas_str]
    return notas

notas = ler_notas_usuario()
resultado = pode_ter_roubado_150(notas)
print("O suspeito pode ter roubado 150 fulampos?", resultado)
