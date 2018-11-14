#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import math

#Constantes
CERO = 0
UNO = 1
DOS = 2
TRES = 3
CUATRO = 4
NO_VERIFICADO = False
COEFICIENTES = "A de Coeficientes"
INDEPENDIENTES = "B de Terminos independientes"
AFIRMATIVO = "SI"
NEGATIVO = "NO"
BIENVENIDA = "BIENVENIDO A SIEL"
IMPRESION_DATOS = "IMPRESION DE LOS DATOS INGRESADOS"
INGRESO_DATOS = "INGRESO DE DATOS"
DESPEDIDA = "Gracias por usar SIEL!"

MENU_PRINCIPAL="""                                 MENU PRINCIPAL

1.Norma 1
2.Norma 2
3.Norma Infinito
4.Resolver Sistema

0.Salir """

MENU_METODOS="""                                 Menu de Metodos Disponibles

1.Metodo de Jacobi
2.Metodo de Gauss Seidel

0.Volver al menu principal """
	
#Funciones

def imprimirBienvenida():
	"""Despliega la bienvenida del sistema."""
	print 
	print BIENVENIDA.center(100," ")
	print
	print "En esta aplicacion trabajaremos con sistemas del tipo A.X = B"
		
def imprimirDespedida():
	"""Despliega la despedida del sistema."""
	print 
	print DESPEDIDA.center(100," ")
	
def imprimirMenuPrincipal():
	"""Imprime el menu principal."""
	print 
	print MENU_PRINCIPAL.center(100," ")

def imprimirVolviendoAlMenuPrincipal():
	"""Imprime mensaje volviendo al menu principal."""
	print
	print "Volviendo al menu principal..."
	print 

def imprimirSistemaCargado(matrizCoeficientes, matrizIndependientes):
	"""Imprime cuando el sistema fue cargado satisfactoriamente."""
	print
	print IMPRESION_DATOS.center(100," ")
	imprimirMatrizDeCoeficientes(matrizCoeficientes)
	print "La matriz de coeficientes es Estrictamente Dominante Diagonalmente."
	imprimirMatrizIndependientes(matrizIndependientes)
	print 


def imprimirMenuMetodos():
	"""Imprime el menu con los metodos disponibles para solucionar
	el sistema de ecuaciones lineales."""
	print 
	print MENU_METODOS.center(100," ")
	
def imprimirMatrizDeCoeficientes(matrizCoeficientes):
	"""Imprime la matriz de Coeficientes."""
	print
	print "La matriz de coeficientes es de la forma: "
	print matrizCoeficientes
	
def imprimirMatrizIndependientes(matrizIndependientes):
	"""Imprime la matriz de terminos independientes."""
	print
	print
	print "La matriz columna de terminos independientes es de la forma: "
	print matrizIndependientes
	
def inicioDePrograma():
	"""Da inicio a la ejecucion del programa."""
	return True

def terminarPrograma():
	"""Termina la ejecucion del programa."""
	return False

def ingresoDeDatosDeLaMatriz(matriz, filas, columnas, nombre):
	"""Funcion que dada una matriz, el numero de filas, el numero de 
	columnas y el nombre de la misma le pide al usuario el ingreso de 
	los elementos que estaran dentro de ella. """
	print
	print "Ingrese los datos de la matriz {}".format(nombre)
	print
	for i in range(filas):
		for j in range(columnas):
			matriz[i,j] = input("Ingrese el valor de la fila {}, columna {}: ".format(i+UNO,j+UNO))		
	
def ingresarVectorInicial(filas):
	"""Dado una cantidad de filas, le pide al usuario que ingrese el vector
	inicial con el cual se resolvera el metodo seleccionado y 
	luego lo devuelve."""
	vectorInicial = crearVectorDeCeros(filas)
	print 
	print "Vector Inicial	"
	for i in range(filas):
		vectorInicial[i,CERO] = input("Ingrese la componente {} del vector inicial: ".format(i+UNO))
	return vectorInicial

def ingresarCotaDeError():
	"""Pide el ingreso de la cota de error para su posterior uso."""
	print 
	cotaDeError = input("Ingrese la cota de error, por ej 0.001: ")
	if (cotaDeError < CERO):
		print "La cota no puede ser menor a cero. "
		cotaDeError = ingresarCotaDeError()
	return cotaDeError
	
def ingresarCantidadDeDecimales():
	"""Pide el ingreso de la cantidad de decimales para su posterior uso."""
	print
	return input("Ingrese la cantidad de decimales: ")
	
