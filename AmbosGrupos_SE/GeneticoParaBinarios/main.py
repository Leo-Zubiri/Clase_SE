
def calc_FO(indv):
    return sum(indv)

#m = numero de genes
tot_genes = 10

#n  = numero de vectores
tot_individuos = 100  #numero de individuos

#Poblacion Inicial
import random as rnd
poblacion = []
for i in range(tot_individuos):
    poblacion.append([ rnd.randint(0,1)  for i in range(tot_genes)])

#print("Poblacion Inicial: ")
#for indv in poblacion:
#    print(indv)

padres = []
tot_padres = 50

for i in range(tot_padres):
    indexPadre1 = rnd.randint(0, tot_individuos-1) #aleatorio entre 0 y n-1
    indexPadre2 = rnd.randint(0, tot_individuos-1) #aleatorio entre 0 y n-1
    while(indexPadre1==indexPadre2):
        indexPadre2 = rnd.randint(0, tot_individuos - 1)  # aleatorio entre 0 y n-1

    tempPadre1 = poblacion[indexPadre1]
    tempPadre2 = poblacion[indexPadre2]

    if calc_FO(tempPadre1) >= calc_FO(tempPadre2):
        padres.append(tempPadre1.copy())
    else:
        padres.append(tempPadre2.copy())

#print("Padres para cruza: ")
#for index, padre in enumerate(padres):
#    print(index,".-", padre)

hijos = []
for i in range(0,tot_padres, 2):
    tempPadre1 = padres[i]
    tempPadre2 = padres[i+1]

    #Generar un aleatorio
    puntoCruza = rnd.randint(tot_genes)

    #La primera parte del padre 1, será la primera parte del hijo 1,
    # la segunda parte del padre 1, será la segunda parte del hijo 2

    # La primera parte del padre 2, será la primera parte del hijo 2,
    # la segunda parte del padre 2, será la segunda parte del hijo 1

    hijo1 = []
    hijo2 = []