 #!"C:\Python33\python.exe"
'''
Imprime a tabuada do 1 ao 10.
'''

__version__ = "0.1.0"
__author__ = "Bruno"

numeros = list(range(1, 11))

# Iterable (percorriveis)
for numero1 in numeros:
    print("\n" "{:-^20}".format(f"Tabuada do {numero1}"))
    for numero2 in numeros:
        resultado = numero1 * numero2
        print("{:^20}".format(f"{numero1} * {numero2} = {resultado}")) #centralizando string

# fruit_encoded = '🍉'
# fruit_encoded = fruit_encoded.encode() #transformando img/emoji em texto
# print(fruit_encoded) #como é armazenado dentro do bd
# print(fruit_encoded.decode()) #puxando texto do bd e o transformando em img/emj 
