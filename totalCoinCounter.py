import math,os, sys,random,time,turtle,operator
import datetime

def count_change(money,coins):
    ways=[1]+[0]*money

    for coin in coins:
        for i in range(coin,money+1):
            ways[i]+=ways[i-coin]
    return ways[money]



print(count_change(11  ,[5,7]))
