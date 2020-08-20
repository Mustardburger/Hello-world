# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:52:01 2020

@author: Thien Phuc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dice_scores = np.array([1,2,3,4,5,6])
num_of_dice, num_of_tosses = 10, 10000
sums_of_score = np.array([])
for i in range(num_of_tosses):
    sum_of_score = np.array([np.random.choice(dice_scores) for dice in range(num_of_dice)]).sum()
    sums_of_score = np.append(sums_of_score, sum_of_score)
    
df = pd.Series(np.sort(sums_of_score))
df.to_csv('Dice roll scores 2.csv')
frequency = {}

for unique_sum in np.unique(sums_of_score):
    frequency[unique_sum] = (sums_of_score == unique_sum).sum()
unique_sums = np.array(list(frequency.keys()))
unique_sum_frequency = np.array(list(frequency.values()))
df = pd.DataFrame(unique_sums, unique_sum_frequency)
df.to_csv('Dice roll scores.csv')

plt.hist(sums_of_score)