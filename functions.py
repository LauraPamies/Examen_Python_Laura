#recibe el nombre de un fichero csv con muestras de vino
#y devuelve un diccionario con un formato
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
        

    return datosvino


def split(diccionario):
    diccionariowhite = dict()
    for key in diccionario.keys():
        
