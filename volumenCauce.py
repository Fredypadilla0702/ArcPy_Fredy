# accedemos a la libreria:
import arcpy

# Declara la variable
carpeta_entrada = r"D:\ArcPRO\CaudePrincipal\seccionesCauce"

# Definir el area de trabajo
arcpy.env.workspace = carpeta_entrada

# Listar los raster
datosRaster = arcpy.ListRasters()
print(datosRaster)
print("Cantidad de raster: " + str(len(datosRaster)))
datosRaster2 = datosRaster[0:10]

# se crea un archivo de texto para que se carguen los datos de volumen y elevacion max y min del raster
archivoSalida = open("D:\ArcPRO\CaudePrincipal\salidaVolCauce\salidaVolRaster1.txt", "a")
archivoSalida.write("Archivo_Raster,Cota_Maxima,Cota_Media,Cota_Minima,Volumen" + " \n")

# con este for se recorre cada raster y se extrae la elevacion minima
for a in datosRaster:
    # se extrae el valor de elevacion minima
    elevationMax = arcpy.GetRasterProperties_management(a, "MAXIMUM")
    # print(elevationMin)
    # print(type(elevationMin))

    # se convierte el valor de elevacion a float(decimal)
    elevationMin2 = 0
    for i in elevationMax:
        elevationMax2 = float(i)

    # le sumamos 1.5 metros a la elevacion minima para subir el plano de referencia
    alturaDisminuida = 1.5
    elevationAdicional = elevationMax2 - alturaDisminuida

    # determinamos los valores de entrada para el proceso(surface volume), el texto de salida tambien es opcional
    rasterEntrada = carpeta_entrada + "//" + a
    planoReferencia = "ABOVE"
    alturaPlano = float(elevationAdicional)

    # se realiza el SurfaceVolume
    resultado = arcpy.SurfaceVolume_3d(rasterEntrada, "", planoReferencia, alturaPlano, 1, 0)

    # se extraen las otras propiedades del raster(cota maxima y media)
    elevationMin = arcpy.GetRasterProperties_management(a, "MINIMUM")
    elevationMed = arcpy.GetRasterProperties_management(a, "MEAN")

    # se muestra la salida y se filtra dicha salida para mostrar los datos de volumen con .find
    salida = resultado.getMessages()
    buscar1 = salida.find("2D")
    buscar2 = salida.find("Succeeded")

    # se imprimen los valores
    print(str(a) + " " + "Cota_Maxima=" + str(elevationMax) + " " + "Cota_Media=" + str(elevationMed) + " " +
          "Cota_Minima=" + str(elevationMin) + " " + salida[buscar1:buscar2])

    # se exportan los valores al archivo de texto y se filtra solo el dato de volumen con .find
    buscar3 = salida.find("Volume=")
    archivoSalida.write(str(a) + "," + str(elevationMax) + "," + str(elevationMed) + "," + str(elevationMin) + "," +
                        salida[(buscar3 + 7):buscar2])


archivoSalida.close()

print("fin del proceso")