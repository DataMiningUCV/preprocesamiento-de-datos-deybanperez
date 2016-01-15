import csv as csv
import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd

def deleteSpaces(array):
    array.sort()

    while (array[0] == ''):
        array = np.delete(array,0)

    return array

def modaLista(lista):
    aux = 0
    cont = 0
    moda = -1
    for i in range(0,len(lista)-1):
        cont +=1
        if (lista[i] == lista[i+1]):
            if cont >= aux:
                aux = cont
                moda = lista[i]
        else:
            cont=0

    return moda

def mixRows(array,index,string1,string2):
    for row in array:
        if string2 == '-':
            if row[index] != string1:
                row[index] = row[index+1]
        else:
            if row[index] == string1:
                row[index] = string2

#Se abre el archivo 'data.csv' que contiene el set de datos a procesar
csv_file_object = csv.reader(open('tarea_1/data.csv', 'rb'))
header = csv_file_object.next()  #Se ignora el encabezado del archivo de datos
data=[]                          #Crea una lista ára guardar los datos

for row in csv_file_object:      #Recorre todas las filas del csv
    data.append(row)             #añadiendo cada valor a la variable data

data = np.array(data)          #Convertimos de lista a arreglo
#.....................................................................
#..Vamos a eliminar las columnas que no nos proporcionan informacion..
#.....................................................................
data = np.delete(data,0,1) #Eliminamos la columna ""
data = np.delete(data,3,1) # Eliminamos la columna "edad"
mixRows(data,9,'No','-') # Unificacimos la columnas "Ha.cambiado.usted.de.direccion" con la columna "De.ser.afirmativo..indique.el.motivo"
data = np.delete(data,10,1) #Eliminamos la columna "De.ser.afirmativo..indique.el.motivo"
data = np.delete(data,10,1) #Eliminamos la columna "Numero.de.materias.inscritas.en.el.semestre.o.ano.anterior"

#Unificamos la columna "X.Estas.realizado.tesis...trabajo.de.grado.o.pasantias.de.grado"con la columna "Tesis...trabajo.de.grado.o.pasantas.de.grado"
for row in data:
    if ( ((row[17] == 'No') and (row[18] != '')) or (row[17] != 'No') ):
        row[17] = row[18]

var = data[0::,18] #Vaciamos los datos de la columna "Tesis...trabajo.de.grado.o.pasantas.de.grado"
var = deleteSpaces(var) #Removemos los espacios en blanco
moda = modaLista(var) #Calculamos la moda
mixRows(data,17,'',moda) # Reemplazamos los campos con el valor '' por la moda de la columna "Tesis...trabajo.de.grado.o.pasantas.de.grado"
data = np.delete(data,18,1) #Eliminamos la columna "Tesis...trabajo.de.grado.o.pasantas.de.grado"

#Unificamos la columna "Residencia.o.habitacion.alquilada" con la columna
# "En.caso.de.vivir.en.habitacion.alquilada.o.residencia.estudiantil..indique.el.monto.mensual"
var = data[0::,22] #Vaciamos la informacion de "En.caso.de.vivir.en.habitacion.alquilada.o.residencia.estudiantil..indique.el.monto.mensual"
var1 = data[0::,39] #Vaciamos la informacion de "Residencia.o.habitacion.alquilada"

# Nos quedamos con la parte numerica de la columna
for i in xrange(len(var)):
    line =var[i].split()

    if(len(line)>1):
        var[i] = line[0]
    elif (len(line) == 0):
        var[i] = '0'
# Nos quedamos con la parte numerica de la columna

#Reemplazamos los valores "NA" por 0's
for i in xrange(len(var1)):
    if(var1[i] == 'NA'):
        var1[i] = '0'

#Unificamos las columnas
for i in xrange(len(var1)):
    if (var1[i].astype(np.float) < var[i].astype(np.float)):
        var1[i] = var[i]

