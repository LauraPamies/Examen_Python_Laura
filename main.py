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
    listareducida2 = reduce(diccionariowhite,"quality")

except ValueError as e:
    print(e, type(e))
#print(listareducida)

#silhouette(listareducida,listareducida2)