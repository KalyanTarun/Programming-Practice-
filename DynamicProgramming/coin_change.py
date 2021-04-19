# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:38:02 2019

@author: Tarun
"""
#Coin change applicable when coins are sorted
from copy import deepcopy
coins=sorted([1,2,3])
n=4
solns=0

def coins_change(bag,coin):
      global coins
      global n
      global solns
      
      if coin is not None:
          bag.append(coin)
      
      if sum(bag) == n:
          solns+=1
          print(bag)
          
      if sum(bag) < n or coin is None:
          for coin_value in coins:
              #Dp approach to eliminate the path if sum>n and if coin being added is greater than
              #last element in bag i.e to avoid duplicates
              if sum(bag) + coin_value > n or ( len(bag) > 0 and bag[-1] < coin_value):
                  break
              coins_change(deepcopy(bag),coin_value)
              
      
    
    
    
def main():
    global solns
    coins_change([], None)
    print(solns)
    
main()