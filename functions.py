from math import *


def read_data(nombrefichero):
    fichero = open(nombrefichero+".csv", mode="rt", encoding="utf-8")
    next(fichero)
    datosvino = dict()
    lineas = fichero.readlines()
    contvaloresllenos=0
    cont =0
    for linea in lineas:
        
        cont=cont+1
    
        palabras = linea.strip().split(",") #divide todas las palabras de la linea
        
        if len(palabras) == 13:
            contvaloresllenos =contvaloresllenos+1
            datosvino.update({"dato"+str(cont): {
            "type" : palabras[0],
            "fixed acidity" : palabras[1],
            "volatile acidity" : palabras[2],
            "citric acid" : palabras[3],
            "residual sugar" : palabras[4],
            "chlorides" : palabras[5],
            "free sulfur dioxide" : palabras[6],
            "total sulfur dioxide" : palabras[7],
            "density" : palabras[8],
            "PH" : palabras[9],
            "sulphates" : palabras[10],
            "alcohol" : palabras[11],
            "quality" : palabras[12]
            }})
    fichero.close()
        
    if contvaloresllenos <10:
        raise ValueError("Ha ocurrido la excepción ")

    return datosvino


def split(diccionario):
    diccionariowhite = dict()
    contwhite = 0

    diccionariored = dict()
    contred = 0

    for key in diccionario.keys():
        if diccionario[key]["type"] == "white":
            contwhite = contwhite+1
            diccionariowhite.update({"dato"+str(contwhite): {
            "fixed acidity" : diccionario[key]["fixed acidity"],
            "volatile acidity" : diccionario[key]["volatile acidity"],
            "citric acid" : diccionario[key]["citric acid"],
            "residual sugar" : diccionario[key]["residual sugar"],
            "chlorides" : diccionario[key]["chlorides"],
            "free sulfur dioxide" : diccionario[key]["free sulfur dioxide"],
            "total sulfur dioxide" : diccionario[key]["total sulfur dioxide"],
            "density" : diccionario[key]["density"],
            "PH" : diccionario[key]["PH"],
            "sulphates" : diccionario[key]["sulphates"],
            "alcohol" : diccionario[key]["alcohol"],
            "quality" : diccionario[key]["quality"]
            }})

        if diccionario[key]["type"] == "red":
            contred = contred+1
            diccionariored.update({"dato"+str(contred): {
            "fixed acidity" : diccionario[key]["fixed acidity"],
            "volatile acidity" : diccionario[key]["volatile acidity"],
            "citric acid" : diccionario[key]["citric acid"],
            "residual sugar" : diccionario[key]["residual sugar"],
            "chlorides" : diccionario[key]["chlorides"],
            "free sulfur dioxide" : diccionario[key]["free sulfur dioxide"],
            "total sulfur dioxide" : diccionario[key]["total sulfur dioxide"],
            "density" : diccionario[key]["density"],
            "PH" : diccionario[key]["PH"],
            "sulphates" : diccionario[key]["sulphates"],
            "alcohol" : diccionario[key]["alcohol"],
            "quality" : diccionario[key]["quality"]
            }})

    return diccionariowhite,diccionariored


def reduce(diccionario,texto):
    listafinal = list()
    for key in diccionario.keys():
        if texto != "fixed acidity" and texto != "volatile acidity" and texto != "citric acid" and texto != "residual sugar" and texto != "chlorides" and texto != "free sulfur dioxide" and texto != "total sulfur dioxide" and texto != "density" and texto != "PH" and texto != "sulphates" and texto != "alcohol" and texto!= "quality":
            raise ValueError("Ha ocurrido la excepción ")
        
        listafinal.append(diccionario[key][texto])

    return listafinal

def silhouette(lista1,lista2):
    distancia = 0
    distanciadistintalista = 0

    a = 0
    b = 0
    valores = 0
    valores2 = 0
    for i in lista1:
        for j in lista1:
            valores = valores + 1
            
            distancia = distancia + sqrt(pow(abs(i-j)),2)

        a = distancia / (valores-1)
        for value2 in lista2:
            valores2 = valores2 +1
            distanciadistintalista = distanciadistintalista + (sqrt(pow(abs(i-value2)),2))
        
        b = distanciadistintalista / (valores2-1)
    
    S= ((b-a) / max(a,b))
    return S
