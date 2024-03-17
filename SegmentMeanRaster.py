# accedemos a la libreria:
import arcpy
from arcpy.sa import *

# Declara la variable (carpeta donde estan las imagenes)
carpeta_imagenes = r"D:\ArcPRO\ClasificacionSup2\ImportLog"

# Definir el area de trabajo
arcpy.env.workspace = carpeta_imagenes

# Listar los raster
datosRaster = arcpy.ListRasters()
print(datosRaster)
print("Cantidad de raster: " + str(len(datosRaster)))

# con este for se recorre cada raster y para aplicarle el proceso SegmentMeanShift
for i in datosRaster:
    print(f"realizando proceso a {i}")

    # variables del SegmentMeanShift
    rasterEntrada = carpeta_imagenes + "//" + i
    detalleEspectral = "20"
    detalleEspacial = "5"
    minSegmentos = "20"
    indiceBandas = ""

    # se realiza el geo-proceso SegmentMeanShift
    segmentRaster = SegmentMeanShift(rasterEntrada, detalleEspectral, detalleEspacial, minSegmentos, indiceBandas)

    # se guarda la imagen a la que se le ha aplicado el geo-proceso
    segmentRaster.save(r"D:\ArcPRO\ClasificacionSup2\salidaSegment" + "//" + "Segment" + i)
