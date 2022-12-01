# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:56:54 2022

@author: Beth_El 2
"""

#BMI Exercise

#Defining the class BMI
class BMI():
    def __init__(self):
#Defining the parameters
        self.weight = 0
        self.height = 0
        self.bmi = 0

#Defining the attributes
    def set_weight(self,weight):
        self.weight = weight
        
    def set_height(self,height):
        self.height = height
        
#Setting up the calculation
    def calc_bmi(self):
        self.bmi = (self.weight/(self.height/100)**2)
        
#Setting the getter function and printing it
    def get_bmi(self):
        print(self.bmi)

#Defining the call function
def main():
    bmi = BMI()
    bmi.set_weight(70)
#Setting height to cm instead of m
    bmi.set_height(165)
    bmi.calc_bmi()
    bmi.get_bmi()

#Trying to print using word statement
#print(int(input("My BMI is %d : ", %bmi)
  
main()
        
    

