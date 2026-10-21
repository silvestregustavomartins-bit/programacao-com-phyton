def mostrar_nome():
    nome = "Joao"
    return nome
print(mostrar_nome())


numero = 10
def calculo():
   global numero
   numero = 20
    
calculo()
print(numero)