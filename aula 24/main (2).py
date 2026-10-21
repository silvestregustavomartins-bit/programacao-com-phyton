item1 = input("coloque o item: ")
item2 = input("coloque outro item aqui: ")



personagem = {
    "nome": "Link",
    "classe": "guerreiro",
    "nivel": 1,
    "inventario": ["Ocarina", "espada", "escudo", "arco e flecha"]
}

personagem["inventario"].append(item1)
personagem["inventario"].append(item2)

for x in personagem["inventario"]:
    print(x)