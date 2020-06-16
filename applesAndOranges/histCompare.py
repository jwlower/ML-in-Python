"""
the simplest classifier there is, a colour histogram comparison algo
Use: compare apples and oranges from images
Need: general hist for ornages, apples, and negative cases
"""

#Libs we Need
import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

mu_1 = -4 #mean of the first distribution
mu_2 = 4 #mean of the second distribution
bin_num=100 #number of bins in each hist
data_1 = np.random.normal(mu_1, 2.0, 1000)
data_2 = np.random.normal(mu_2, 2.0, 1000)
hist_1, _ = np.histogram(data_1, bins=bin_num, range=[-15, 15])
hist_2, _ = np.histogram(data_2, bins=bin_num, range=[-15, 15])

plt.hist(hist_1, bins=bin_num)
plt.show()

def return_intersection(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection

intersection = return_intersection(hist_1,hist_2)

print(intersection)
