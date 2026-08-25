import re
codigo = input("digite um codigo: ")
if re.fullmatch(r"\d{4}", codigo):
    print("Código valido")
else:
    print("Código invalido")