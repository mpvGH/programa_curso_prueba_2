"""
El fichero calificaciones.csv contiene las calificaciones de un curso. 
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en 
la al final del curso (convocatoria ordinaria). 

Escribir un programa que contenga las siguientes funciones:

1.	Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
La lista tiene que estar ordenada por apellidos.

2.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial 
de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

3.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los 
exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.


Se  debe  habilitar  GIT y  crear un   repositorio  en GITHUB ,  donde se realicen  “COMMIT”  por  cada  función (actualizaciones mínimas).
"""
import csv

# 1.	Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
# donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
# La lista tiene que estar ordenada por apellidos.

def recibir_calificaciones():
    lista = []
    ruta_archivo = input("Ingrese la ruta al archivo: ")
    with open(ruta_archivo, "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2, len(lector_csv)):
                    if linea[i] == "":
                        linea[i] = "0,0"
                        # Apellidos	Nombre	Asistencia	Parcial1	Parcial2	Ordinario1	Ordinario2	Practicas	OrdinarioPracticas
                Apellidos = linea[0]
                Nombre = linea[1]
                Asistencia = linea[2]
                
                def numeros_punto_flotante(nota):
                    if len(nota) == 2:
                        normalizacion = nota/10
                    else:
                        normalizacion = nota
                    return normalizacion
                
                Parcial1 = numeros_punto_flotante(linea[3])
                Parcial2 = numeros_punto_flotante(linea[4])
                Ordinario1 = numeros_punto_flotante(linea[5])
                Ordinario2 = numeros_punto_flotante(linea[6])
                Practicas = numeros_punto_flotante(linea[7])
                OrdinarioPracticas = numeros_punto_flotante(linea[8])
                lista.append({
                    'Apellidos':Apellidos,
                    'nombre': Nombre,
                    'Asistencia': Asistencia,
                    'Parcial1': Parcial1,
                    'Parcial2': Parcial2,
                    'Ordinario1': Ordinario1,
                    'Ordinario2': Ordinario2,
                    'Practicas': Practicas,
                    'OrdinarioPracticas': OrdinarioPracticas,
                                })
            else:
                pos = 1
    return lista

# 2.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
# y añada a cada diccionario un nuevo par con la nota final del curso. 
# El peso de cada parcial de teoría en la nota final es de un 30% mientras que 
# el peso del examen de prácticas es de un 40%.

def añadir_nota_final(calificaciones):
    lista = []
    for alumno in calificaciones:
        # Nos cercioramos de que las notas que tomaremos en cuenta corresponden  a las últimas rendidas para los casos de repetición de pruebas. (Ordinario1; Ordinario2; OrdinarioPracticas)
        if alumno['Ordinario1'] > 0:
            parcial1 = alumno["Ordinario1"]
        else:
            parcial1 = alumno['Parcial1']
            
        if alumno['Ordinario2'] > 0:
            parcial2 = alumno["Ordinario2"]
        else:
            parcial2 = alumno['Parcial2']
            
        if alumno['OrdinarioPracticas'] > 0:
            practicas = alumno["OrdinarioPracticas"]
        else:
            practicas = alumno['Practicas']
            
        alumno_final_1 = parcial1
        alumno_final2 = parcial2
        alumno_practicas = practicas
        nota_final = parcial1*30/100 + parcial2*30/100 + practicas*40/100
        alumno_apellidos = alumno['Apellidos']
        alumno_nombre = alumno['Nombre']
        alumno_asistencia = alumno['Asistencia']
        
        lista.append({
            'Apellidos':alumno_apellidos,
            'Nombre':alumno_nombre,
            'Asistencia':alumno_asistencia,
            'Parcial1':alumno_final_1,
            'Parcial2':alumno_final2,
            'Practicas':alumno_practicas,
            'NotaFinal':nota_final
        })
    return lista

# 3.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
# y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
# Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los 
# exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

def status_final(calificaciones):
    lista_ap = []
    lista_rp = []
    for alumno in calificaciones:
        alumno['Asistencia'] = alumno['Asistencia'].replace("%", "")
        aprobado = False
        if alumno['Asistencia'] >= 75 and alumno['Parcial1'] >= 4 and alumno['Parcial2'] >= 4 and alumno['Practicas'] >= 4 and alumno['NotaFinal'] >= 5:
            aprobado = True
        if aprobado:
            lista_ap.append(alumno)
        else:
            lista_rp.append(alumno)
    return lista_ap, lista_rp

def imprimir_alumnos_aprobados(calificaciones):
    ruta_final = input("Ingrese la ruta para el archivo que contiene los datos sobre los alumnos aprobados")
    with open(ruta_final, "w", newline = "") as archivo_final:
        escritor_csv = csv.writer(archivo_final, delimiter = ";")
        escritor_csv.writerow(['Apellidos', 'Nombre', 'Asistencia', 'Parcial1', 'Parcial2', 'Practicas', 'Nota Final'])
        
        for alumno in calificaciones:
            lista_imp = []
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            lista_imp.append(alumno['Apellidos'])
            escritor_csv.writerow(lista_imp)
            
    return

calificacion = recibir_calificaciones()
calificacion_final = añadir_nota_final(calificacion)
alumnos_aprobados, alumnos_reprobados = status_final(calificacion_final)
imprimir_alumnos_aprobados(alumnos_aprobados)