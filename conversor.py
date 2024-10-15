# Funcao que le o arquivo texto
def leiaEntrada():
    with open("entrada.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Numero total de linhas no arquivo
    nbinarios = len(linhas)
    
    # Inicializa as listas para armazenar o numero binario e o expoente
    binarios = []
    expoentes = []
    
    # Processa cada linha do arquivo
    for linha in linhas:
        # Remove espacos e quebras de linha desnecessarias
        linha = linha.strip()
        
        # Divide a linha no formato 'numero_binario x 2^expoente'
        corte = linha.split(" x 2^")
        binario = corte[0] 

        # Se nao tiver nenhum expoente, considera 0
        if(len(corte) > 1):
            expoente = int(corte[1])  
        else:
            expoente = 0

        # Adiciona o binario e o expoente às listas
        binarios.append(binario)
        expoentes.append(expoente)
    
    arquivo.close()
    
    return nbinarios, binarios, expoentes

# Funcao que arruma a posição real do binario sem o expoente
def arruma(nbinarios, binarios, expoentes):
    for i in range(nbinarios):
        binario = binarios[i]
        expoente = expoentes[i]
        
        # Remove o ponto decimal para facilitar a manipulacao
        binario = binario.replace('.', '')

        # Achar a posicao original da vírgula
        pos_virgula = binarios[i].find('.')  # Posicao da vírgula original
        
        # Mover a vírgula para a direita (expoente positivo) ou esquerda (expoente negativo)
        if expoente > 0:
            nova_posicao = pos_virgula + expoente

            # Se o expoente é maior que o numero de dígitos à direita da vírgula, adicionar zeros
            if nova_posicao >= len(binario):
                diferenca = nova_posicao - len(binario)-1
                binario = binario + '0' * (diferenca + 1)  
            else:
                # Adicionar a vírgula na nova posicao
                binario = binario[:nova_posicao] + '.' + binario[nova_posicao:]

        else:
            # Expoente negativo: mover a vírgula para a esquerda, adicionando zeros à esquerda se necessario
            nova_posicao = pos_virgula + expoente
            if nova_posicao <= 0:
                # Se a nova posicao for antes do início do numero, adicionar zeros à esquerda
                binario = '0.' + '0' * abs(nova_posicao) + binario
            else:
                binario = binario[:nova_posicao] + '.' + binario[nova_posicao:]

        # Atualiza o binario ajustado
        binarios[i] = binario.strip('.')

    return binarios

    
# Funcao que converte binario para decimal    
def converte(nbinarios, binarios):
    decimais = []
    for i in range(nbinarios):
        binario = binarios[i]
        decimal = 0

        # Achar a posicao da vírgula
        pos_virgula = binario.find('.')  # Posicao da vírgula
        
        # Se nao houver vírgula, trata-se de um numero inteiro binario
        if pos_virgula == -1:
            pos_virgula = len(binario) 

        # Remover o ponto da string para facilitar o calculo
        binario_sem_ponto = binario.replace('.', '')

        # Converter a parte inteira (à esquerda da vírgula)
        for j in range(pos_virgula):
            bit = int(binario_sem_ponto[j])
            decimal += bit * (2 ** (pos_virgula - j - 1)) 

        # Converter a parte fracionaria (à direita da vírgula)
        for j in range(pos_virgula, len(binario_sem_ponto)):
            bit = int(binario_sem_ponto[j])
            decimal += bit * (2 ** -(j - pos_virgula + 1))

        decimais.append(decimal)
    
    return decimais


# Chamadas das funcoes
nbinarios, binarios, expoentes = leiaEntrada()
binarios = arruma(nbinarios, binarios, expoentes)
decimais = converte(nbinarios, binarios)

#Imprime o resultado
for i in range(nbinarios):
    print(f"Binario: {binarios[i]}, Decimal: {decimais[i]}")