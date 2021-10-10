# Debemos crear un programa que realice la conversion de una moneda X a dolar

'''
	* Planificacion: * 
		- Elegir la moneda con la cual trabajaremos.
		- Tener valor actual del dolar.
		- Ingresar dinero a convertir.
		- valor de la moneda seleccionada en dolar
		- Convertir moneda a dolar.
		- Mostrar por pantalla el resultado

	* Solucion: *
		√ Presentamos el objetivo de nuestro programa. 
		√ Solicitamos el tipo de moneda a convertir:
			√ La almacenamos en una variable.
		√ Solicitamos la cantidad de dinero que queremos convertir.
		√ Funcion que valide la opcion ingresada por el usuario.
		√ Funcion que convertira el dinero a dolar:
			√ contendra la formula para realizar los calculos de cada moneda.
			√ retornara el resultado y lo almacenara en una variable global.
		√ Imprimimos el resultado.
'''

# Presentacion del programa:
print('Bienvenido al conversor mas popular de internet/nQue moneda desea convertir a Dolar?')
print('1) CLP/n2)COP/COL/n3)ARS/n4)Salir')

# almacenando opcion
type_of_currency = int(input('>> ')) 

# Solicitando cantidad a convertir
money_to_convert = int(input('Ingrese la cantidad de dinero a convertir/n>> $'))

# Almacenando resultado de conversion:
my_dollars = 0 

# Validando opcion ingresada por usuario:
def validate_option(opt):
		if opt == 1 or opt == 2 or opt == 3 or opt == 4:
				return opt 
		else:
				while opt > 4 or opt < 1:
					print('Por favor eliga una opcion valida')
					print('1) CLP/n2)COP/COL/n3)ARS/n4)Salir')
					opt  = int(input('>> ')) 
				
				return opt
# Convirtiendo moneda:
def currency_converter(status_validate, currency):
		if status_validate  == 1:
				return  0.0012 * money_to_convert

		elif status_validate  == 2:
				return  0.00027 * money_to_convert	
				 
		elif status_validate  == 3:
				return  0.010 * money_to_convert
		
		elif status_validate  == 4:
				return 'Gracias por usarme :)'

# Almacenando el resultado de la conversion:
my_dollars = currency_converter(validate_option(type_of_currency), money_to_convert)
# imprimir valor por pantalla:
print(f'Mi dinero : ${money_to_convert} ')
print(f'Mis dolares ${my_dollars}')
