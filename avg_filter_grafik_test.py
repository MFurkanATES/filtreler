import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 1.0,num = 10)
x2 = np.linspace(0.0, 1.0,num = 10)
y2 = np.empty(10,dtype= float)


global k 
k = 1.0
global pre_avg
pre_avg = 0.0


nokta = np.random.randint(1,100,(10))
print np.shape(nokta)
y1 = nokta

def avg_filter(x): 
  global pre_avg
  global k 
  alpha = (k - 1.0) / k
  average = alpha * pre_avg + (1 - alpha) * x
  pre_avg = average
  k = k + 1.0
  return  average

for i in range(9):
  y2[i] = avg_filter(nokta[i])


print np.shape(x1),np.shape(y1),np.shape(x2),np.shape(y2)


plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()