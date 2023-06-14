import matplotlib.pyplot as plt
import math
import numpy as np

aci = np.linspace(2*np.pi,8*np.pi,25)
grafik1 = []
grafik2 = []
grafik3 = []
for i in range(len(aci)):
    grafik1.append(math.sin(aci[i]))
    grafik2.append(math.cos(aci[i]))
    grafik3.append(math.log10(aci[i]))

plot1 = plt.figure(1)
plt.plot(aci,grafik1,':+r')
plt.xlabel('x ekseni - açı değerleri')
plt.ylabel('y ekseni - sin değerleri')
plt.title('sinüs grafiği')
plt.legend('1')
plt.grid(True)
plt.ylim(-5,5)
plt.xlim(5,30)

plot2 = plt.figure(2)
plt.plot(aci,grafik2,'--og')
plt.xlabel('x ekseni - açı değerleri')
plt.ylabel('y ekseni - sin değerleri')
plt.title('cosinüs grafiği')
plt.legend('2')
plt.grid(True)
plt.ylim(-5,5)
plt.xlim(5,30)

plot1 = plt.figure(3)
plt.plot(aci,grafik3,'-m4')
plt.xlabel('x ekseni - açı değerleri')
plt.ylabel('y ekseni - sin değerleri')
plt.title('logaritma grafiği')
plt.legend('3')
plt.grid(True)
plt.ylim(-5,5)
plt.xlim(5,30)

plt.show()

