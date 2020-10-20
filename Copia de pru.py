
def es_primo(num):
	if num == 1 or num == 2:
		return True
	else : 
		cont = 0
		for i in range(1,num+1):
			if num % i ==0:
				cont = cont +1

	if cont == 2:
		return print("Es es primo")
	else:
		return print("No es primo")
				

es_primo(4)