# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:41:25 2022

@author: Beth_El 2
"""

class CurrencyConverter():
    def __init__(self):
        self.__exchange_rate = 0.0
        
    def set_exchange_rate(self,rate):
        self.__exchange_rate = rate
        
    def convert_to_currency(self,amount):
        converted_currency = self.__exchange_rate * amount
        return converted_currency
    
def main():
    cc = CurrencyConverter()
    cc.set_exchange_rate(2.5)
    val = cc.convert_to_currency(20)
    print("Converted amount : ", val)
    
main()
 

        