import pandas as pd  # Importando a biblioteca pandas

# Lê o arquivo excel chamado "Vendas.xlsx" e amarzena os dados em um dataframe chamado 'excel'
excel = pd.read_excel("Vendas.xlsx")
# Criei uma variável chamada (mes) com um input de entrada para o usuário solicitar um mes
mes = input("Qual mês você quer Analisar? ")

# Verifica se o mês informado pelo usuário está presente nas colunas do DataFrame
if mes in excel.columns:
    # Ordena o DataFrame 'excel' pela coluna do mês especificado, em ordem decrescente
    analise = excel.sort_values(by=mes, ascending=False)
    # Vai imprimir o nome do melhor vendedor do mês
    print(f'O melhor vendedor do mês de {mes} foi o(a) {analise.iloc[0, 0]}')

    analise = excel.sort_values(by=mes, ascending=True)
    # Vai imprimir o nome do pior vendedor do mês
    print(f'O pior vendedor do mês de {mes} foi o(a) {analise.iloc[0, 0]}')

else:
    # Se a coluna com o nome do mês não for encontrada, exibe uma mensagem de erro
    print(f"coluna {mes} não encontrada. Verifique o nome da coluna.")
