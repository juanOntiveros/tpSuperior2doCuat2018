#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Falta hacer toda la logica de los metodos de Jacobi y de Gauss Seidel.

"""

import numpy
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
AFIRMATIVO = "SI"
NEGATIVO = "NO"

MENU_PRINCIPAL="""Menu Principal
------
1.Norma 1
2.Norma 2
3.Norma Infinito
4.Resolver Sistema

0.Salir """

MENU_METODOS="""Menu de Metodos Disponibles
-----
1.Metodo de Jacobi
2.Metodo de Gauss Seidel

0.Volver al menu principal """

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
			matriz[i,j] = input("Ingrese el dato de la fila {} y la columna {}: ".format(i+UNO,j+UNO))

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
				listaDiagonal.append(abs(matrizCoeficientes[i,j]))
			else:
				listaSuma[i]+= abs(matrizCoeficientes[i,j])
	return listaDiagonal, listaSuma
	
def verificarValoresAbsolutosDeLaMatriz(verificado, listaDiagonal, listaSuma):
	"""Funcion que dada dos listas verifica si los elementos de la primera
	son mayores que la de la segunda."""
	i = CERO
	while (verificado and i < len(listaDiagonal)):
		verificado = (listaDiagonal[i] > listaSuma[i])
		i+=UNO
	return verificado
	
def inicioDePrograma():
	"""Da inicio a la ejecucion del programa."""
	return True

def terminarPrograma():
	"""Termina la ejecucion del programa."""
	return False
	
def decidirSiSeguirEjecutando():
	"""Le permite al usuario decidir si quiere seguir ejecutando el programa
	o salir definitivamente."""
	print "Desea salir definitivamente o dar origen a un nuevo set de datos? (Si/No)"
	decision = inicioDePrograma()
	seleccion = raw_input().upper()
	if seleccion == AFIRMATIVO:
		return terminarPrograma()
	if seleccion == NEGATIVO:
		return inicioDePrograma()
	else:
		print "Opcion incorrecta. Por favor vuelva a intentarlo..."
		return decidirSiSeguirEjecutando()
		
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
	determinante = numpy.linalg.det(matrizCoeficientes)
	if (determinante == CERO):
		print
		print "La matriz ingresada no es inversible."
	return (determinante != CERO)

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
	
def ingresoDeDatos():
	"""Funcion que pide el ingreso de todos los datos y los verifica."""
	verificado = NO_VERIFICADO
	while (not verificado):
		filas, columnas = ingresoDeNumeroDeFilasyColumnas(CERO, CERO)
		matrizCoeficientes = numpy.zeros((filas,columnas))
		matrizIndependientes = numpy.zeros((filas, UNO))
		ingresoDeDatosDeLaMatriz(matrizCoeficientes, filas, columnas, COEFICIENTES)
		verificado = analisisDeMatriz(matrizCoeficientes, filas, columnas)
	ingresoDeDatosDeLaMatriz(matrizIndependientes, filas, UNO, INDEPENDIENTES)
	return matrizCoeficientes, matrizIndependientes
	
def imprimirBienvenida():
	"""Despliega la bienvenida del sistema."""
	print "Bienvenido a SIEL"
	
def imprimirDespedida():
	"""Despliega la despedida del sistema."""
	print "-----"
	print "Gracias por usar SIEL!"
	
def imprimirMenuPrincipal():
	"""Imprime el menu principal."""
	print 
	print MENU_PRINCIPAL

def imprimirVolviendoAlMenuPrincipal():
	"""Imprime mensaje volviendo al menu principal."""
	print "Volviendo al menu principal..."
	print "-----"

def imprimirSistemaCargado(matrizCoeficientes, matrizIndependientes):
	"""Imprime cuando el sistema fue cargado satisfactoriamente."""
	imprimirMatrizDeCoeficientes(matrizCoeficientes)
	imprimirMatrizIndependientes(matrizIndependientes)
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
	"""Dada una matriz calcula la norma 1 de la misma."""
	listaDeMaximos = []
	for j in range(matrizCoeficientes.shape[COLUMNAS]):
		listaDeMaximos.append(CERO)
		for i in range(matrizCoeficientes.shape[FILAS]):
			listaDeMaximos[j] += int(abs(matrizCoeficientes[i,j]))
	print "----"
	print "La norma 1 de la matriz A es {}".format(max(listaDeMaximos))
	
def calcularNormaInfinito(matrizCoeficientes):
	"""Dada una matriz calcula la norma infinito de la misma."""
	listaDeMaximos = []
	for i in range(matrizCoeficientes.shape[FILAS]):
		listaDeMaximos.append(CERO)
		for j in range(matrizCoeficientes.shape[COLUMNAS]):
			listaDeMaximos[i] += int(abs(matrizCoeficientes[i,j]))
	print "----"
	print "La norma infinito de la matriz A es {}".format(max(listaDeMaximos))

def multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes):
	"""Hace el producto de la matriz transpuesta de coeficientes con
	la matriz normal de coeficientes."""
	matrizTranspuesta = matrizCoeficientes.transpose()
	return numpy.matmul(matrizTranspuesta,matrizCoeficientes)
	
def calcularLosAutovaloresDeUnaMatriz(matriz):
	"""Calcula los autovalores de una matriz dada."""
	return numpy.linalg.eigvals(matriz)

def calcularElMaximoValorModuloDeLosAutovalores(listaDeAutovalores):
	"""Dado una lista con los autovalores de una matriz, calcula el
	maximo valor en modulo entre ellos y lo devuelve."""
	for autovalor in listaDeAutovalores:
		autovalor = abs(autovalor)	
	return max(listaDeAutovalores)
	
def calcularNormaDos(matrizCoeficientes):
	"""Dada una matriz calcula la norma 2 de la misma."""
	matrizCalculada = multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes)
	listaDeAutovalores = calcularLosAutovaloresDeUnaMatriz(matrizCalculada)
	print "----"
	print "La norma 2 de la matriz A es {}".format(calcularElMaximoValorModuloDeLosAutovalores(listaDeAutovalores))

def imprimirMenuMetodos():
	"""Imprime el menu con los metodos disponibles para solucionar
	el sistema de ecuaciones lineales."""
	print 
	print MENU_METODOS

def ingresarVectorInicial(filas):
	"""Dado una cantidad de filas, le pide al usuario que ingrese el vector
	inicial con el cual se resolvera el metodo seleccionado y 
	luego lo devuelve."""
	vectorInicial = numpy.zeros((filas,UNO))
	print "-----"
	for i in range(filas):
		vectorInicial[i,CERO] = input("Ingrese la componente {} del vector inicial: ".format(i+UNO))
	return vectorInicial

def ingresarCotaDeError():
	"""Pide el ingreso de la cota de error para su posterior uso."""
	print "-----"
	return input("Ingrese la cota de error: ")
	
def ingresarCantidadDeDecimales():
	"""Pide el ingreso de la cantidad de decimales para su posterior uso."""
	print "-----"
	return input("Ingrese la cantidad de decimales: ")

def accionarDecisionDelMenuMetodos(opcion, matrizCoeficientes, matrizIndependientes):
	"""Dada una opcion seleccionada para el menu de metodos, la ejecuta."""
	if (opcion == UNO):
		return
	if (opcion == DOS):
		return
	if (opcion == CERO):
		imprimirVolviendoAlMenuPrincipal()

def ejecutarMenuMetodos(matrizCoeficientes, matrizIndependientes):
	"""Ejecuta el menu de metodos."""
	opcion = UNO
	while (opcion != CERO):
		imprimirMenuMetodos()
		opcion = seleccionarOpcion(CERO, DOS)
		accionarDecisionDelMenuMetodos(opcion, matrizCoeficientes, matrizIndependientes)

def accionarDecisionDelMenuPrincipal(opcion, matrizCoeficientes, matrizIndependientes):
	"""Dada una opcion seleccionada para el menu principal, la ejecuta."""
	if (opcion == UNO):
		calcularNormaUno(matrizCoeficientes)
	if (opcion == DOS):
		calcularNormaDos(matrizCoeficientes)
	if (opcion == TRES):
		calcularNormaInfinito(matrizCoeficientes)
	if (opcion == CUATRO):
		ejecutarMenuMetodos(matrizCoeficientes, matrizIndependientes)
	if (opcion != CERO):
		imprimirVolviendoAlMenuPrincipal()
		
def imprimirMatrizDeCoeficientes(matrizCoeficientes):
	"""Imprime la matriz de Coeficientes."""
	print "-----"
	print "La matriz de coeficientes es de la forma: "
	print matrizCoeficientes
	
def imprimirMatrizIndependientes(matrizIndependientes):
	"""Imprime la matriz de terminos independientes."""
	print "-----"
	print "La matriz columna de terminos independientes es de la forma: "
	print matrizIndependientes
	
def ejecutarMenuPrincipal(matrizCoeficientes, matrizIndependientes):
	"""Ejecuta el menu principal."""
	opcion = UNO
	while (opcion != CERO):
		imprimirMenuPrincipal()
		opcion = seleccionarOpcion(CERO, CUATRO)
		accionarDecisionDelMenuPrincipal(opcion, matrizCoeficientes, matrizIndependientes)
	return opcion
	
def main():
	"""Funcion principal del programa."""
	imprimirBienvenida()
	ejecutar = inicioDePrograma()
	while (ejecutar):
		matrizCoeficientes, matrizIndependientes = ingresoDeDatos()
		imprimirSistemaCargado(matrizCoeficientes,matrizIndependientes)
		ejecutarMenuPrincipal(matrizCoeficientes, matrizIndependientes)
		ejecutar = decidirSiSeguirEjecutando()
	imprimirDespedida()	
	return 0

main()