def ingresoDeNumeroDeFilasyColumnas(filas, columnas):
	"""Funcion que pide el ingreso del numero de filas y de columnas."""
	print
	print INGRESO_DATOS.center(100," ")
	print 
	filas = int(input("Ingrese el numero de filas de A: "))
	columnas = int(input("Ingrese el numero de columnas de A: "))
	return verificarFilasyColumnas(filas,columnas)
	
def ingresoDeDatos():
	"""Funcion que pide el ingreso de todos los datos y los verifica."""
	verificado = NO_VERIFICADO
	while (not verificado):
		filas, columnas = ingresoDeNumeroDeFilasyColumnas(CERO, CERO)
		matrizCoeficientes = crearMatrizDeCeros(filas, columnas)
		matrizIndependientes = crearVectorDeCeros(filas)
		ingresoDeDatosDeLaMatriz(matrizCoeficientes, filas, columnas, COEFICIENTES)
		verificado = analisisDeMatriz(matrizCoeficientes, filas, columnas)
	ingresoDeDatosDeLaMatriz(matrizIndependientes, filas, UNO, INDEPENDIENTES)
	return matrizCoeficientes, matrizIndependientes

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
		
def verificarValoresAbsolutosDeLaMatriz(verificado, listaDiagonal, listaSuma):
	"""Funcion que dada dos listas verifica si los elementos de la primera
	son mayores que la de la segunda."""
	i = CERO
	while (verificado and i < len(listaDiagonal)):
		verificado = (listaDiagonal[i] > listaSuma[i])
		i+=UNO
	return verificado
		
def verificarMatrizEstrictamenteDominante(matrizCoeficientes, verificado, filas, columnas):
	"""Funcion que verifica que una matriz sea Estrictamente 
	Dominante Diagonalmente"""
	if not verificado: 
		return verificado
	listaDiagonal, listaSuma = conseguirListasConValoresAbsolutosDeLaMatriz(matrizCoeficientes, filas, columnas)
	return verificarValoresAbsolutosDeLaMatriz(verificado, listaDiagonal, listaSuma)

def verificarMatrizCuadrada(filas, columnas):
	"""Funcion que verifica si una matriz es cuadrada."""
	if filas != columnas:
		print
		print "La matriz no es cuadrada."
	return filas == columnas

def verificarMatrizInversible(matrizCoeficientes, verificado):
	"""Funciona que dada una matriz verifica si es inversible."""
	if not verificado: 
		return verificado
	determinante = calcularDeterminante(matrizCoeficientes)
	if (determinante == CERO):
		print
		print "La matriz ingresada no es inversible."
	return (determinante != CERO)

def analisisDeMatriz(matrizCoeficientes, filas, columnas):
	"""Dada una matriz de coeficientes analiza si el sistema de ecuaciones
	lineales a la que esta asociada es apto para ser resuelto mediante
	un metodo iterativo."""
	verificado = verificarMatrizCuadrada(filas, columnas)
	verificado = verificarMatrizInversible(matrizCoeficientes, verificado)
	verificado = verificarMatrizEstrictamenteDominante(matrizCoeficientes, verificado, filas, columnas)
	if not verificado:
		print
		print "La matriz ingresada no es Estrictamente Dominante Diagonalmente."
		print "Por favor vuelva a ingresar los datos hasta que se cumpla esta condicion."
	return verificado

def verificarFilasyColumnas(filas,columnas):
	"""Verifica que el numero de filas y columnas dado no sea Cero."""
	if filas == CERO or columnas == CERO:
		print
		print "El numero de filas o columnas no puede ser cero." 
		print "Por favor vuelva a intentarlo: "
		return ingresoDeNumeroDeFilasyColumnas(filas, columnas)
	return filas, columnas
	
def crearMatrizDeCeros(filas, columnas):
	"""Crea una matriz de ceros, dado un numero de filas y columnas."""
	return numpy.zeros((filas, columnas), dtype = int)
	
def crearVectorDeCeros(filas):
	"""Crea un vector de ceros, dado un numero de filas."""
	return numpy.zeros((filas, UNO), dtype = int)
	
def calcularOrden(matriz):
	"""Calcula el orden de la matriz cuadrada dada."""
	return len(matriz)
	
def calcularDeterminante(matriz):
	"""Calcula el determinante de una matriz."""
	return numpy.linalg.det(matriz)
	
