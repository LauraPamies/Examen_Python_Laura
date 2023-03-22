#recibe el nombre de un fichero csv con muestras de vino
#y devuelve un diccionario con un formato
def read_data(nombrefichero):
    fichero = open(nombrefichero+".csv", mode="rt", encoding="utf-8")
    datosvino = dict()
    linea = fichero.readlines()
    cont =0
    linea = fichero.readline()
    while linea != "type,fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality" : #mientras haya lineas
        linea = fichero.readline()
        cont=cont+1
        print(linea)
        palabras = linea.strip().split() #divide todas las palabras de la linea
        print(palabras)
        datosvino.update({"dato"+str(cont): {
        "type" : palabras[1],
        "fixed acidity" : palabras[1],
        "citric acid" : palabras[2],
        "residual sugar" : palabras[3],
        "chlorides" : palabras[4],
        "free sulfur dioxide" : palabras[5],
        "total sulfur dioxide" : palabras[6],
        "density" : palabras[7],
        "PH" : palabras[8],
        "sulphates" : palabras[9],
        "alcohol" : palabras[10]}})
    fichero.close()
            

    return datosvino
