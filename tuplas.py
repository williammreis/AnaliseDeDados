# As tuplas usam parênteses como sintaxe
tp = ("Banana", "Maça", 10, 50)
print(tp[0])

# Para criar um dicionário utilizamos as {}
# Dicionário trabalham com o conceito chave e valor
dc = {"Maça": 20, "Banana": 10, "Laranja": 15, "Uva": 5}
print(dc)
print(dc["Banana"])

dc["Banana"] = 25
print(dc)

# Retornando todas as chaves e valores do dicionário
print(dc.keys())
print(dc.values())

# Verificando se já existe uma chave no dicionário e caso não exista inserir
dc.setdefault("Limão", 22)
print(dc)