data[0::,39] = var1 #Reemplazamos la columna en el arreglo principal
data = np.delete(data,22,1) ##Eliminamos la columna "En.caso.de.vivir.en.habitacion.alquilada.o.residencia.estudiantil..indique.el.monto.mensual"
data = np.delete(data,23,1) #Eliminamos la columna "X.Contrajo.Matrimonio"
mixRows(data,23,'No','-') #Unificamos la columna "X.Ha.solicitado.algun.otro.beneficio.a.la.Universidad.u.otra.Institucion"
                        #con la columna "En.caso.afirmativo.señnale..año.de.la.solicitud..institucion.y.motivo"
data = np.delete(data,24,1) #Eliminamos la columna "En.caso.afirmativo.señnale..año.de.la.solicitud..institucion.y.motivo"
mixRows(data,24,'No','-') #Unificamos la columna "X.Se.encuentra.usted..realizando.alguna.actividad.que.le.genere.ingresos"
                        #con la columna "En.caso.de.ser.afirmativo..indique.tipo.de.actividad.y.su.frecuencia"
data = np.delete(data,25,1) #Eliminamos la columna "En.caso.de.ser.afirmativo..indique.tipo.de.actividad.y.su.frecuencia"
data = np.delete(data,29,1) #Eliminamos la columna "Ingreso.mensual.total"
data = np.delete(data,38,1) #Eliminamos la columna "Total.egresos"
data = np.delete(data,42,1) #Eliminamos la columna "Total.de.ingresos"
data = np.delete(data,51,1) #Eliminamos la columna "Total.de.egresos"

#............................................................................
#..Vamos reestructurar el orden de la informacion de las columnas restantes..
#............................................................................

#colocamos de primero los valores personales de los estudiantes
data[:,[1,0]] = data[:,[0,1]] #Intercambiamos "pRenovar" con "cIdentidad"
data[:,[2,1]] = data[:,[1,2]] #intercambiamos "pRenovar" con "fNacimiento"
data[:,[4,2]] = data[:,[2,4]] #intercambiamos "pRenovar" con "sexo"
data[:,[5,4]] = data[:,[4,5]] #intercambiamos "pRenovar" con "escuela"
data[:,[6,5]] = data[:,[5,6]] #intercambiamos "pRenovar" con "aIngreso"
data[:,[7,6]] = data[:,[6,7]] #intercambiamos "pRenovar" con "mIngreso"
data[:,[8,7]] = data[:,[7,8]] #intercambiamos "pRenovar" con "sCurso"
data[:,[17,8]] = data[:,[8,17]] #intercambiamos "pRenovar" con "tGrado"
data[:,[16,9]] = data[:,[9,16]] #intercambiamos "cDireccion" con "mInscritas"
data[:,[13,10]] = data[:,[10,13]] #intercambiamos "mAprobadas" con "pAprobado"
data[:,[14,11]] = data[:,[11,14]] #intercambiamos "mRetiradas" con "eficiencia"
data[:,[13,12]] = data[:,[12,13]] #intercambiamos "mReprobadas" con "mAprobadas"
data[:,[14,13]] = data[:,[13,14]] #intercambiamos "mReprobadas" con "mRetiradas"
data[:,[17,16]] = data[:,[16,17]] #intercambiamos "pRenovar" con "cDireccion"
data[:,[25,17]] = data[:,[17,25]] #intercambiamos "cDireccion" con "Beca"
data[:,[21,20]] = data[:,[20,21]] #intercambiamos "pReside" con "tVivienda"
data[:,[24,23]] = data[:,[23,24]] #intercambiamos "oSolicitudes" con "aIngreso"
data[:,[25,23]] = data[:,[23,25]] #intercambiamos la columna "aIngreso" con "cDireccion"
data[:,[38,26]] = data[:,[26,38]] #intercambiamos la columna "aResponsable" con "reconomico"
data[:,[39,27]] = data[:,[27,39]] #intercambiamos la columna "crFamilia" con "aOtros"
data[:,[38,28]] = data[:,[28,38]] #intercambiamos la columna "iActividades" con "aResponsable"
data[:,[38,29]] = data[:,[29,38]] #intercambiamos la columna "gAlimentacion" con "iActividades"
data[:,[39,30]] = data[:,[30,39]] #intercambiamos la columna "gTransporte" con "aOtros"
data[:,[38,31]] = data[:,[31,38]] #intercambiamos la columna "gAlimentacion" con "gMedicos"
data[:,[39,32]] = data[:,[32,39]] #intercambiamos la columna "gOdontologicos" con "gTransporte"
data[:,[38,33]] = data[:,[33,38]] #intercambiamos la columna "gMedicos" con "gPersonales"
data[:,[39,34]] = data[:,[34,39]] #intercambiamos la columna "gOdontologicos" con "gAlquiles"
data[:,[39,35]] = data[:,[35,39]] #intercambiamos la columna "gEstudios" con "gAlquiler"
data[:,[39,36]] = data[:,[36,39]] #intercambiamos la columna "gEstudios" con "gRecreacion"
data[:,[38,37]] = data[:,[37,38]] #intercambiamos la columna "gOtros" con "gPersonales"
data[:,[39,38]] = data[:,[38,39]] #intercambiamos la columna "gOtros" con "gRecreacion"
data[:,[43,42]] = data[:,[42,43]] #intercambiamos la columna "grVivienda" con "grAlimentacion"
data[:,[44,43]] = data[:,[43,44]] #intercambiamos la columna "grVivienda" con "grTransporte"
data[:,[45,44]] = data[:,[44,45]] #intercambiamos la columna "grVivienda" con "grMedicos"
data[:,[46,45]] = data[:,[45,46]] #intercambiamos la columna "grVivienda" con "grOdontologicos"
data[:,[47,46]] = data[:,[46,47]] #intercambiamos la columna "grVivienda" con "grEducativos"