def calcularMatrizInversa(matriz):
	"""Calcula la inversa de una matriz."""
	return numpy.linalg.inv(matriz)
	
def calcularTranspuesta(matriz):
	"""Calcula la transpuesta de una matriz dada."""
	return matrizCoeficientes.transpose()
	
def calcularLosAutovaloresDeUnaMatriz(matriz):
	"""Calcula los autovalores de una matriz dada."""
	return numpy.linalg.eigvals(matriz)

def calcularSumaDeMatrices(primerMatriz, segundaMatriz):
	"""Calcula la suma de dos matrices dadas."""
	return (primerMatriz + segundaMatriz)
	
def calcularRestaDeMatrices(primerMatriz, segundaMatriz):
	"""Calcula la resta de dos matrices dadas."""
	return (primerMatriz - segundaMatriz)
	
def calcularLaNormaDeUnVector(vector):
	"""Calcula la norma de un vector dado."""
	return numpy.linalg.norm(vector)

def multiplicarMatrices(primerMatriz, segundaMatriz):
	"""Mutiplica una matriz por otra, si es posible."""
	return numpy.matmul(primerMatriz, segundaMatriz)

def multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes):
	"""Hace el producto de la matriz transpuesta de coeficientes con
	la matriz normal de coeficientes."""
	matrizTranspuesta = matrizCoeficientes.transpose()
	return numpy.matmul(matrizTranspuesta,matrizCoeficientes)

def conseguirMatrizDiagonal(matrizCoeficientes):
	"""Dada una matriz de Coeficientes A, consigue una matriz diagonal D
	con los coeficientes de la diagonal de A y la devuelve."""
	n = calcularOrden(matrizCoeficientes)
	matrizDiagonal = crearMatrizDeCeros(n,n)
	for i in range(n):
		matrizDiagonal[i,i]+=matrizCoeficientes[i,i]
	return matrizDiagonal
	
def conseguirMatrizTriangularSuperior(matrizCoeficientes):
	"""Dada una matriz de Coeficientes A, consigue una matriz triangular
	superior U con los coeficientes de la diagonal de A y la devuelve."""
	n = calcularOrden(matrizCoeficientes)
	matrizTriangularSuperior = crearMatrizDeCeros(n,n)
	for i in range(n):
		for j in range(n):
			if i < j:
				matrizTriangularSuperior[i,j]-=matrizCoeficientes[i,j]
	return matrizTriangularSuperior
	
def conseguirMatrizTriangularInferior(matrizCoeficientes):
	"""Dada una matriz de Coeficientes A, consigue una matriz triangular
	inferior L con los coeficientes de la diagonal de A y la devuelve."""
	n = calcularOrden(matrizCoeficientes)
	matrizTriangularInferior = crearMatrizDeCeros(n,n)
	for i in range(n):
		for j in range(n):
			if i > j:
				matrizTriangularInferior[i,j]-=matrizCoeficientes[i,j]
	return matrizTriangularInferior
	
def separarMatrizDeCoeficientes(matrizCoeficientes):
	"""Dada una matriz de coeficientes, devuelve las matrices D, L y U 
	que se consiguen a partir de ella.""" 
	matrizD = conseguirMatrizDiagonal(matrizCoeficientes)
	matrizL = conseguirMatrizTriangularInferior(matrizCoeficientes)
	matrizU = conseguirMatrizTriangularSuperior(matrizCoeficientes)
	return matrizD, matrizL, matrizU
	
def calcularMatrizTdeJacobi(matrizD, matrizL, matrizU):
	"""Dadas las matrices D,L y U, calcula la matriz T de Jacobi y 
	la devuelve."""
	matrizDInversa = calcularMatrizInversa(matrizD)
	matrizSuma = calcularSumaDeMatrices(matrizL, matrizU)
	return multiplicarMatrices(matrizDInversa, matrizSuma)
	
def calcularMatrizCdeJacobi(matrizD, matrizIndependientes):
	"""Dada una matriz D y la matriz de valores independientes, calcula 
	la matriz C de Jacobi y la devuelve."""
	matrizDInversa = calcularMatrizInversa(matrizD)
	return multiplicarMatrices(matrizDInversa, matrizIndependientes)	

