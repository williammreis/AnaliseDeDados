import pandas as pd

try:
    # Carregar o DataFrame
    excel = pd.read_excel("PastaTeste.xlsx")

    # Mostrar as colunas disponíveis
    print("Colunas disponíveis:", excel.columns)

    # Receber o input do usuário
    item = input("Qual item você quer Analisar? ")

    # Verificar se o input do usuário corresponde a uma coluna existente
    if item in excel.columns:
        analise = excel.sort_values(by=item)
        print(analise)
    else:
        print(f"Coluna '{item}' não encontrada. Verifique o nome da coluna.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


import pandas as pd

# Carregar o DataFrame sem cabeçalhos
excel = pd.read_excel("PastaTeste.xlsx", header=None)

# Mostrar as primeiras linhas para entender a estrutura
print(excel.head(10))

# Filtrar linhas que não contêm dados úteis
# Assumindo que a linha de cabeçalho está na linha com índices relevantes
# Ajuste o índice da linha de cabeçalho se necessário
header_index = 1  # Por exemplo, a linha 1 parece ter cabeçalhos reais
data = excel.iloc[header_index + 1:].reset_index(drop=True)

# Definir cabeçalhos manualmente com base na linha identificada
headers = excel.iloc[header_index].tolist()
data.columns = headers

# Remover quaisquer linhas extras ou cabeçalhos não necessários
data = data.dropna(how='all').reset_index(drop=True)

# Verificar o DataFrame reorganizado
print(data.head())
print("Colunas disponíveis:", data.columns)

# Receber o input do usuário
item = input("Qual item você quer Analisar? ")

# Verificar se o input do usuário corresponde a uma coluna existente
if item in data.columns:
    analise = data.sort_values(by=item)
    print(analise)
else:
    print(f"Coluna '{item}' não encontrada. Verifique o nome da coluna.")
