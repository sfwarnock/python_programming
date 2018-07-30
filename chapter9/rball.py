# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 2018

@author: scott warnock
"""

#rball.py

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
    
def printIntro():
    print("This program simulates a game of racquet ball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")
    
def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate?"))
    return a, b, n

def simNGames(n, probA, probB):
    #Simulates n gmaes of racquetball between players whose abilites are
    #   are represented by the probability of winning a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    #Simulates n gmaes of racquetball between players whose abilites are
    #   are represented by the probability of winning a serve.
    #Returns final scores for A and B
    serving = "A"
    scoreA = 0
    ScoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                