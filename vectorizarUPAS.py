# accedemos a la libreria:
import arcpy
# el arcpy.sa es para importar el proceso MajorityFilter
from arcpy.sa import *

# Declara la variable
carpeta_entrada = r"D:\ArcPRO\proyectoUPAS\coberturasUPAs.gdb"

# Definir el area de trabajo
arcpy.env.workspace = carpeta_entrada

# Listar los raster
datosRaster = arcpy.ListRasters()
print(datosRaster)
print("Cantidad de raster: " + str(len(datosRaster)))

# realizar Filtro mayoritario 3 veces
for i in datosRaster:
    print("aplicando filtro")
    filtroMayor = arcpy.sa.MajorityFilter(i, "FOUR", "MAJORITY")
    filtroMayor.save(r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_1.tif")

    raster1 = r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_1.tif"
    filtroMayor = arcpy.sa.MajorityFilter(raster1, "FOUR", "MAJORITY")
    filtroMayor.save(r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_2.tif")
    arcpy.Delete_management(raster1)

    raster2 = r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_2.tif"
    filtroMayor = arcpy.sa.MajorityFilter(raster2, "FOUR", "MAJORITY")
    print("guardando raster")
    filtroMayor.save(r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_3.tif")
    arcpy.Delete_management(raster2)

    # vectorizamos el raster

    print("vectorizando raster")
    raster3 = r"D:\ArcPRO\proyectoUPAS\salidaFiltro\filtro" + i + "_3.tif"
    shapeSalida = r"D:\ArcPRO\proyectoUPAS\salidaPoligono\poly" + i + ".shp"
    rasterPoligono = arcpy.RasterToPolygon_conversion(raster3, shapeSalida, "SIMPLIFY", "VALUE")

    # agregamos columna de area al shape
    print("agregando columna de area")
    nombreColumna = "Area_m2"
    tipoColumna = "DOUBLE"

    arcpy.AddField_management(shapeSalida, nombreColumna, tipoColumna)

    # calculamos las areas en m2
    print("calculando areas")
    arcpy.CalculateGeometryAttributes_management(shapeSalida, [[nombreColumna, "AREA_GEODESIC"]], "METERS")

    # usamos Eliminate para borrar poligonos pequeños

    shpEntrada = shapeSalida
    tempLayer = "temp" + i + ".shp"
    expresion = '"Area_m2" < 50'
    shpSalida = r"D:\ArcPRO\proyectoUPAS\salidaPoligono2\cob" + i + ".shp"

    # creamos un archivo temporal
    print("creando shape temporal")
    arcpy.MakeFeatureLayer_management(shpEntrada, tempLayer)
    # seleccionamos los poligonos
    print("seleccionando atributos")
    arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", expresion)
    # utilizamos Eliminate para borrar los poligonos seleccionados
    print("eliminando poligonos seleccionados")
    arcpy.Eliminate_management(tempLayer, shpSalida)

    print(f"fin proceso {i}")
