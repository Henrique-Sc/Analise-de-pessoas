# Imports
from time import sleep as s

# Cores no terminal
r = '\033[m'
IR = '\033[38;5;9m'
IB = '\033[38;5;12m'

# Declarando as variáveis
pessoas = []
dados = {}
c = 0

# Laço para a inserção dos dados
while True:
    # Inserção dos dados
    dados['nome'] = str(input('Seu nome: ')).strip().title()
    dados['idade'] = int(input('Sua idade: ').strip())
    
    while True:
        dados['sexo'] = str(input(f'Sexo: [{IR}M{r}arculino / {IR}F{r}eminino / {IR}O{r}utros] ')).strip().upper()[0]
        # Tratamento de erro
        if dados['sexo'] in 'MFO':
            break
        print(f'\n{IR}Valor incorreto!{r} Digite novamente.')

    # Inserindo os dados em um dicionário, colocando em uma lista e limpando o dicionário
    pessoas.append(dados.copy())
    dados.clear
    
    c += 1

    esc = str(input(f'\nDeseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    
    # Tratamento de erro
    if esc not in 'NS': print()
    while esc not in 'NS':
        esc = str(input(f'{IR}Valor incorreto!{r} Deseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
        
    print()
    
    if esc == 'N':
        break

# Declarando as variáveis
tot_pessoas = len(pessoas)
tot_idade = 0
tot_m = []

# Laços para análise dos dados
for p in pessoas:
    tot_idade += p['idade']
    if p['sexo'] == 'F':
        tot_m.append(p['nome'])
if tot_m == []:
    tot_m = 'Nenhuma mulher foi cadastrada'
media_idade = tot_idade / tot_pessoas

# linha para design
s(0.5), print('==' * 20, '\n'), s(0.5)

# Exibição dos dados
print(f'- Número de pessoas cadastradas: {tot_pessoas}')
s(0.5)
print(f'- Média de idade do grupo: {media_idade:.1f}')
s(0.5)
print(f'- Nomes das mulheres cadastradas: {tot_m}')
s(0.5)
print(f'- Pessoas com idade maior que a média do grupo: ')
s(0.5)
c = 0
for p in (pessoas):
    if p['idade'] > media_idade:
        print('   -> ', end='')
        for k, v in p.items():
            print(f'{k.title()}: {v}; ', end='')
        print()
        c += 1
if c == 0:
    print('   -- Nenhuma pessoa com a idade maior que a média')

# Linha para design
print()
print('==' * 20), s(0.5)
