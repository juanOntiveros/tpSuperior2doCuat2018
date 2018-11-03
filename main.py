#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

#Constantes
CERO = 0
UNO = 1
DOS = 2
TRES = 3
CUATRO = 4
FILAS = 0
COLUMNAS = 1
NO_VERIFICADO = False
COEFICIENTES = "A de Coeficientes"
INDEPENDIENTES = "B de Terminos independientes"

MENU_PRINCIPAL="""Menu Principal
------
1.Norma 1
2.Norma 2
3.Norma Infinito
4.Resolver Sistema

0.SALIR """

#Funciones

def ingresoDeDatosDeLaMatriz(matriz, filas, columnas, nombre):
	"""Funcion que dada una matriz, el numero de filas, el numero de 
	columnas y el nombre de la misma le pide al usuario el ingreso de 
	los elementos que estaran dentro de ella. """
	print
	print "Ingrese los datos de la matriz {}".format(nombre)
	print
	for i in range(filas):
		for j in range(columnas):
			matriz[i][j] = input("Ingrese el dato de la fila {} y la columna {}: ".format(i+UNO,j+UNO))

def conseguirListasConValoresAbsolutosDeLaMatriz(matrizCoeficientes, filas, columnas):
	"""Funcion que recorre una matriz cuadrada e inversible y crea dos 
	listas. La primera tiene el valor absoluto de los elementos de la 
	diagonal y la segunda tiene el valor absoluta de la suma
	de los elementos de cada fila exceptuando el elemento de 
	la diagonal."""
	listaDiagonal = []
	listaSuma = []
	for i in range(filas):
		listaSuma.append(CERO)
		for j in range(columnas):
			if i == j:
				listaDiagonal.append(abs(matrizCoeficientes[i][j]))
			else:
				listaSuma[i]+= abs(matrizCoeficientes[i][j])
	return listaDiagonal, listaSuma
	
def verificarValoresAbsolutosDeLaMatriz(verificado, listaDiagonal, listaSuma):
	"""Funcion que dada dos listas verifica si los elementos de la primera
	son mayores que la de la segunda."""
	i = CERO
	while (verificado and i < len(listaDiagonal)):
		verificado = (listaDiagonal[i] > listaSuma[i])
		i+=UNO
	return verificado
		
def verificacionMatrizEstrictamenteDominante(matrizCoeficientes, verificado, filas, columnas):
	"""Funcion que verifica que una matriz sea Estrictamente 
	Dominante Diagonalmente"""
	if not verificado: 
		return verificado
	listaDiagonal, listaSuma = conseguirListasConValoresAbsolutosDeLaMatriz(matrizCoeficientes, filas, columnas)
	return verificarValoresAbsolutosDeLaMatriz(verificado, listaDiagonal, listaSuma)

def verificacionMatrizCuadrada(filas, columnas):
	"""Funcion que verifica si una matriz es cuadrada."""
	if filas != columnas:
		print
		print "La matriz no es cuadrada."
	return filas == columnas

def verificacionMatrizInversible(matrizCoeficientes, verificado):
	"""Funciona que dada una matriz verifica si es inversible."""
	if not verificado: 
		return verificado
	determinante = calcularDeterminante(copiarMatriz(matrizCoeficientes))
	if (determinante == CERO):
		print
		print "La matriz ingresada no es inversible."
	return (determinante != CERO)

# Funciones sacadas de internet (sujetas a revision)	
	
def multiplicaFila(m,f,e):
	'''
	Multiplica la fila f por el valor e
	'''
	n=len(m)
	for c in range(n):
		m[f][c]=m[f][c]*e
		
def combinacion(m,i,j,e):
	'''
	Combina las filas i y j, añadiendo a la fila j el producto de la
	fila i por un factor e
	'''
	n=len(m)
	for c in range(n):
		m[j][c]=m[j][c]+e*m[i][c]
		
def intercambiaFilas(m,i,j):
	m[i],m[j] = m[j],m[i] 
	
def calcularDeterminante(m):
	'''
	Calcula el determinante poniendo ceros debajo
	de la diagonal principal
	'''
	n=len(m)
	det=1
	for i in range(n):
		j=primeroNoNulo(m,i)
		if j == n:
			return 0
		if i!=j:
			det=-1*det
			intercambiaFilas(m,i,j)
		det=det*m[i][i]
		multiplicaFila(m,i,1./m[i][i])
		for k in range(i+1,n):
			combinacion(m,i,k,-m[k][i])
	return det
	
def primeroNoNulo(m,i):
	'''
	A partir de la fila i, busca la primera fila j cuya entrada
	(i,j) es nula
	'''
	result=i
	while result<len(m) and m[result][i]==0:
		result=result+1
	return result

# Fin Funciones sacadas de internet (sujetas a revision)

def analisisDeMatriz(matrizCoeficientes, filas, columnas):
	"""Dada una matriz de coeficientes analiza si el sistema de ecuaciones
	lineales a la que esta asociada es apto para ser resuelto mediante
	un metodo iterativo."""
	verificado = verificacionMatrizCuadrada(filas, columnas)
	verificado = verificacionMatrizInversible(matrizCoeficientes, verificado)
	verificado = verificacionMatrizEstrictamenteDominante(matrizCoeficientes, verificado, filas, columnas)
	if not verificado:
		print
		print "La matriz ingresada no es Estrictamente Dominante Diagonalmente."
		print "Por favor vuelva a ingresar los datos hasta que se cumpla esta condicion."
	return verificado

