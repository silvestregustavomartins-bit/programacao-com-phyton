#aula 20

personagens = [
    {"nome": "Arthur Morgan", "idade": 23},
    {"nome": "Finn", "idade": 17},
]
# print(personagens[0]["Nome"])
# print(personagens[1]["Nome"])

for personagem in personagens:
    print("nome:", personagem["nome"])
    print("idade:", personagem["idade"])