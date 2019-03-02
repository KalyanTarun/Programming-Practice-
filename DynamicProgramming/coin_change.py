# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:38:02 2019

@author: Tarun
"""
from copy import deepcopy
coins=[1,2,3]
n=4
solns=0

def coins_change(bag,coin):
      global coins
      global n
      global solns
      bag.append(coin)
      
      if sum(bag) == n:
          solns+=1
      if sum(bag) < n:
          for coin_value in coins:
              coins_change(deepcopy(bag),coin_value)
              
      
    
    
    
def main():
    global solns
    coins_change([],coins[0])
    print(solns)