#............................................................................
#..Vamos a imṕutar las diferentes columnas...................................
#............................................................................

#Imputamos la columna fNacimiento

var = data[0::,1] #Vaciamos la data de la columna fNacimiento

#Reemplazamos los '-' y los espacios en blanco por '/'
for i in xrange(len(var)):
    line = re.split(r'[- ]',var[i])
    if(len(line) == 3):
        var[i] = line[0] + "/" + line[1] + "/" + line[2]

#Acomodamos un valor mal escrito
var[19] = '22/04/1985'

#Si el dato no tenia delimitador, se lo agregamos y acomodamos el año d ela fecha
for i in xrange(len(var)):
    line = re.split(r'[/]',var[i])

    if(len(line) == 1):
        string = line[0]
        if (len(string) == 7):
            string = '0' + string
        var[i] = string[:2] + '/' + string[2:4] + '/' +string[4:]
        line = re.split(r'[/]',var[i])

    string = line[-1]
    if (len(string) == 2):
        string = '19' + string
        var[i] = line[0] + "/" + line[1] + "/" + string


data[0::,1] = var #Reemplazamos la columna en el arreglo principal

#Imputamos la columna sexo
#Binarizamos los valores categoricos
data[(data[0::,2] == "Femenino"),2] = '0'
data[(data[0::,2] == "Masculino"),2] = '1'

#Imputamos la columna eCivil
#Numerizamos las categorias
data[(data[0::,3] == "Soltero (a)"),3] = '0'
data[(data[0::,3] == "Casado (a)"),3] = '1'
data[(data[0::,3] == "Viudo (a)"),3] = '2'
data[(data[0::,3] == "Unido (a)"),3] = '3'

#Imputamos la columna escuela
#Numerizamos las categorias

for i in xrange(len (data)):
    line = data[i,4]

    if(line[0] == 'E'):
        data[i,4] = '0'
    else:
        data[i,4] = '1'

#Imputamos al columna mIngreso
#Numerizamos las categorias

for i in xrange(len(data)):
    line = re.split(r'[ ]',data[i,6])

    if (line[1] == 'OPSU'):
        data[i,6] = '0'
    elif (line[1] == 'Interinstitucionales'):
        data[i,6] = '1'
    elif (line[1] == 'Internos'):
        data[i,6] = '2'
    elif (line[1] == 'Interna'):
        data[i,6] = '3'

