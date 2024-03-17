import arcpy
# el arcpy.sa es para importar el proceso ExtractByMask
from arcpy.sa import *

archivo_raster = r"D:\shapes quito\imagenes geoinglobe\2_5 DTM INTEGRADO-20220818T200704Z-002\2_5 DTM " \
            r"INTEGRADO\Mod_Rio_Quito-001.TIF "

carpeta_shapes = r"D:\shapes quito\BancosArenas\sinUnir"
arcpy.env.workspace = carpeta_shapes

shapesArena = arcpy.ListFeatureClasses()
print(shapesArena)
print(len(shapesArena))

rasterMDE = arcpy.Describe(archivo_raster)
print(rasterMDE.dataType)

extraer = ExtractByMask(archivo_raster, shapesArena[0])

extraer.save(r"D:\shapes quito\VolumenArenas\split\arenafinal1.tif")

# separar = arcpy.SplitRaster_management()

print("proceso finalizado")
