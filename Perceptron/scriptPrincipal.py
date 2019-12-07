
import character as ch
import army as ar
from random import randint
import numpy as np
import matplotlib.pyplot as mp
import perceptronTD as per
import csv


characters_list = []
armee_list = []
total_erreur= np.zeros((11,11))

with open('characters.csv') as f:
    f_csv = csv.reader(f)
    en_tetes = next(f_csv)
    for ligne in f_csv:
        name = ligne[0]
        first_name = ligne[1]
        age = ligne[2]
        profession = ligne[3]
        moralBoost = ligne[4]
        personnage = ch.Character(name, first_name, age, profession, moralBoost)
        characters_list.append(personnage)
        armee = ar.Army(personnage,randint(20,100))
        armee_list.append(armee)
"""for i in characters_list:
    print(i)
for e in armee_list:
    print(e.get_total_moral())
"""
print("Valeur totale de toutes les armée : ")
val_army = (np.random.random_sample(5))*(100-20)


val_persos = [0.97, 2, 1.3, 1.5, 0.1]
result = np.dot(val_army, val_persos)

print(result)

list_and = [[0,0],[0,1],[1,0],[1,1]]
list_sortie_and = [0, 0, 0, 1]
list_poids = np.arange(-5,6,1)


for w1 in list_poids:
    for w2 in list_poids:
        for index, h in enumerate(list_and):
            p = w1*h[0]+w2*h[1]
            if(p<=0):
                y=0
            else:
                y=1
            erreur = 0.5*(y-list_sortie_and[index])**2
            total_erreur[5+w1, 5+w2] += erreur

print("Voici les erreurs : ")
mp.imshow(total_erreur)
mp.show()


print("Perceptron :")
perceptron = per.Perceptron(2, 7, 0.01)
perceptron.train(list_and, list_sortie_and)
for i in list_and:
    print(perceptron.predict(i[0], i[1]))
    
perceptron.sauv_poids()