#Imputamos la columna sCurso
#Numerizamos los valores

for i in xrange(len(data)):
    line = data[i,7]

    if (line[0] == '1'):
        data[i,7] = '1'
    elif (line[0] == '2'):
        data[i,7] = '2'
    elif (line[0] == '3'):
        data[i,7] = '3'
    elif (line[0] == '4'):
        data[i,7] = '4'
    if (line[0] == '5'):
        data[i,7] = '5'
    elif (line[0] == '6'):
        data[i,7] = '6'
    elif (line[0] == '7'):
        data[i,7] = '7'
    elif (line[0] == '8'):
        data[i,7] = '8'
    elif (line[0] == '9'):
        data[i,7] = '9'
    elif (line[0] == '10'):
        data[i,7] = '10'

#Imputamos la columna tGrado
#Numerizamos las categorias
data[(data[0::,8] == "No"),8] = '0'
data[(data[0::,8] == "Primera vez"),8] = '1'
data[(data[0::,8] == "Segunda vez"),8] = '2'
data[(data[0::,8] != '0') & (data[0::,8] != '1') & (data[0::,8] != '0'),8] = '3'

#Imputamos la columna pAprobado
#Estandarizamos el formato

for i in xrange(len(data)):
    string = data[i,10]

    if(len(string) >2):

        if ((string[2] != '.') and  (string[1] != '.')):
            string = string[:2] + '.' +string[2:]
            data[i,10] = string

#Imputamos las columna eficiencia
#Estandarizamos el formato

for i in xrange(len(data)):
    string = data[i,11]

    if(len(string) > 1):
        if (string[0] == '1'):
            data[i,11] = '1'
        elif(string[1] != '.'):
            data[i,11] = '0.' + string

#Imputamos las columna mAprobadas
#categorizamos el formato

data[((data[0::,12] != '0') & (data[0::,12] != '1') & (data[0::,12] != '2') & (data[0::,12] != '3') & (data[0::,12] != '4') & (data[0::,12] != '5') & (data[0::,12] != '6') & (data[0::,12] != '7') & (data[0::,12] != '8') & (data[0::,12] != '9') & (data[0::,12] != '10')),12] = '11'

#Imputamos la columna jReprobadas
#Rellenamos los NAN

data[(data[0::,15] == ''),15] = 'No'

#Imputamos la columna pRenovar
#Estandarizamos el formato

data[((data[0::,16] == 'PRI 2014') | (data[0::,16] == 'PRI-2-2014') | (data[0::,16] == 'Pri-2014') | (data[0::,16] == 'pri 2014 II') | (data[0::,16] == 'pri-2014')),16] = '0' #Periodo I-2014

data[((data[0::,16] == '2014 II') | (data[0::,16] == '2014-02') | (data[0::,16] == '2014-02S') | (data[0::,16] == '2014-02s') | (data[0::,16] == '2014-02seg') | (data[0::,16] == '2014-2') | (data[0::,16] == '2014-2015') | (data[0::,16] == '2014-2s octubre-febrero') | (data[0::,16] == '2014-II') | (data[0::,16] == '2014_2015') | (data[0::,16] == 'II- 2014') | (data[0::,16] == 'SEG 2014') | (data[0::,16] == 'SEG-14') | (data[0::,16] == 'SEG-2014') | (data[0::,16] == 'SEG2014') | (data[0::,16] == 'Seg 2014') | (data[0::,16] == 'Seg-2014') | (data[0::,16] == 'Segundo semestre 2014') | (data[0::,16] == 'sec-14') | (data[0::,16] == 'seg 2014') | (data[0::,16] == 'seg 2014') | (data[0::,16] == 'seg- 14') | (data[0::,16] == 'seg-14') | (data[0::,16] == 'seg-2014') | (data[0::,16] == 'seg2014') | (data[0::,16] == 'II-2014')),16] = '1' #Periodo II-2014

