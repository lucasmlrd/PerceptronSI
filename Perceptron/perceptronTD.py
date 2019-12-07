# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp
import csv
class Perceptron:

    def __init__(self, nombreInputs, epochs, learning_rate):
        """Constructeur de notre classe"""
        self.nombreInputs = nombreInputs
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.biais = 1
        self.biais_poids = 0
        self.list_poids=np.zeros(nombreInputs)
        self.erreur = []
        
    
    def predict(self, input1, input2):
        evalua = self.biais_poids*self.biais+self.list_poids[0]*input1+self.list_poids[1]*input2
        if(evalua <= 0):
            return 0
        else:
            return 1

    def train(self, inputs, attendu):
        for _ in range(self.epochs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i][0], inputs[i][1])
                for j in range(len(self.list_poids)):
                    nouvPoids = self.list_poids[j] + self.learning_rate * (attendu[i] - prediction) * inputs[i][j]
                    self.list_poids[j] = nouvPoids
                self.biais_poids = self.biais_poids + self.learning_rate * (attendu[i] - prediction) * 1
        
    def sauv_poids(self):
        filename = 'perceptronPoids.csv'
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            header_line = ['w1', 'w2', 'w-biais']
            csv_writer.writerow(header_line)
            csv_writer.writerow(self.list_poids + [self.biais_poids])
            
    def charger_poids(self):
        filename = 'perceptronPoids.csv'
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for line in csv_reader:
                poids = line
            for i in range(len(poids) - 1):
                self.list_poids[i] = poids[i]
            self.biais_poids = poids[-1]

        print(self)

    def __str__(self):
        return "Affichage perceptron : poids = {}, poids biais = {}".format(self.list_poids, self.biais_poids)