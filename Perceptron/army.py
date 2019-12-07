#!/usr/local/bin/python
# coding: utf-8
import character as ch
import numpy as np
class Army:
    moralB = 0
    def __init__(self, chef, moralB):
        """Constructeur de notre classe"""
        self.chef = chef
        self.moralB = moralB

    """Getters"""
    def getChef(self):
        return self.chef

    def getMoralB(self):
        return self.moralB

    """Setters"""
    def setChef(self, chef):
        self.chef = chef

    def setMoralB(self, mo):
        self.moralB = mo

    def get_total_moral(self):
        total = float(self.moralB) * float(self.chef.getMoralBoost())
        return total

    def __str__(self):
        string = "Chef de l'armée : {}\n moral de base : {}\n".format(self.getChef(), self.getMoralB())
        return string