data[((data[0::,16] == '1- periodo 2015') | (data[0::,16] == '1- periodo 2015') | (data[0::,16] == '2015-01') | (data[0::,16] == '2015-01S') | (data[0::,16] == '2015-01s') | (data[0::,16] == '2015-1') | (data[0::,16] == '2015-1S') | (data[0::,16] == '2015-s1') | (data[0::,16] == 'I- 2015 ') | (data[0::,16] == 'PRI 2015') | (data[0::,16] == 'PRI-15') | (data[0::,16] == 'PRI-2015') | (data[0::,16] == 'PRI-2105') | (data[0::,16] == 'PRI-2105') | (data[0::,16] == 'PRI/2015') | (data[0::,16] == 'PRI2015') | (data[0::,16] == 'PRI/2015') | (data[0::,16] == 'Pri 15') | (data[0::,16] == 'Pri 2015') | (data[0::,16] == 'Pri-15') | (data[0::,16] == 'Pri-2015') | (data[0::,16] == 'pri 2015') | (data[0::,16] == 'pri-15') | (data[0::,16] == 'pri-2015') | (data[0::,16] == 'pri2015') | (data[0::,16] == 'prim-2015') | (data[0::,16] == 'I-2015')),16] = '2' #Periodo I-2015

data[((data[0::,16] == '2015-2016') | (data[0::,16] == 'SEG-2015') | (data[0::,16] == 'seg-2015')),16] = '3' #Periodo II-2015

var = np.copy(data[0::,16])
var.sort()
moda = modaLista(var)

data[((data[0::,16] != '0') & (data[0::,16] != '1') & (data[0::,16] != '2') & (data[0::,16] != '3'),16)] = moda

#Imputamos la columna lProcedencia.
#Numerizamos los valores

data[((data[0::,18] == 'Altos Mirandinos')),18] = '0'
data[((data[0::,18] == 'Anzoategui')),18] = '1'
data[((data[0::,18] == 'Apure')),18] = '2'
data[((data[0::,18] == 'Aragua')),18] = '3'
data[((data[0::,18] == 'Barinas')),18] = '4'
data[((data[0::,18] == 'Barlovento')),18] = '5'
data[((data[0::,18] == 'Bolívar')),18] = '6'
data[((data[0::,18] == 'Delta Amacuro')),18] = '7'
data[((data[0::,18] == 'Guarenas - Guatire')),18] = '8'
data[((data[0::,18] == 'Guárico')),18] = '9'
data[((data[0::,18] == 'Lara')),18] = '10'
data[((data[0::,18] == 'Monagas')),18] = '11'
data[((data[0::,18] == 'Municipio Baruta')),18] = '12'
data[((data[0::,18] == 'Municipio Chacao')),18] = '13'
data[((data[0::,18] == 'Municipio El Hatillo')),18] = '14'
data[((data[0::,18] == 'Municipio Libertador Caracas')),18] = '15'
data[((data[0::,18] == 'Municipio Sucre')),18] = '16'
data[((data[0::,18] == 'Mérida')),18] = '17'
data[((data[0::,18] == 'Nueva Esparta')),18] = '18'
data[((data[0::,18] == 'Portuguesa')),18] = '19'
data[((data[0::,18] == 'Sucre')),18] = '20'
data[((data[0::,18] == 'Trujillo')),18] = '21'
data[((data[0::,18] == 'Táchira')),18] = '22'
data[((data[0::,18] == 'Valles del Tuy')),18] = '23'
data[((data[0::,18] == 'Vargas')),18] = '24'
data[((data[0::,18] == 'Yaracuy')),18] = '25'

