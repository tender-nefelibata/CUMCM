#!/usr/bin/env python
# coding=utf-8
# calculate x when F(x) min 
# F(x) = 6x^7 - 8x^6 + 7x^3 - 5x^2 - xy 
# y from user input
import random

y = int(input("please input Y"))
def getX():
    return random.uniform(0,100)


def getScore(x):
    score = 6*x**7-8*x**6+7*x**3-5*x**2-x*y
    return score


initT = 100
Tmin = 1e-8
k = 100 #iteration
delta = 0.98

t=initT

x_list = []
for i in range(100):
    x_list.append(getX())
while(t>Tmin):
    for i in range(100):
        x = getX()
        score_old = getScore(x_list[i])
        new_x = x + (random.random()*2-1) *t
        score_new = getScore(new_x)
        if (score_new < score_old):
            x = new_x
        else:
            p = 1 / (1+2.7**(-(score_new-score_old)/t))
            if(random.random() < p):
                x = new_x
            else:
                x_list[i] = x





    t = t*delta

score_list = [getScore(x) for x in x_list]
score = min(score_list)
print(score)
print(score_list.index(score))


