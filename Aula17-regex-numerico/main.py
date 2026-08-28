import re
codigo = input("digite um codigo: ")

while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("digite novamente (contendo 5 caracteres: letras e numeros): ")