#Imputamos al columna lResidencia
#Numerizamos los valore sy rellenamos los faltantes con la moda
data[((data[0::,19] == 'Altos Mirandinos')),19] = '0'
data[((data[0::,19] == 'Guarenas - Guatire')),19] = '1'
data[((data[0::,19] == 'Municipio Baruta')),19] = '2'
data[((data[0::,19] == 'Municipio Chacao')),19] = '3'
data[((data[0::,19] == 'Municipio El Hatillo')),19] = '4'
data[((data[0::,19] == 'Municipio Libertador Caracas')),19] = '5'
data[((data[0::,19] == 'Municipio Sucre')),19] = '6'
data[((data[0::,19] == 'Valles del Tuy')),19] = '7'

var = np.copy(data[0::,19])
var.sort()
moda = modaLista(var)
data[((data[0::,19] == '')),19] =moda

#Imputamos la coumna tVivienda
#Numerizamos los elementos
data[((data[0::,20] == 'Casa de vecindad') | (data[0::,20] == 'Casa en barrio rural') | (data[0::,20] == 'Casa en barrio urbano') | (data[0::,20] == 'Quinta o casa quinta') | (data[0::,20] == 'casa') | (data[0::,20] == 'Apartamento en quinta - casa quinta o casa')),20] = '0'
data[((data[0::,20] == 'Apartamento en edifico')),20] = '1'
data[((data[0::,20] == 'Habitación alquilada')),20] = '2'
data[((data[0::,20] == 'Residencia estudiantil')),20] = '3'
data[((data[0::,20] == 'conserjería ')),20] = '4'

#Imputamos la columna pReside
#Numerizamos los elementos
data[((data[0::,21] == 'Solo') | (data[0::,21] == 'sola')),21] = '0' #Nadie

data[((data[0::,21] == 'Ambos padres') | (data[0::,21] == 'Padres, hermana y abuelos maternos') | (data[0::,21] == 'ambos padres y dos hermanis')),21] = '1' #Ambos Padres

data[((data[0::,21] == 'Madre') | (data[0::,21] == 'Madre y Hermanos') | (data[0::,21] == 'Madre y hermano') | (data[0::,21] == 'Madre, Hermana, Abuela') | (data[0::,21] == 'Madre, Hermano y Sobrina') | (data[0::,21] == 'Mamá y Abuela') | (data[0::,21] == 'Mi Mamá y mi hijo ') | (data[0::,21] == 'madre y hermana') | (data[0::,21] == 'madre y hermanos') | (data[0::,21] == 'madre,hermano e hijo')),21] = '2' #Mama

data[((data[0::,21] == 'Padre')),21] = '3' #Papa

data[((data[0::,21] == 'Hermana') | (data[0::,21] == 'dos hermanos') | (data[0::,21] == 'hermana') | (data[0::,21] == 'hermanas') | (data[0::,21] == 'hermano') | (data[0::,21] == 'hermano, hermana y mi hijo')),21] = '4' #Hermano

data[((data[0::,21] == 'Esposo (a) Hijos (as) ') | (data[0::,21] == 'madre y su esposo,abuela,y mi esposo')),21] = '5' #Esposo

data[((data[0::,21] == 'Familiares maternos') | (data[0::,21] == 'Familiares paternos') | (data[0::,21] == 'abuela') | (data[0::,21] == 'madrina') | (data[0::,21] == 'prima')),21] = '6' #Familiares

data[((data[0::,21] == 'Dueños del apartamento donde alquilo la habitacion') | (data[0::,21] == 'OTROS INQUILINOS') | (data[0::,21] == 'Residencia') | (data[0::,21] == 'compañeros de habitacion alquilada') | (data[0::,21] == 'dueña del apartamento') | (data[0::,21] == 'recidencia') | (data[0::,21] == 'residencia') | (data[0::,21] == 'residencia estudiantil') | (data[0::,21] == 'Amigos')),21] = '7' #Otros

#Imputamos la columna dHabitacion
#Estandarizamos los valores

data[(data[0::,22] == ''),22] = 'No'

#Imputamos la columna rEconomico
#Numerizamos los elementos

data[((data[0::,26] == 'Usted mismo') | (data[0::,26] == 'ninguno')),26] = '0' #Nadie

data[(data[0::,26] == 'Ambos padres'),26] = '1' #Ambos Padres

