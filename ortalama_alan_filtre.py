import numpy as np
import matplotlib.pyplot as plt

global k 
k = 1.0
global pre_avg
pre_avg = 0.0




def avg_filter(x): 
  global pre_avg
  global k 
  alpha = (k - 1.0) / k
  average = alpha * pre_avg + (1 - alpha) * x
  pre_avg = average
  k = k + 1.0
  return  average
  


