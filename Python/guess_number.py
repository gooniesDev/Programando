# Voy a crear un programa que genere un numero aleatorio y el usuario deba adivinar este numero.

'''
	***Planificacion***
		- Mostrar instrucciones por pantalla.
		- Generar un numero aleatorio.
		- solicitar al usuario un numero.
		- comprobar si el numero ingresado es el mismo que el numero que contiene nuestra computadora.
		- Mostrar resultados.

	***Solucion***
		- Generar el numero aleatorio 
		- Crear una funcion que muestre el menu y solicite una de las opciones.
		- Solicitar input del numero generado en nuestra computadora.
		- Mostrar resultados.
'''

import random, sys

print('Bienevnido al adivina el numero\n Debes adivinar que numero a elegido nuestra super computadora\nEste numero se encuentra desde el 1 al 10, seras capaz?')

# Variables a utilizar
random_number = random.randint(1, 10)
input_option = '' 
input_number = 0
user_won = False

def game_state(state):
		if state != True:
				print('Lo siento pero mi computadoraa ganado')
		else:
				print('Haz sido el GANADOR!!')



def menu():
		while True:
				# Solicitamos a usuario una de las opciones desplegadas:			
				print('**Menu**\n1) Comenzar Juego\n2) Salir')
				input_option = input('Ingrese una opcion\n>> ')
				
				if input_option.strip() == '1':
						break
				elif input_option.strip() == '2':
						sys.exit() # Finalizamos nuestro programa.

def play_game():
		
		# Instrucciones del juego:
		print('Tendra 3 oprtunidades para darle al blanco al numero elegido por nuestra computadora')
		input_number = int(input('Ingrese el numero\n>> '))
		# Aranca el juego
		for i in range(2):
				if input_number != random_number:
						input_number = int(input('Ingrese el numero\n>> '))
						user_won = False
						continue
				else:
						user_won = True
						break
			

# Ejecutamos nuestro programa
menu()
play_game()
game_state(user_won)
print(f'La computadora selecciono el siguiente numero\n>> {random_number}\n')