data[(data[0::,26] == 'Madre'),26] = '2' #MAma

data[(data[0::,26] == 'Padre'),26] = '3' #Papa

data[((data[0::,26] == 'Hermano') | (data[0::,26] == 'MI HERMANA') | (data[0::,26] == 'hermana')),26] = '4' #Hermano

data[((data[0::,26] == 'Cónyugue') | (data[0::,26] == 'esposo')),26] = '5' #Conyugue

data[((data[0::,26] == 'Familiares') | (data[0::,26] == 'abuela') | (data[0::,26] == 'tia')),26] = '6' #Familiar

#Imputamos la columna aResponsable
#Reemplazamos los valores NA por el valor neutro 0

data[(data[0::,28] == 'NA'),28] = '0'

#Imputamos la columna iActividades
#Reemplazamos los valores NA por el valor neutro 0

data[(data[0::,29] == 'NA'),29] = '0'

#Imputamos la columna aOtros
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,30] == 'NA'),30] = '0'

#Imputamos la columna gAlimentacion
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,31] == 'NA'),31] = '0'

#Imputamos la columna gTransporte
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,32] == 'NA'),32] = '0'

#Imputamos la columna gMedicos
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,33] == 'NA'),33] = '0'

#Imputamos la columna gOdontologicos
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,34] == 'NA'),34] = '0'

#Imputamos la columna gPersonales
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,37] == 'NA'),37] = '0'

#Imputamos la columna gRecreacion
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,38] == 'NA'),38] = '0'

#Imputamos la columna gOtros
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,39] == 'NA'),39] = '0'

#Imputamos la columna gOtros
#Reemplazamos los valores NA por el valor neutro 0
data[(data[0::,39] == 'NA'),39] = '0'

#Imputamos la columna irMensual
#Estandarizamos los elementos

for i in xrange(len(data)):
    line = re.split(r'[ ]', data[i,40]) #Revisamos los espacios en blanco
    if (len(line) == 2):
        if (line[1] == 'bs'):
            data[i,40] = line[0]
        else:
            data[i,40] = line[0] + line[1]

    line = re.split(r'[bs]', data[i,40]) #Revisamos los bs

    if(len(line) > 1):
        data[i,40] = line[0]

    line = re.split(r'[,]', data[i,40]) #Revisamos las comas

    if(len(line) == 2):

        if(len(line[1]) == 2):
            print i
            data[i,40] = line[0] + '.' + line[1]
        else:
            data[i,40] = line[0] + line[1]

    elif(len(line) > 2):
        data[i,40] = line[0] + line[1] + line[2]

    line = re.split(r'[.]', data[i,40]) #Revisamos los puntos

    if(len(line) > 1):

        if(len(line[1]) > 2):
            data[i,40] = line[0] + line[1]

#Imputamos la columna irOtros
#Normalizamos los tipos e impiutamos los valores faltantes

for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,41])

    if(len(line) > 1):
        data[i,41] = line[0]


data[((data[0::,41] == '') | (data[0::,41] == 'No')),41] = '0'

#Imputamos la columna gralimentacion
#Estandarizamos el tipo

for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,42])

    if(len(line) > 1):
        data[i,42] = line[0]

#Imputamos la columna grTransporte
#Estandarizamos el tipo

for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,43])

    if(len(line) > 1):
        data[i,43] = line[0]

#imputamos la columna grMedicos
#llenamos los valores faltantes por el valor neuto 0
for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,44])

    if(len(line) > 1):
        data[i,44] = line[0]

data[(data[0::,44] == ''),44] = '0'

#Imputamos la columna grOdontologicos
#Llenamos los valores faltantes por el valor neutro 0
data[(data[0::,45] == ''),45] = '0'

#Imputamos la columna grEducativos
#Llenamos los valores faltantes por el valor neutro 0
data[(data[0::,46] == 'NA'),46] = '0'

#Imputamos la columna grVivienda
#Llenamos los valores faltantes por el valor neutro 0
data[(data[0::,47] == ''),47] = '0'