def verificacionFilasyColumnas(filas,columnas):
	"""Verifica que el numero de filas y columnas dado no sea Cero."""
	if filas == CERO or columnas == CERO:
		print
		print "El numero de filas o columnas no puede ser cero." 
		print "Por favor vuelva a intentarlo: "
		return ingresoDeNumeroDeFilasyColumnas(filas, columnas)
	return filas, columnas

def ingresoDeNumeroDeFilasyColumnas(filas, columnas):
	"""Funcion que pide el ingreso del numero de filas y de columnas."""
	print
	filas = int(input("Ingrese el numero de filas: "))
	columnas = int(input("Ingrese el numero de columnas: "))
	return verificacionFilasyColumnas(filas,columnas)

def crearMatrizDeCeros(filas, columnas):
	matriz = []
	for i in range(filas):
		matriz.append([])
		for j in range(columnas):
			matriz[i].append(0)
	return matriz
	
def copiarMatriz(matriz):
	matrizNueva = []
	for i in range(len(matriz)):
		matrizNueva.append([])
		for j in range(len(matriz[CERO])):
			matrizNueva[i].append(matriz[i][j])
	return matrizNueva

def ingresoDeDatos():
	"""Funcion que pide el ingreso de todos los datos y los verifica."""
	verificado = NO_VERIFICADO
	while (not verificado):
		filas, columnas = ingresoDeNumeroDeFilasyColumnas(CERO, CERO)
		matrizCoeficientes = crearMatrizDeCeros(filas, columnas)
		matrizIndependientes = crearMatrizDeCeros(filas, UNO)
		ingresoDeDatosDeLaMatriz(matrizCoeficientes, filas, columnas, COEFICIENTES)
		verificado = analisisDeMatriz(matrizCoeficientes, filas, columnas)
	ingresoDeDatosDeLaMatriz(matrizIndependientes, filas, UNO, INDEPENDIENTES)
	return matrizCoeficientes, matrizIndependientes
	
def imprimirBienvenida():
	"""Despliega la bienvenida del sistema."""
	print "Bienvenido a SIEL"
	
def imprimirMenuPrincipal():
	"""Imprime el menu principal."""
	print 
	print MENU_PRINCIPAL

def imprimirVolviendoAlMenuPrincipal():
	print "Volviendo al menu principal..."
	print "-----"

def imprimirSistemaCargado():
	"""Imprime cuando el sistema fue cargado satisfactoriamente."""
	print "-----"
	print "Sistema de ecuaciones lineales cargado..."
	print "Deplegando menu principal..."

def seleccionarOpcion(minimo, maximo):
	"""Dado un minimo y un maximo, pide el ingreso de una opcion. """
	print "-----"
	opcion = int(input("Su opcion elegida es: "))
	if (opcion < minimo or opcion > maximo):
		print "Opcion elegida incorrecta. Vuelva a intentarlo"
		opcion = seleccionarOpcion(minimo, maximo)
	return opcion
	
def calcularNormaUno(matrizCoeficientes):
	"""Dada una matriz cuadrada calcula la norma 1 de la misma."""
	listaDeMaximos = []
	n = len(matrizCoeficientes)
	for j in range(n):
		listaDeMaximos.append(CERO)
		for i in range(n):
			listaDeMaximos[j] += int(abs(matrizCoeficientes[i][j]))
	print "----"
	print "La norma 1 de la matriz A es {}".format(max(listaDeMaximos))
	
def calcularNormaInfinito(matrizCoeficientes):
	"""Dada una matriz calcula la norma infinito de la misma."""
	listaDeMaximos = []
	n = len(matrizCoeficientes)
	for i in range(n):
		listaDeMaximos.append(CERO)
		for j in range(n):
			listaDeMaximos[i] += int(abs(matrizCoeficientes[i][j]))
	print "----"
	print "La norma infinito de la matriz A es {}".format(max(listaDeMaximos))

def multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes):
	matrizTranspuesta = matrizCoeficientes.transpose()
	return numpy.matmul(matrizTranspuesta,matrizCoeficientes)

def accionarDecisionDelMenuPrincipal(opcion, matrizCoeficientes, matrizIndependientes):
	"""Dada una opcion seleccionada, la ejecuta."""
	if (opcion == UNO):
		calcularNormaUno(matrizCoeficientes)
	if (opcion == DOS):
		#print multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes)
		return
	if (opcion == TRES):
		calcularNormaInfinito(matrizCoeficientes)
		return
	if (opcion == CUATRO):
		return
	if (opcion != CERO):
		imprimirVolviendoAlMenuPrincipal()
	
def ejecutarMenuPrincipal(matrizCoeficientes, matrizIndependientes):
	"""Ejecuta el menu principal."""
	opcion = UNO
	while (opcion != CERO):
		imprimirMenuPrincipal()
		opcion = seleccionarOpcion(CERO, CUATRO)
		accionarDecisionDelMenuPrincipal(opcion, matrizCoeficientes, matrizIndependientes)	
	
def main():
	"""Funcion principal del programa."""
	imprimirBienvenida()
	matrizCoeficientes, matrizIndependientes = ingresoDeDatos()
	imprimirSistemaCargado()
	ejecutarMenuPrincipal(matrizCoeficientes, matrizIndependientes)
	return 0

main()
