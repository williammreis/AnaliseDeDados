# Criando uma lista chamada animais
animais = [1, 2, 3]
print(animais)


animais = ["cachorro", "gato", 12345, 6.5]
print(animais)

# Imprimindo o primeiro elemento da lista
print(animais[0])

# Imprimindo o 4 elemento da lista
print(animais[3])

# Substituindo o primeiro elemento da lista
animais[0] = "papagaio"
print(animais)

# Removendo gato da lista
animais.remove("gato")
print(animais)

# Ver o tamanho da lista
print(len(animais))

animais.append(["Leão", "cachorro"])
print(animais)

animais.extend(["cobra", 6])
print(animais)

print(animais.count(6))