def calcularMatrizToCdeGaussSeidel(matrizD, matrizL, matrizAdicional):
	"""Dada una matriz D y L, mas una matriz adicional, calcula la matriz
	T o C de Gauss Seidel y la devuelve. Para la matriz T debe recibir
	como matriz adicional a la matriz U y para la matriz C debe recibir
	la matriz de valores independientes."""
	matrizResta = calcularRestaDeMatrices(matrizD, matrizL)
	matrizRestaInversa = calcularMatrizInversa(matrizResta)
	return multiplicarMatrices(matrizRestaInversa, matrizAdicional)
	
def calcularElMaximoValorModuloDeLosAutovalores(listaDeAutovalores):
	"""Dado una lista con los autovalores de una matriz, calcula el
	maximo valor en modulo entre ellos y lo devuelve."""
	for autovalor in listaDeAutovalores:
		autovalor = abs(autovalor)	
	return max(listaDeAutovalores)
	
def calcularNormaUno(matrizCoeficientes):
	"""Dada una matriz calcula la norma 1 de la misma."""
	listaDeMaximos = []
	n = calcularOrden(matrizCoeficientes)
	for j in range(n):
		listaDeMaximos.append(CERO)
		for i in range(n):
			listaDeMaximos[j] += int(abs(matrizCoeficientes[i,j]))
	print "La norma 1 de la matriz A es {}".format(max(listaDeMaximos))
	
def calcularNormaDos(matrizCoeficientes):
	"""Dada una matriz calcula la norma 2 de la misma."""
	matrizCalculada = multiplicarTranspuestaPorMatrizNormal(matrizCoeficientes)
	listaDeAutovalores = calcularLosAutovaloresDeUnaMatriz(matrizCalculada)
	print "La norma 2 de la matriz A es {}".format(calcularElMaximoValorModuloDeLosAutovalores(listaDeAutovalores))
	
def calcularNormaInfinito(matrizCoeficientes):
	"""Dada una matriz calcula la norma infinito de la misma."""
	listaDeMaximos = []
	n = calcularOrden(matrizCoeficientes)
	for i in range(n):
		listaDeMaximos.append(CERO)
		for j in range(n):
			listaDeMaximos[i] += int(abs(matrizCoeficientes[i,j]))
	print "La norma infinito de la matriz A es {}".format(max(listaDeMaximos))
	
def calcularNormaInfinitoParaVector(vector):
	"""Calcula la norma infinito para un vector dado."""
	listaDeMaximos = []
	for i in range(len(vector)):
		listaDeMaximos.append(abs(vector[i,CERO]))
	return max(listaDeMaximos)	

def calcularCondicionDeCorte(vectorK, vectorKmenosUno):
	"""Dado un vector K y un vector K-1 calcula la condicion de corte para
	el metodo seleccionado. Devuelve la resta de ambos y el resultado calculado."""
	primerResultado = calcularRestaDeMatrices(vectorK, vectorKmenosUno)
	segundoResultado = calcularNormaInfinitoParaVector(primerResultado)
	tercerResultado = calcularNormaInfinitoParaVector(vectorK)
	cuartoResultado = (segundoResultado / tercerResultado)
	
	return primerResultado, cuartoResultado
	
def pedirDatosParaElMetodos(matrizCoeficientes):
	"""Pide los datos para su posterior utilizacion en el metodo 
	seleccionado y los devuelve."""
	n = calcularOrden(matrizCoeficientes)
	vectorInicial = ingresarVectorInicial(n)
	numeroDecimales = ingresarCantidadDeDecimales()
	cotaDeError = ingresarCotaDeError()
	return vectorInicial, numeroDecimales, cotaDeError
	
def calcularResultadosDelMetodo(matrizT, matrizC, vectorKmenosUno, cotaDeError):
	"""Calcula los resultados y el criterio de corte del metodo elegido
	para su posterior salida por pantalla. Devuelve una lista con los
	resultados y otra con los criterios de corte."""
	condicionDeCorte = UNO
	listaConResultados = []
	listaConCriteriosDeCorte = []
	while(condicionDeCorte >= cotaDeError):
		primerMatriz = multiplicarMatrices(matrizT, vectorKmenosUno)
		vectorK = calcularSumaDeMatrices(primerMatriz, matrizC)
		vectorResta, condicionDeCorte = calcularCondicionDeCorte(vectorK, vectorKmenosUno)
		listaConResultados.append(vectorK)
		listaConCriteriosDeCorte.append(vectorResta)
		vectorKmenosUno = vectorK
	return listaConResultados, listaConCriteriosDeCorte
	
