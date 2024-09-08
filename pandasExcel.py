# Importando a biblioteca pandas
import pandas as pd

# Leitura dos arquivos excel
excel = pd.read_excel("")
excel2 = pd.read_excel("")
excel3 = pd.read_excel("")

# Juntando todos os arquivos
excel = pd.concat([excel, excel2, excel3])

# Exibindo as 5 primeiras linhas
excel.head()

# Exibindo as 5 últimas linhas
excel.tail()

# Verificando o tipo de dados de cada coluna
excel.dtypes()

# Alteradno o tipo de dado da coluna lojaID
excel["lojaID"] = excel["lojaID"].astype("object")


# --------------------------------------------------------------------------------------------------------------------------------
# TRATANDO VALORES FALTANTES

# Consultando linhas com valores faltantes
excel.isnull().sum()

# Substituindo os valores nulos pela média
excel["Vendas"].fillna(excel["Vendas"].mean(), inplace=True)

# Substituindo os valores nulos por zero
excel["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
excel.dropna(inplace=True)

# Apagando as linhas com os valores nulos com base apenas em 1 coluna
excel.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
excel.dropna(how="all", inplace=True)


# ---------------------------------------------------------------------------------------------------------------------
# CRIANDO COLUNAS NOVAS

# Criando a coluna de rceita
excel["Receita"] = excel["Vendas"].mul(excel["Qtde"])
excel.head()
excel["Receita/Vendas"] = excel["Receita"] / excel["Vendas"]
excel.head()

# Retornando a maior receita
excel["Receita"].max()

# Retornando a menor receita
excel["Receita"].min()

# nlargest
excel.nlargest(3, "Receita")

# nsmallest
excel.nsmallest(3, "Receita")

# Agrupamento por cidade
excel.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de dados
excel.sort_values("Receita", ascending=False).head(10)


# ---------------------------------------------------------------------------------------------------------------------------------
# TRABALHANDO COM DATAS

# Transformando a coluna de data em tipo inteiro
excel["Data"] = excel["Data"].astype("int69")

# Verificando o tipo de dado de cada coluna
excel.dtypes

# Transformando coluna de data em data
excel["Data"] = pd.to_datetime(excel["Data"])
excel.dtypes

# Agrupamento por ano
excel.groupby(excel["Data"].dt.year)["Receita"].sum()

# Criando uma nova coluna com o ano
excel["Ano_Venda"] = excel["Data"].dt.year
excel.sample(5)

# Extraindo o mês e o dia
excel["mes_venda"], excel["dia_venda"] = (
    excel["Data"].dt.month, excel["Data"].dt.day)

# Retornando a data mais antiga
excel["Data"].min()

# Calculando a diferença de dias
excel["diferenca_dias"] = excel["Data"] - excel["Data"].min()
excel.sample(5)

# Criando a coluna de trimestre
excel["trimestre_venda"] = excel["Data"].dt.quarter
excel.sample(5)

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = excel.loc[(excel["Data"].dt.year == 2019) & (
    excel["Data"].dt.month == 3)]
print(vendas_marco_19)


# -----------------------------------------------------------------------------------------------------------------------------------
# VISUALIZAÇÃO DE DADOS

excel["lojaID"].value_counts(ascending=False)

# Gráfico de barras
excel["lojaID"].value_counts(ascending=False).plot.bar()

# Gráfico de barras horizontais
excel["lojaID"].value_counts().plot.barh()

# Gráfico de barras horizontais
excel["lojaID"].value_counts(ascending=False).plot.barh()

# Gráfico de pizza
excel.groupby(excel["Data"].dt.year)["Receita"].sum().plot.pie()

# Total vendas por cidade
excel["Cidade"].value_counts()
