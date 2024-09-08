import matplotlib.pyplot as plt
import pandas as pd

excel = pd.read_excel("Vendas.xlsx")
mes = input("Qual mês você quer Analisar? ")


if mes in excel.columns:
    analise = excel.sort_values(by=mes, ascending=False).head(1)
    print(f"o melhor vendedor do mês de {mes} foi o(a) {analise.iloc[0, 0]}")
    print(f"{analise}")

    plt.figure(figsize=(10, 6))
    excel.plot(x='Unnamed: 0', y=mes, kind='barh',
               title=f"Valores do mês de {mes}", color="red")
    plt.xlabel("Vendedores")
    plt.xlabel("Valores")
    plt.show()
else:
    print(f"coluna {mes} não encontrada. Por favor verifique o nome do mês.")
