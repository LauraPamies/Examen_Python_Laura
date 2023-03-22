#recibe el nombre de un fichero csv con muestras de vino
#y devuelve un diccionario con un formato
def read_data(nombrefichero):
    fichero = open(nombrefichero+".csv", mode="rt", encoding="utf-8")