def imprimirListaEnTabla(lista, numeroDecimales):
	"""Imprime en forma de tabla la lista que se le pase y con la cantidad
	de decimales establecida previamente."""
	for i in range(len(lista)):
		print i+UNO , 
		resultado = lista[i]
		for j in range(calcularOrden(resultado)):
			print round(resultado[j, CERO], numeroDecimales) ,
		print
	print

def imprimirVariables(listaConResultados, numeroDecimales):
	"""Imprime por pantalla las variables resultado del metodo elegido"""
	print
	VARIABLES = "Variables"
	print VARIABLES.center(50," ")
	imprimirListaEnTabla(listaConResultados, numeroDecimales)
	
def imprimirCriterioDeParo(listaConCriteriosDeCorte, numeroDecimales):
	"""Imprime por pantalla el criterio de paro resultado del metodo elegido"""
	CRITERIO = "Criterio de Paro"
	print CRITERIO.center(50," ")
	imprimirListaEnTabla(listaConCriteriosDeCorte, numeroDecimales)

def imprimirConjuntoDeValoresQueSatisfaceElSistema(listaConResultados):
	"""Imprime el conjunto de valores que satisfacen el sistema
	resultado del metodo elegido"""
	print
	SOLUCION = "Conjunto de valores que satisfacen el sistema"
	print SOLUCION.center(50," ")
	resultado = listaConResultados[len(listaConResultados) - UNO]
	for i in range(calcularOrden(resultado)):
		print int(round(resultado[i, CERO], UNO)) ,
	print

def imprimirResultadosDelMetodo(listaConResultados, listaConCriteriosDeCorte, numeroDecimales):
	"""Imprime por pantalla los resultados del metodo elegido."""
	imprimirVariables(listaConResultados, numeroDecimales)
	imprimirCriterioDeParo(listaConCriteriosDeCorte, numeroDecimales)
	imprimirConjuntoDeValoresQueSatisfaceElSistema(listaConResultados)
	
def calcularMetodoJacobi(matrizCoeficientes, matrizIndependientes):
	"""Calcula por el metodo de Jacobi la solucion del sistema dado."""
	vectorInicial, numeroDecimales, cotaDeError = pedirDatosParaElMetodos(matrizCoeficientes)
	matrizD, matrizL, matrizU = separarMatrizDeCoeficientes(matrizCoeficientes)
	matrizT = calcularMatrizTdeJacobi(matrizD, matrizL, matrizU)
	matrizC = calcularMatrizCdeJacobi(matrizD, matrizIndependientes)
	listaConResultados, listaConCriteriosDeCorte = calcularResultadosDelMetodo(matrizT, matrizC, vectorInicial, cotaDeError)
	imprimirResultadosDelMetodo(listaConResultados, listaConCriteriosDeCorte, numeroDecimales)
	
def calcularMetodoGaussSeidel(matrizCoeficientes, matrizIndependientes):
	"""Calcula por el metodo de Gauss Seidel la solucion del sistema dado."""
	vectorInicial, numeroDecimales, cotaDeError = pedirDatosParaElMetodos(matrizCoeficientes)
	matrizD, matrizL, matrizU = separarMatrizDeCoeficientes(matrizCoeficientes)
	matrizT = calcularMatrizToCdeGaussSeidel(matrizD, matrizL, matrizU)
	matrizC = calcularMatrizToCdeGaussSeidel(matrizD, matrizL, matrizIndependientes)
	listaConResultados, listaConCriteriosDeCorte = calcularResultadosDelMetodo(matrizT, matrizC, vectorInicial, cotaDeError)
	imprimirResultadosDelMetodo(listaConResultados, listaConCriteriosDeCorte, numeroDecimales)
		
def seleccionarOpcion(minimo, maximo):
	"""Dado un minimo y un maximo, pide el ingreso de una opcion. """
	print
	opcion = int(input("Ingresar la opcion elegida: "))
	if (opcion < minimo or opcion > maximo):
		print "Opcion elegida incorrecta. Vuelva a intentarlo"
		opcion = seleccionarOpcion(minimo, maximo)
	return opcion

def accionarDecisionDelMenuMetodos(opcion, matrizCoeficientes, matrizIndependientes):
	"""Dada una opcion seleccionada para el menu de metodos, la ejecuta."""
	if (opcion == UNO):
		calcularMetodoJacobi(matrizCoeficientes, matrizIndependientes)
	elif (opcion == DOS):
		calcularMetodoGaussSeidel(matrizCoeficientes, matrizIndependientes)
	elif (opcion == CERO):
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
	print
	print "Resultado:"
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
