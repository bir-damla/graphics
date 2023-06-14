import matplotlib.pyplot as plt
import numpy as np

sehir = ['artvin','samsun','ankara']
sicaklik = [[15,14,17,18],[16,18,12,13],[10,5,7,9]]
sicaklik = np.array(sicaklik)
s,gun = sicaklik.shape

x = 1+np.arange(gun)
y = np.arange(len(sehir))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in y:
    ax.bar(x,sicaklik[i,:],i,zdir = 'y')
ax.set_title('3d bar grafiği')
ax.set_xlabel('gün')
ax.set_ylabel('şehir')
ax.set_zlabel('sıcaklık')
plt.xticks(x)
plt.yticks(y,sehir)
plt.show()
