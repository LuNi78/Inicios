#-*- coding: utf-8 -*-
__author__ = 'Lunatico'
__license__ = 'GPL'
__version__ = '0.01'

#==========================================#
#    Barra de progreso en consola win      #
#==========================================#

import time,os   # importo las librerias solo para el ejemplo , no son necesaria


# se tiene que pasar el valor en cada momento con un while por ejemplo

def progresoBarra(reci):
    porcentaje = (reci * 100) / 20      #  crea el porcentaje con referencia a una barra de progreso de 20 caracteres
    espacios = porcentaje / 5           # se toma la referencia para el progreso de la barra
    print('En proceso: ',porcentaje)
    print('0% |'+'#'*int(espacios)+(' '*(20 - int(espacios))+'| 100%'))

con = 0
while True:
    progresoBarra(con)
    time.sleep(1.5)       # solo para que el proceso no sea relampago en el ejemplo detengo el tiempo 1,5 s
    con += 1
    os.system('cls')      # limpia la consola
    if con == 21:         # detiene la ejecucion recordemos que la barra es de 20 espacios
        break