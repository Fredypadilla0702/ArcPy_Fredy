
def rellenar(gridcode):
    # abrimos el archivo de texto de los volumenes para leerlo
    archivoSalida = open("D:\ArcPRO\ejemplo\salidaVolumen\salidaVolRasterTabla.txt", "r")
    # leemos la primera linea que es el encabezado para que no entre en el proceso
    encabezado = archivoSalida.readline()
    # leemos linea por linea con readlines()
    for l in archivoSalida.readlines():
        # con split la linea se convierte en una lista separada por coma
        lista = l.split(",")
        # print(lista)
        codigo = int(lista[0])
        contador = 0
        if codigo == gridcode:
            volumen = lista[4]
            contador = contador + 1
            break
    if contador == 1:
        return volumen
    else:
        return 0

    archivoSalida.close()


print(rellenar(2))



