import numpy as np

#bu filtre sanirsam onceden bi veriye sahip olmani gerektiriyor

global pre_mov_avg
pre_mov_avg = 0 

global k 
k = 0.0

#kac olcumun toplanip bolunecegi icin
precision = 5

#veri dizisi
x = []

def mov_avg_filter(x,precision):
    weights = np.repeat(1.0, precision)/precision
    sma = np.convolve(x, weights, 'valid')
    return sma
  