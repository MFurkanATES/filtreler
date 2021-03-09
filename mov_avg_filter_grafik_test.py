import numpy as np
import matplotlib.pyplot as plt
#bu filtre sanirsam onceden bi veriye sahip olmani gerektiriyor

global pre_mov_avg
pre_mov_avg = 0 

global k 
k = 0.0

#kac olcumun toplanip bolunecegi icin
p = 2

#veri dizisi




def mov_avg_filter(x,precision):
    weights = np.repeat(1.0, precision)/precision
    sma = np.convolve(x, weights, 'valid')
    return sma
  

x1 = np.linspace(0.0, 1.0,num = 9)
x2 = np.linspace(0.0, 1.0,num = 10)
#y2 = np.empty(10,dtype= float)

y2 = np.random.randint(1,100,(10))
y1 = mov_avg_filter(y2,p)

print np.shape(x1),np.shape(y1),np.shape(x2),np.shape(y2)


plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')


plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')


plt.show()