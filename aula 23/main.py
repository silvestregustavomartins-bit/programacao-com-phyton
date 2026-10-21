personagens = []

def criar_personagem():
    nome = input("digite o nome do seu personagem: ")
    classe = input("digite a classe do seu personagem: ")
    nivel = int(input("digite o nivel do seu personagem: "))
    
    personagem = {
        "nome": nome, 
        "classe": classe, 
        "nivel": nivel
    }
    personagens.append(personagem)
    
    
quantidade = int(input("quantos personagens voce quer criar")) 
for i in range(quantidade):
    print(f"criando personagem {1 + 1}")
    criar_personagem()
    
print("----Lista final de personagem----")
for personagem in personagens:
    print("PERSONAGEM CRIADO")
    print("Nome: ", personagem["nome"])
    print("Classe: ", personagem["classe"])
    print("Nível: ", personagem["nivel"])
    print()
    
    
    