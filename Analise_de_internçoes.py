# Nome do arquivo: Exercício_Técnico_DELL.py
# Nome do autor: Amon Brollo
# Propósito do programa: fazer uma análise detalhada do crescente número de internações causado pela
# pandemia do convid-19

# nesta parte do código declaramos as variáveis que serão usadas mais tarde
número_total_de_pacientes_do_município = 0
quant_idade_m = 0
idade_m = 0
quant_idade_f = 0
idade_f = 0

# aqui abrimos o arquivo, que fechará automaticamente mais tarde, na variável "a"
with open ('gerint_solicitacoes_mod.csv') as a:
# como a primeira linha é informativa vamos usar "next()" para não ser confundido com os dados
    next(a)
# a variável a seguir recebe a informação do usuário para coletar os dados
    nome_do_município = input('Informe o nome do município residencial: ')

# fazemos uma loop para coletar os dados junto com ".strip()" e "split(";")" para remover qualquer 
# linha nova ou espaço em branco e separar os dados por coluna
    for linha in a:
        linha = linha.strip()
        linha = linha.split(";")

# aqui colocamos cada coluna de dado que usaremos em uma variável
        sexo = linha[5]
        idade = linha[6]
        municipio_residencia = linha[7]
    
# coletamos os dados de acordo com a resposta do usuário
# cada vez que o programa encontra um paciente em dada cidade, o número 1 é adicionado à variavel
#  "número_total_de_pacientes_do_município" proporcionando o número de pacientes
        if nome_do_município.lower() == municipio_residencia.lower():
            número_total_de_pacientes_do_município = número_total_de_pacientes_do_município + 1

# encontramos os pascientes masculinos e usamos a mesma lógica usada anteriormente para descobrir
# a quantidade de pacientes masculinos e adicionamos a idade de cada um para mais tarde calcular a 
# média
# transformamos a variável "idade" em tipo float para poder somar os valores
            if sexo == ("MASCULINO"):
                quant_idade_m = quant_idade_m + 1
                idade_m = idade_m + float(idade)

# e fazemos o mesmo com os pacientes femininos
            if sexo == ("FEMININO"):
                quant_idade_f = quant_idade_f + 1
                idade_f = idade_f + float(idade)
        
# calculamos a média de idade dos pacientes masculinos e femininos
    média_de_idade_m = (idade_m/quant_idade_m)
    média_de_idade_f = (idade_f/quant_idade_f)
# calculamos a média de idade de todos os pacientes adicionado os pacientes femininos aos masculinos
    média_de_idade = (idade_m + idade_f) / (quant_idade_m + quant_idade_f)

# apresentamos ao usuário o resultado da análise
# usamos ":.2f" para mostrar apenas 2 decimais depois do ponto
    print(f'Número total de pacientes do município: {número_total_de_pacientes_do_município}')
    print(f'Média de idade de pacientes masculinos: {média_de_idade_m:.2f}')
    print(f'Média de idade de pacientes femininos: {média_de_idade_f:.2f}')
    print(f'Média de idade de todos os pacientes: {média_de_idade:.2f}') 
