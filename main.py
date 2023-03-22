from functions import *

try:
    diccionario = read_data("winequality")
except ValueError as e:
    print(e , type(e))
#print(diccionario)

diccionariowhite,diccionariored = split(diccionario)

#print(diccionariored)

listareducida = reduce(diccionariored,"quality")

#print(listareducida)