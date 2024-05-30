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

notas = [1, 2, 3, 10, 20, 50, 100]
resultado = pode_ter_roubado_150(notas)
print("O suspeito pode ter roubado 150 fulampos?", resultado)
