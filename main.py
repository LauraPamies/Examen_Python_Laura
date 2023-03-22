from functions import *

try:
    diccionario = read_data("winequality")
except ValueError as e:
    print(e , type(e))
#print(diccionario)

diccionariowhite,diccionariored = split(diccionario)

#print(diccionariored)

try:
    listareducida = reduce(diccionariored,"quality")
except ValueError as e:
    print(e, type(e))
#print(listareducida)