for i in xrange(len(data)):
    line = re.split(r'[ ]',data[i,47])

    if(len(line) > 1):
        data[i,47] = line[0]

    line = re.split(r'[,]', data[i,47]) #Revisamos las comas

    if(len(line) == 2):

        if(len(line[1]) == 2):
            print i
            data[i,47] = line[0] + '.' + line[1]
        else:
            data[i,47] = line[0] + line[1]

var = data[0::,47].copy()
moda = modaLista(var)
data[(data[0::,47] == 'comodato'),47] = moda

#imputamos al columna grServicios
#Estandarizamos y sustituimos los valores faltantes por el neutro 0
for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,48])

    if(len(line) > 1):
        data[i,48] = line[0]

data[(data[0::,48] == ''),48] = '0'

#imputamos al columna grCondominio
#Estandarizamos y sustituimos los valores faltantes por el neutro 0

for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,49])

    if(len(line) > 1):
        data[i,49] = line[0]

data[(data[0::,49] == ''),49] = '0'


#imputamos al columna grOtros
#Estandarizamos y sustituimos los valores faltantes por el neutro 0
for i in xrange(len(data)):

    line = re.split(r'[bs]', data[i,50])

    if(len(line) > 1):
        data[i,50] = line[0]

data[(data[0::,50] == 'NA'),50] = '0'

clean_file = open("tarea_1/minable.csv", "wb")
clean_file_object = csv.writer(clean_file)

clean_file_object.writerow(["cIdentidad", "fNacimiento", "sexo", "eCivil", "escuela", "aIngreso", "mIngreso", "sCurso", "tGrado", "mInscritas", "pAprobado", "eficiencia", "mAprobadas", "mRetiradas", "mReprobadas", "jReprobadas", "pRenovar", "beca", "lProcedencia", "lResidencia", "tVivienda", "pReside", "dHabitacion", "cDireccion", "oSolicitudes", "aEconomica", "rEconomico", "crFamiliar", "aResponsable", "iActividades", "aOtros", "gAlimentacion", "gTransporte", "gMedicos", "gOdontologicos", "gAlquiler", "gEstudios", "gPersonales", "gRecreacion", "gOtros", "irMensual", "irOtros", "grAlimentacion", "grTransporte", "grMedicos", "grOdontologicos", "grEducativos", "grVivienda", "grServicios", "grCondominio", "grOtros", "rating", "sugerencias"])

for row in data:
    clean_file_object.writerow(row)

clean_file.close()

"""
df = pd.read_csv("tarea_1/clean_data.csv")


print df.describe()

df = df.drop('cIdentidad',1)
df = df.drop('sexo',1)
df = df.drop('eCivil',1)
df = df.drop('escuela',1)
df = df.drop('aIngreso',1)
df = df.drop('mIngreso',1)
df = df.drop('sCurso',1)
df = df.drop('tGrado',1)
df = df.drop('mInscritas',1)
df = df.drop('pAprobado',1)

print df.describe()

df = df.drop('eficiencia',1)
df = df.drop('mAprobadas',1)
df = df.drop('mRetiradas',1)
df = df.drop('mReprobadas',1)
df = df.drop('pRenovar',1)
df = df.drop('beca',1)
df = df.drop('lProcedencia',1)
df = df.drop('lResidencia',1)
df = df.drop('tVivienda',1)
df = df.drop('rEconomico',1)

print df.describe()

df = df.drop('crFamiliar',1)
df = df.drop('aResponsable',1)
df = df.drop('iActividades',1)
df = df.drop('aOtros',1)
df = df.drop('gAlimentacion',1)
df = df.drop('gTransporte',1)
df = df.drop('gMedicos',1)
df = df.drop('gOdontologicos',1)
df = df.drop('gAlquiler',1)
df = df.drop('gEstudios',1)

print df.describe()


plt.plot(df['rating'],'bo')
plt.ylabel('Rating Servicio de Becas crema')
plt.xlabel('Cedula Identidad')
plt.show()
"""